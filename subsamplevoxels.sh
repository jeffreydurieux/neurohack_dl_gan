#!/bin/bash
dir=$1

mkdir output/

for file in $dir*.nii.gz;
do
      fslmaths $file -subsamp2 output/$file
done


