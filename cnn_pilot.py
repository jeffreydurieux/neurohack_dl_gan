def cnn_pilot():


    import nibabel as nib
    import os
    import numpy as np
    from matplotlib import pyplot as plt
    import glob
    import tensorflow as tf
    print(tf.__version__)
    import keras
    import random
    %matplotlib inline

    # Read in data
    dat = np.load('/Users/benjaminwade/Desktop/HCP_DL_Project/data/hcp_dat.npy')
    print(dat.shape)

    # Normalize data
    dat_norm=[]
    for i in range(0,len(dat[:,1,1])):
        dat_norm.append(dat[i]/np.amax(dat[i]))
    dat_norm=np.array(dat_norm)
    dat_norm=np.expand_dims(dat_norm, axis=3)

    # Make (random) training and testing data partition and (random) outcome labels
    split_index=np.random.choice([0, 1], size=(len(dat_norm[:,1,1]),), p=[.3, .7])
    train_data=dat_norm[split_index==1,:,:]
    test_data=dat_norm[split_index==0,:,:]
    train_labels=np.random.choice([0, 1], size=(len(train_data[:,1,1]),), p=[.5, .5])
    test_labels=np.random.choice([0, 1], size=(len(test_data[:,1,1]),), p=[.5, .5])

    # Build model
    model = keras.models.Sequential([
        keras.layers.Conv2D(64, (3,3), activation = 'relu', input_shape=(311,311,1)),
        keras.layers.MaxPooling2D(2,2),
        keras.layers.Conv2D(64, (3,3), activation = 'relu'),
        keras.layers.MaxPooling2D(2,2),
        keras.layers.Conv2D(64, (3,3), activation = 'relu'),
        keras.layers.MaxPooling2D(2,2),
        keras.layers.Conv2D(64, (3,3), activation = 'relu'),
        keras.layers.MaxPooling2D(2,2),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation = 'relu'),
        keras.layers.Dense(2, activation = 'softmax')
    ])

    # Fit model
    fit=model.fit(train_data, train_labels, epochs=3)

    test_loss = model.evaluate(test_data, test_labels)
    print(test_loss)

    return fit, test_loss