import os
from setting import main_dir, dataset_name
import pandas as pd



def get_path_and_label():
    directory=main_dir

    dataset=open(dataset_name, 'w')

    print('path,label', file=dataset)
    for d in os.listdir(directory):
        sd=os.path.join(directory,d)
        for f in os.listdir(sd):
            absolute=os.path.join(sd,f)
            print('{},{}'.format(absolute, d), file=dataset)


def get_label_name():
    data = pd.read_csv(dataset_name, index_col=False)
    data=data['label']
    data=data.drop_duplicates()
    class_label=list(data)
    return class_label