
# this data can be used to load numpy arrays and stack them
# or merging folder of images into one folder
# or nifti and similar ones as arrays
import os
import numpy as np
from os import listdir
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

channels = 1 # 1: Grayscale, 3: RGB
label_counts = 2 # how many classes in dataset?
test_ratio = 0.2 # split 20% of data as test set the 80 % would be the training set
input_folder = 'alldata'
data_folder = 'data'


def loader(input_folder):
    my_data = np.load(input_folder)
    # my_data = imread(input_folder, flatten= True if channels == 1 else False) # to make all the color layers into a single grayscale layer
    # my_data = imresize(my_data, (dim1, dim2, channels)
    # if your data is a picture uncomment the code above
    # so you can read your data using imread and resize your data using imresize
    labels = listdir(input_folder)
    X, Y = [], []
    # now merging data with labels
    for i, label in enumerate(labels):
    label_of_folder = input_folder+'/'+label
    for my_data_labeled in listdir(label_of_folder):
        my_data = get_data(label_of_folder+'/'+my_data_labeled)
        X.append(my_data)
        Y.append(i)

        return my_data_loaded

def splitter(my_data_loaded):
    X = X.reshape(X.shape[0], X.shape[1], X.shape[2])
    #Assuming for 2D array-like data input
    Y = np.array(Y).astype('float32')

    # train_test_splits splits the numpy array input with the given ratio, first we split as train as test_size
    # secondly we are using the previous test split and splitting again using the same command to have train test and val splits
    # so we are dividing test set twice and changing the test_size parameter each time so we can have same size of test and val

    # regular way of splitting data
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=test_ratio, random_state=42)
    x_test, x_val, y_test, y_val = train_test_split(x_test, y_test, test_size=0.5, random_state=42)

    # k-fold cross validation split

    #skf = StratifiedKFold(n_splits=kfold_splits, shuffle=True)
    #for index, (train_indices, val_indices) in enumerate(skf.split(X, Y)):
        #print "Training on fold " + str(index+1) + "/10..."    # Generate batches from indice
        #x_train, x_val = x_train[train_indices], x_val[val_indices]
        #y_train, y_val = y_train[train_indices], y_val[val_indices]
    # labels also could be made categorially but we will be doing it later as well
    # Y = to_categorical(Y, label_counts)
    return my_data_splitted

def saver():
    # save the final data as numpy :D
    np.save(data_folder+'/x_train.npy', x_train)
    np.save(data_folder+'/x_test.npy', x_test)
    np.save(data_folder+'/x_val.npy', x_val)
    return
