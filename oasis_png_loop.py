"""

This script loads the nifti T1w images from each subject's folder and,
by calling the function convert_nii_to_png.py transform each slice in a png image.
The converted images are then saved in the output folder (one different folder is created for each subject)

"""

import os
import glob
import re
import numpy as np
import subprocess

## Set the path where the nifti files are stored
base_path = '/home/ubuntu/OASIS_cropped'

## Extract subjects id from nifti filenames and creates a list
sub_list = []
scan_list = []
for item in os.listdir(base_path):
    try:
        subid = re.findall(r"\w+_s",item)[0]
        sub_list.append(subid[:-2])
    except:
        continue

## The list of id is trimmed in order to obtain an array of unique ids
sub_list = np.unique(np.array(sub_list))

## Nifti files for all subjects are listed
for id in sub_list:
    flist = glob.glob(os.path.join(base_path,'sub-%s_*.nii.gz' %id))
    scan_list.extend(flist)


## Each nifti file is passed to the convert_nii_to_png.py function and saved in its own subject directory
for scan in scan_list:
    print(scan)
    subid = re.findall(r"\w+_s",scan)[0][:-2]
    print(subid)
    outdir = '/home/ubuntu/data/oasis_pngimages/%s' %subid
    print(outdir)
    try:
        subprocess.call('mkdir %s' %outdir, shell=True)
    except:
        continue
    subprocess.call("python convert_nii_to_png.py %s %s" %(scan, outdir), shell=True)
