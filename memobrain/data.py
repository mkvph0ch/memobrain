import pandas as pd

AWS_BUCKET_PATH = "gs://memobrain/raw_data/OASIS2/oasis_longitudinal_demographics.csv"


def get_data():
    '''returns a DataFrame with nrows from the bucket'''
    df = pd.read_csv(AWS_BUCKET_PATH)
    return df

def clean_data(df, test=False):
    """ Drops unneeded columns:
    - 'MR Delay', 'Group' and 'Visit' (this information does not apply to the analysis)
    - 'Hand' (all patients are right handed)
    - 'Subject ID', 'MRI ID' (they are just identification strings)

    It splits the dataset into X and y. The target column 'CDR' is transformed into a binary class, giving the value of 0 to Non Demented and 1 to Demented (some level) """
    X=df.drop(columns=['CDR', 'MR Delay', 'Subject ID', 'MRI ID', 'Group', 'Visit', 'Hand'])
    y=df['CDR'].apply(lambda x: 1 if x>0 else 0)
    X['SES'].fillna(value=X['SES'].median(), inplace=True)
    X['MMSE'].fillna(value=X['MMSE'].median(), inplace=True)
    return X, y


if __name__ == '__main__':
    df = get_data()
