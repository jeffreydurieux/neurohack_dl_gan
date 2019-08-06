# Author: Jeffrey Durieux j.durieux@fsw.leidenuniv.nl
# script for converting np.arrays to png images

import os 
import numpy as np
import imageio

os.chdir('/home/ubuntu/data/')

# load data, shape = (N , 311, 311), where N is number of subjects
data = np.load('hcp_dat.npy')


# for loop over the matrices and write as png to pngimages directory
os.chdir('/home/ubuntu/data/pngimages/')

print('Saving png images')

idx = np.shape(data)
for ii in range(idx[0]):
    imageio.imwrite('{}.png'.format(ii), data[ii])
    print('Image {} done'.format(ii))
