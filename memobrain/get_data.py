from google.cloud import storage
#from google.cloud import vision
import pandas as pd
import cv2
import glob
import numpy as np
import nibabel as nib
import tensorflow as tf
import matplotlib.pyplot as plt
from wand.image import Image

### GCP Storage - - - - - - - - - - - - - - - - - - - - - -
BUCKET_NAME = 'memobrain'
BUCKET_TRAIN_DATA_PATH = '/'

##### Data  - - - - - - - - - - - - - - - - - - - - - - - -
BUCKET_TRAIN_DATA_PATH = 'data/oasis_cross-sectional.csv'


def get_data():
    """method to get the training data (or a portion of it) from google cloud bucket"""
    #bucket = storage.Client.from_service_account_json('wagon-bootcamp-312423-bde5b1b38bca.json').get_bucket(BUCKET_NAME)
    #bucket = storage.Client.from_service_account_json(C19_API_KEY).get_bucket(BUCKET_NAME)
    print('###### get_data')

    def list_blobs_with_prefix(BUCKET_NAME, prefix, delimiter=None):
        print('###### list blobs prefix')
        #storage_client = storage.Client.from_service_account_json('wagon-bootcamp-312423-bde5b1b38bca.json')
        print()

        client = storage.Client()

        #storage_client = storage.Client.from_service_account_json(C19_API_KEY)

        bucket = client.bucket(BUCKET_NAME)
        blobs = client.list_blobs(BUCKET_NAME, prefix=prefix, delimiter=None)

        print("Blobs:")

        images = []

        #for blob in blobs:
        #     #print(blob.name)
        #     if blob.name.endswith(".img"):
        #         image = cv2.imdecode(np.asarray(bytearray(blob.download_as_string())), 0)
                 #print(image.shape)
         #        images.append(image)

        #ct = 0

        for blob in blobs:
            #print(blob)
            #while ct < 2500:
            #print(blob.name)
            if blob.name.endswith(".jpg"):
                #blob.download_to_filename('downloaded_image.png')
                image = cv2.imdecode(np.asarray(bytearray(blob.download_as_string())), 0)
                #print(bytearray(blob.download_as_string()))
                #image = nib.load(bytearray(blob.download_as_string()))#.get_fdata()
                #image = Image.open("downloaded_image.png") #.convert('RGB')
                #print(image.shape)
                images.append(image)
                #images.append(np.array(image))

            #ct +=1

        return images

    imgs = list_blobs_with_prefix(BUCKET_NAME, 'raw_data/OASIS1/OAS1_RAW/OAS1_0001_MR1/PROCESSED/MPRAGE/SUBJ_111/', '/')

    #save_file_to_gcp('test', imgs)
    print('Getting data completed')
    return imgs

if __name__ == '__main__':
    # get training data from GCP bucket
    df = get_data()
