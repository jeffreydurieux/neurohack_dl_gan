#!/bin/bash
# author: Jeffrey Durieux j.durieux@fsw.leidenuniv.nl
# date = 05-aug-2019

dir=$1

mkdir output/

for file in $dir*.nii.gz;
do
      fslmaths $file -subsamp2 output/$file
done


