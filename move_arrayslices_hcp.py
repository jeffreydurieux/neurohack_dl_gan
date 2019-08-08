#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:07:14 2019

@author: jeffreydurieux

# need to move array slices on aws
"""


import os
import pandas as pd
from shutil import copyfile

os.chdir('/Users/jeffreydurieux/Desktop/test/')

data = pd.read_csv('gan_dl_BehavioralData.csv')
list(data)

df = data[['Subject','age_category']]


os.chdir('/Users/jeffreydurieux/Desktop/test/array_slices/')

files = os.listdir()

# remove strings from list
files.remove('age0')
files.remove('age1')
files.remove('age2')
files.remove('age3')

Sid = []
for i in range(1112):
    Sid.append(files[i][:6])



# type cast Sid to int
Sid = list(map(int, Sid))

idx = df.Subject.isin(Sid)

# subset of data: data to work with
df = df[idx]

for ii in range(1112):
    data = df.iloc[ii]
    filenum = str(int(data['Subject']))
    age_cat = data['age_category']

    
    file = filenum + '_slice_100.npy'
    
    if age_cat == 0:
        print('age cat is 0')
        copyfile(src = file , dst = "age0/"+file)
        
    if age_cat == 1:
        print('age cat is 1')
        copyfile(src = file , dst = "age1/"+file)
        
    if age_cat == 2:
        print('age cat is 2')
        copyfile(src = file , dst = "age2/"+file)
        
    if age_cat == 3:
        print('age cat is 3')
        copyfile(src = file , dst = "age3/"+file)
