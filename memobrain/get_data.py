from google.cloud import storage
import pandas as pd

### GCP Storage - - - - - - - - - - - - - - - - - - - - - -
BUCKET_NAME = 'memobrain2'

##### Data  - - - - - - - - - - - - - - - - - - - - - - - -
BUCKET_TRAIN_DATA_PATH = 'data/oasis_cross-sectional.csv'

def get_data():
    """method to get the training data (or a portion of it) from google cloud bucket"""
    df = pd.read_csv(f"gs://{BUCKET_NAME}/{BUCKET_TRAIN_DATA_PATH}", nrows=1000)
    return df

if __name__ == '__main__':
    # get training data from GCP bucket
    df = get_data()
