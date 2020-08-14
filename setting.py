
# main directory that contains audio for training and testing
# it has contains sub-derectory, sub-directory will become the label
# for classifier
main_dir = 'D:\sound classifier\drum'

# file that will store label and path to audio files
dataset_name = 'samples.csv'

# shapes of extracted features
row_shape = 4
column_shape = 32

# epoch and batch_size
epoch=72
batch_size=128

# model checkpoint name
model_name = 'drum_new.h5'





