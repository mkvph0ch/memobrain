from pathlib import Path
from PIL import Image
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def find_files(file_ext, cpath='.'):
    '''find all files with {file_ext} in {cpath}
    file_ext: str
    cpath: str or path object
    return <list>
    '''
    all_paths = []
    for file_path in Path(cpath).rglob(f"*.{file_ext}"):
        all_paths.append(file_path)

    return all_paths

def find_processed_files(file_ext, list_dirs, local_path, df):
    '''find all processed images with {file_ext} in {local_path/ID/PROCESSED/MPRAGE/T88_111/} which are in list_dirs
    file_ext: str
    list_dirs: list
    local_path: Path object
    df: pd.DataFrame
    '''
    # join all path
    all_paths = []
    for item in list(df['ID']):
        all_paths.append(local_path.joinpath(item).joinpath('PROCESSED/MPRAGE/T88_111/'))

    all_img = []

    for file_path in all_paths:
        for img_path in file_path.glob(f"*_t88_gfc_*.{file_ext}"):
            all_img.append(img_path)

    return all_img

def find_masked_files(file_ext, list_dirs, local_path, df):
    '''find all masked images with {file_ext} in {local_path/ID/PROCESSED/MPRAGE/T88_111/} which are in list_dirs
    file_ext: str
    list_dirs: list
    local_path: Path object
    df: pd.DataFrame
    '''
    # join all path
    all_paths = []
    for item in list(df['ID']):
        all_paths.append(local_path.joinpath(item).joinpath('PROCESSED/MPRAGE/T88_111/'))

    all_img = []

    for file_path in all_paths:
        for img_path in file_path.glob(f"*_t88_masked_*.{file_ext}"):
            all_img.append(img_path)

    return all_img

def convert_images(image_paths, file_ext='gif'):
    '''convert all images with suffix {file_ext} in {image_paths}
    image_paths: list (str or path objects)
    '''
    for image_path in image_paths:
        if image_path.suffix == f".{file_ext}":
            im = Image.open(image_path)
            im_jpg = image_path.parent.joinpath(f"{image_path.stem}.jpg")
            im.save(im_jpg)

    return None

def convert2tensor(array):
    '''Converts np.array to Tensor shape for CNN'''
    return np.array([image for image in array])

def binary_target(value):
    '''convert all dementia to 1, leave no dementia to 0'''
    if value != 0:
        return 1
    else:
        return value

def binary_sex(value):
    '''convert male to 1, female to 0'''
    if value == 'M':
        return 1
    elif value == 'F':
        return 0

def plot_cf_matrix(cf_matrix, model_name):
    '''plt the confusion matrix of a model'''
    group_names = ['True Neg','False Pos','False Neg','True Pos']

    group_counts = ["{0:0.0f}".format(value) for value in cf_matrix.flatten()]

    group_percentages = ["{0:.2%}".format(value) for value in cf_matrix.flatten()/np.sum(cf_matrix)]

    labels = [f"{v1}\n\n{v2}" for v1, v2 in zip(group_names,group_counts)]

    labels = np.asarray(labels).reshape(2,2)

    plt.title(model_name)
    sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues')

    return None

def plot_loss_accuracy(history, title=None):
    fig, ax = plt.subplots(1,2, figsize=(20,7))

    # --- LOSS ---

    ax[0].plot(history.history['loss'])
    ax[0].plot(history.history['val_loss'])
    ax[0].set_title('Model loss')
    ax[0].set_ylabel('Loss')
    ax[0].set_xlabel('Epoch')
    ax[0].set_ylim((0,3))
    ax[0].legend(['Train', 'Test'], loc='best')
    ax[0].grid(axis="x",linewidth=0.5)
    ax[0].grid(axis="y",linewidth=0.5)

    # --- ACCURACY

    ax[1].plot(history.history['accuracy'])
    ax[1].plot(history.history['val_accuracy'])
    ax[1].set_title('Model Accuracy')
    ax[1].set_ylabel('Accuracy')
    ax[1].set_xlabel('Epoch')
    ax[1].legend(['Train', 'Test'], loc='best')
    ax[1].set_ylim((0,1))
    ax[1].grid(axis="x",linewidth=0.5)
    ax[1].grid(axis="y",linewidth=0.5)

    if title:
        fig.suptitle(title)
