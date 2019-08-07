import os
import glob
import re
import numpy as np
import subprocess

base_path = '/home/ubuntu/OASIS3_T1'

sub_list = []
scan_list = []
for item in os.listdir(base_path):
    try:
        subid = re.findall(r"^\w+_M",item)[0]
        sub_list.append(subid[:-2])
    except:
        continue

sub_list = np.unique(np.array(sub_list))

for id in sub_list:
    flist = glob.glob(os.path.join(base_path,'%s_MR_*/*/*.nii.gz' %id))
    scan_list.extend(flist)

for scan in scan_list[0:2]:
    print(scan)
    subid = re.findall(r"\w+_M",scan)[0][:-2]
    print(subid)
    outdir = '/home/ubuntu/data/oasis_pngimages/%s' %subid
    print(outdir)
    try:
        subprocess.call('mkdir %s' %outdir, shell=True)
    except:
        continue
    subprocess.call("python convert_nii_to_png.py %s %s" %(scan, outdir), shell=True)
