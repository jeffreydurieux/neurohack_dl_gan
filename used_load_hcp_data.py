def load_hcp_data(credentials, slice_number=None):

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
    for i in enumerate(sid):
        print(i)
        sub = ny.hcp_subject(i[1])
        im = sub.load('MNINonLinear/T1w.nii.gz')
        data = im.get_fdata()
        im_array.append(data)
    
    arr = np.asarray(im_array)
   # arr_padded = np.pad(arr, [(0,0), (25,26), (0,0)], mode = 'constant') # hard coded to pad this dimension!
    
    return arr, sid

