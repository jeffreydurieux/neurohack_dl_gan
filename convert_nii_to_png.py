'''
Call using
python convert_nii_to_png.py path_to_inputfile output_directory

Expects a niftii file, loads it. The loaded data is a 3D array
Indexes array along the three axes and saves their slices in subdirectories:
axis 0, axis 1 and axis 2.

Params
------
inputFile: path to niftii
outputDir: path to output directory

Returns
-------
None

Saves files to outputDir/
'''
import os, sys
import nibabel as nib
from scipy import misc

def convertToSlices(filepath, outPath):
    if not os.path.exists(filepath):
        print('Filepath "'+filepath+'" does not exist. Exiting')
        sys.exit(2)

    filename =  filepath.split('/')[-1] # get the filename with extension
    filename = filename.split('.nii')[0] # remove .nii or .nii.gz from name

    outPath = outPath + '/axis'
    data = nib.load(filepath).get_data()

    for axis in [0, 1, 2]:
        # coronal, sag, axial directions
        out = outPath + str(axis)
        outFile =  out + '/' + filename + "_slice_{}.png"
        if not os.path.exists(out):
            os.makedirs(out)
        if axis == 0:
            for i in range(data.shape[axis]):
                misc.imsave(outFile.format(i), data[i, :, :])
        elif axis == 1:
            for i in range(data.shape[axis]):
                misc.imsave(outFile.format(i), data[:, i, :])
        elif axis == 2:
            for i in range(data.shape[axis]):
                misc.imsave(outFile.format(i), data[:, :, i])

# Process inputs
# Requires input file path,
# Optional output path
args = sys.argv[1:]
if len(args) < 2:
    print("Expects at least 1 argument: input file path and (optional) output directory, \n EXAMPLE: python test.py ./myNifti.nii.gz ./output ")
inPath = args[0]
outPath = args[1]

convertToSlices(inPath, outPath)
