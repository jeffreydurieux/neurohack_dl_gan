#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:19:00 2019

@author: Bastian
"""

import os, sys, glob
from PIL import Image

def image_padding(img, outsize):
    """ Function to pad and scale image to desired size"""
    
    old_size = img.size  # old_size[0] is in (width, height) format
    ratio = float(outsize)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    # use thumbnail() or resize() method to resize the input image
    # thumbnail is a in-place operation
    # im.thumbnail(new_size, Image.ANTIALIAS)
    img = img.resize(new_size, resample=Image.BICUBIC)
    # create a new image and paste the resized on it
    new_img = Image.new("L", (outsize, outsize))
    new_img.paste(img, ((outsize-new_size[0])//2,
                    (outsize-new_size[1])//2))
    
    return new_img

def resize_images(pngpath, outPath, size):
    
    if not os.path.exists(pngpath):
        print('Filepath "'+pngpath+'" does not exist. Exiting')
        sys.exit(2)
        
    
        
    outPath = outPath + '/slices/axis'
    
    for axis in [0, 1, 2]:
        # coronal, sag, axial directions
        filepath = pngpath + '/slices/axis' + str(axis) + '/'
        out = outPath + str(axis)
        
        if not os.path.exists(out):
            os.makedirs(out)
            
        for i in glob.glob(filepath + "*.png"):
            '''
            fd_img = open(i, 'r')
            img = Image.open(fd_img)
            img = resizeimage.resize_contain(img, [size, size])
            img.save(outFile, img.format)
            fd_img.close()
            '''
            
            filename =  i.split('/')[-1] # get the filename with extension
            filename_noext = filename.split('.png')[0] # remove png from name
            slicenumber = i.split('_')[-1]
            slicenumber = slicenumber.split('.png')[0]
            origimg = Image.open(i)
            
            outFile =  out + '/' + filename_noext + "_" + str(size) + \
            "_slice_" + slicenumber + "x" + slicenumber + ".png"
            
            img = image_padding(origimg, size)
            img.save(outFile.format(slicenumber), img.format)
            
args = sys.argv[1:]
if len(args) < 3:
    print("Expects at least 1 argument: input directory and (optional) output directory, \n EXAMPLE: python test.py ./myNifti.nii.gz ./output ")
inDir = args[0]
outDir = args[1]
sizeimg = int(args[2])

resize_images(inDir, outDir, sizeimg)
                
