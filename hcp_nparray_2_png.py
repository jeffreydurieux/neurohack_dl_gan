#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 15:57:55 2019
@author: jeffreydurieux
email: j.durieux@fsw.leidenuniv.nl

Warning! change absolute paths 
need to make a folder with <absolutpath>/pngimages
all subfolders in pngimages are made on the fly

"""


import os
import numpy as np
import imageio

os.chdir('/Users/jeffreydurieux/Desktop/')

dat = np.load('hcp_dat.npy')

np.shape(dat)
dat = dat[0,] # subjects X axis0 X axis1 X axis2

idx = np.shape(dat)


for subject in range(idx[0]):
    os.chdir('/Users/jeffreydurieux/Desktop/pngimages/')
    os.makedirs('subject{}'.format(subject))
    os.chdir('subject{}'.format(subject))
    
    datasubject = dat[subject]
    idxim = np.shape(datasubject)
    
    os.makedirs('axis0')
    os.makedirs('axis1')
    os.makedirs('axis2')
    
    for ax0 in range(idxim[0]):
        os.chdir('/Users/jeffreydurieux/Desktop/pngimages/subject{}/axis0/'.format(subject))
        imageio.imwrite('{}.png'.format(ax0), datasubject[ax0, :, :])
    for ax1 in range(idxim[1]):
        os.chdir('/Users/jeffreydurieux/Desktop/pngimages/subject{}/axis1/'.format(subject))
        imageio.imwrite('{}.png'.format(ax1), datasubject[:, ax1, :])
    for ax2 in range(idxim[2]):
        os.chdir('/Users/jeffreydurieux/Desktop/pngimages/subject{}/axis2/'.format(subject))
        imageio.imwrite('{}.png'.format(ax2), datasubject[:, :, ax2])


