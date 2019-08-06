def load_hcp_data(credentials, slice_number):

    # Import dictionaries
    import neuropythy as ny
    import ipyvolume as ipv
    import nibabel as nib
    import numpy as np

    # Configure neuropythy
    ny.config['hcp_credentials'] = credentials
    fs = ny.data['hcp'].s3fs

    # Get full path to T1w NIFTIs
    fid = fs.ls('hcp-openaccess/HCP_1200/')
    fid.pop(0)
    fpath = []
    for f in fid:
        fpath.append(f +'/MNINonLinear/T1w.nii.gz')
    
    # Get list of subject IDs
    sid = []
    for f in fid:
        sid.append(f.split('/')[2])

    # Save single slice for each subject into concatenated array
    im_array = []
    sid_tmp = sid[0:3]
    for i in sid_tmp:
        print(i)
        sub = ny.hcp_subject(i)
        im = sub.load('MNINonLinear/T1w.nii.gz')
        data = im.get_fdata()
        im_array.append(data[:,:,slice_number])
    
    arr = np.asarray(im_array)
    arr_padded = np.pad(img, [(0,0), (25,26), (0,0)], mode = 'constant') # hard coded to pad this dimension!
    
    return arr, sid