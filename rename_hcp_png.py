import numpy as np
import os
import natsort

'''
Author: Jeffrey Durieux. j.durieux@fsw.leidenuniv.nl
'''

os.chdir('/home/ubuntu/data/hcp_pngimages/')
sid = np.load('../subjectid.npy')



mydir = os.listdir()
mydir = natsort.natsorted(mydir)



path = '/home/ubuntu/data/hcp_pngimages/'
mydirlen = len(mydir)
for folder in range(1112):
    os.chdir(path + mydir[folder])
    
    os.chdir('axis0')
    subdir = os.listdir()
    subdir = natsort.natsorted(subdir)
    
    pnglen = len(subdir)
    for im in range(pnglen):
        os.rename(subdir[im], mydir[folder]+'_'+subdir[im])
    
    
    os.chdir('../axis1')
    subdir = os.listdir()
    subdir = natsort.natsorted(subdir)
    pnglen = len(subdir)
    for im in range(pnglen):
        os.rename(subdir[im], mydir[folder]+'_'+subdir[im])
    
    os.chdir('../axis2')
    subdir = os.listdir()
    subdir = natsort.natsorted(subdir)
    pnglen = len(subdir)
    for im in range(pnglen):
        os.rename(subdir[im], mydir[folder]+'_'+subdir[im])
