import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#requirements
import nibabel as nib
from pathlib import Path



def get_file_paths(file_ext = 'img', ipath = '/Users/guehojang/code/Gueho/mkvph0ch/memobrain/raw_data/OASIS2'):
    '''retrieve all file paths(*.img)'''
    full_path = []
    for p in Path(ipath).rglob("*."+file_ext):
        full_path.append(str(p))

    return full_path

def get_mean_img_df(file_ext = 'img',
               ipath = '/Users/guehojang/code/Gueho/mkvph0ch/memobrain/raw_data/OASIS2',
               no_rows = -1):
    '''
    Get image dataframe.
    'Subject ID', 'session', 'file_names', 'full_path', 'image_files'
    datatype = 'mean' returns mean of 128 images of each mri image format.
    datatype = '3d' returns images with one plane(sag/cor/tra) of each mri image format.
    '''
    full_path = get_file_paths(file_ext, ipath)
    full_path.sort()

    if no_rows == -1:
        number = len(full_path)
    else:
        number = no_rows

    file_lists = []
    for i in full_path[:number]:
        mri_file = np.mean(nib.load(i).get_fdata(), axis = 2)
        file_lists.append([i, mri_file])

    file_df = pd.DataFrame(file_lists, columns = ['full_path', 'mean_img'])

    # plt.imshow(file_df.mean_img.iloc[0])
    # plt.title('Sample image = mean')
    # plt.show()

    return file_df

def get_plane_img_df(file_ext = 'img',
                     ipath = '/Users/guehojang/code/Gueho/mkvph0ch/memobrain/raw_data/OASIS2',
                     plane = 'sag',
                     no_rows = -1):
    '''
    Get image dataframe.
    'Subject ID', 'session', 'file_names', 'full_path', 'image_files'
    datatype = 'mean' returns mean of 128 images of each mri image format.
    datatype = '3d' returns images with one plane(sag/cor/tra) of each mri image format.
    '''
    full_path = get_file_paths(file_ext, ipath)
    full_path.sort()

    if no_rows == -1:
        number = len(full_path)
    else:
        number = no_rows

    file_lists = []
    for i in full_path[:number]:
        if plane == 'sag':
            mri_file = nib.load(i).get_fdata()[:,:,64]
            file_lists.append([i, mri_file])

        elif plane == 'cor':
            mri_file = nib.load(i).get_fdata()[128,:,:]
            file_lists.append([i, mri_file])

        elif plane == 'tra':
            mri_file = nib.load(i).get_fdata()[:,128,:]
            file_lists.append([i, mri_file])

    file_df = pd.DataFrame(file_lists, columns = ['full_path', 'plane'])

    return file_df



if __name__ == '__main__':
    # get training data from GCP bucket
    sag_img = get_plane_img_df(plane='sag')
    print(sag_img.head())
