import neuropythy as ny
hcp_cred = ''
ny.config['hcp_credentials'] = hcp_cred
fs = ny.data['hcp'].s3fs
fs.ls('hcp-openaccess/HCP_1200/111312/MNINonLinear/Results/rfMRI_REST1_LR')
sub = ny.hcp_subject(111312)
im = sub.load('MNINonLinear/Results/rfMRI_REST1_LR/rfMRI_REST1_LR_Atlas.dtseries.nii')
im
(lh_data, rh_data, subctx_data) = ny.hcp.cifti_split(im.dataobj)
lh_data.shape
sub.hemis['lh_LR32k']

hem = sub.hemis['lh_LR32k']
mesh = hem.surface('inflated')
ny.cortex_plot(mesh, color=lh_data[100], cmap='hot')
import ipyvolume as ipv
ipv.show()
