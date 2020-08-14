# Load various imports 
import pandas as pd
import os
from datetime import datetime 
import librosa
import numpy as np
from os import environ
environ['TF_CPP_MIN_LOG_LEVEL']='5'

from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint 
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, GlobalAveragePooling2D

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split 

from setting import row_shape, column_shape, batch_size, epoch, dataset_name, model_name
from get_data import get_path_and_label


print("Getting audio data")
get_path_and_label()
print("Completed")

def extract_features(file_name):

        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=128)
        mfccsscaled = np.mean(mfccs.T,axis=0)

        return mfccsscaled

metadata = pd.read_csv(dataset_name)

features = []


print("Extracting features")
# Iterate through each sound file and extract the features 
for index, row in metadata.iterrows():

    class_label = row["label"]
    data = extract_features(os.path.abspath(row["path"]))

    features.append([data, class_label])

# Convert into a Panda dataframe 
featuresdf = pd.DataFrame(features, columns=['feature','class_label'])

print('Finished feature extraction from ', len(featuresdf), ' files')



# Convert features and corresponding classification labels into numpy arrays
X = np.array(featuresdf.feature.tolist())
y = np.array(featuresdf.class_label.tolist())

# Encode the classification labels
le = LabelEncoder()
yy = to_categorical(le.fit_transform(y)) 

# split the dataset 


x_train, x_test, y_train, y_test = train_test_split(X, yy, test_size=0.2, random_state = 42)





num_rows = row_shape
num_columns = column_shape
num_channels = 1

x_train = x_train.reshape(x_train.shape[0], num_rows, num_columns, num_channels)
x_test = x_test.reshape(x_test.shape[0], num_rows, num_columns, num_channels)

num_labels = yy.shape[1]
filter_size = 2

# Construct model 
model = Sequential()
model.add(Conv2D(filters=64, kernel_size=2, input_shape=(num_rows, num_columns, num_channels), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.2))


model.add(Conv2D(filters=128, kernel_size=2, activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.2))
model.add(GlobalAveragePooling2D())

model.add(Dense(num_labels, activation='softmax'))


# Compile the model
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

# Display model architecture summary 
model.summary()

# Calculate pre-training accuracy 
score = model.evaluate(x_test, y_test, verbose=1)
print("Pre-training accuracy: ", score[0]) 




num_epochs = epoch
num_batch_size = batch_size

checkpointer = ModelCheckpoint(filepath=model_name, 
                               verbose=1, save_best_only=True)
start = datetime.now()

model.fit(x_train, y_train, batch_size=num_batch_size, epochs=num_epochs, validation_data=(x_test, y_test), callbacks=[checkpointer], verbose=1)


duration = datetime.now() - start
print("Training completed in time: ", duration)


# Evaluating the model on the training and testing set
score = model.evaluate(x_train, y_train, verbose=0)
print("Training Accuracy: ", score[1])

score = model.evaluate(x_test, y_test, verbose=0)
print("Testing Accuracy: ", score[1])