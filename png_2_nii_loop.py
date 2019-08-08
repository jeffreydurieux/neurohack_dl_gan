"""

This script loads png images of single slices from one participants and,
using the png_2_nii_GANversion.py script, converts them back into nifti 
file format relying on the information found in the original nifti file header.

"""

import os
import glob
import re
import numpy as np
import subprocess


base_path_input = ''
base_path_output = ''
base_path_realnii = '/home/ubuntu/OASIS3_T1/'

sub_list = []
for item in os.listdir(base_path_input):
    
    ### To be modified accordingly to the actual data structure 
    try:
        subid = re.findall(r"\w+_s",item)[0]
        sub_list.append(subid[:-2])
    except:
        continue

for sub in sub_list:
    inputdir = base_path_input+'/%s' %sub
    outdir = base_path_output+'/%s' %sub
    realnii = base_path_realnii+'%s_MR_d0105/*/*.nii.gz' %sub
    subprocess.call("python png_2_nii_GANversion.py %s %s %s" %(inputdir, realnii, outdir), shell=True)



