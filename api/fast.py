from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime
from datetime import date, datetime
import pandas as pd
import joblib

### TRYING TO DOWNLOAD A MODEL FROM THE CLOUD    ###

# from google.cloud import storage
# from sklearn.externals import joblib
# from tempfile import TemporaryFile

# storage_client = storage.Client()
# bucket_name=<bucket name>
# model_bucket='model.joblib'

# bucket = storage_client.get_bucket(bucket_name)
# #select bucket file
# blob = bucket.blob(model_bucket)
# with TemporaryFile() as temp_file:
#     #download blob into temp file
#     blob.download_to_file(temp_file)
#     temp_file.seek(0)
#     #load into joblib
#     model=joblib.load(temp_file)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# To allow developers to plug it in JavaScript code running inside of a browser when a web page is displayed.
@app.get("/")
def index():
    return {"greeting": "Hello world"}

@app.get("/predict")
def predict(sex='F', birthday = "19951201", EDUC=12, SES=1, MMSE=25, eTIV=1.2, nWBV=0.8, ASF=0.5):

    # Encode male and female
    # sex = sex.replace('M', '1')
    # sex = sex.replace('F', '0')

    # Encode Education
    # education = {'Lower than high school': '1',
    #             'High school graduate': '2',
    #             'Some college': '3',
    #             'College graduate': '4',
    #             'Beyond college': '5'}

    # for k, v in education.items():
    #     EDUC = EDUC.replace(k, v)

    # Calculate age from birthday
    # birthday = date(birthday)
    # today = date.today()
    # age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    birthday = datetime(year=int(birthday[0:4]), month=int(birthday[4:6]), day=int(birthday[6:8]))
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    result = {
    "M/F": str(sex),
    "Age": float(age),
    "EDUC": float(EDUC),
    "SES": float(SES),
    "MMSE": float(MMSE),
    "eTIV": float(eTIV),
    "nWBV": float(nWBV),
    "ASF": float(ASF)
    }

    X_pred = pd.DataFrame(result, index=[0])
    print(X_pred.dtypes)

    pipeline = joblib.load("../MemoBrainModel/model.joblib")
    #pipeline = joblib.load("gs://memobrain2/models/memobrain/v1/model.joblib")
    prediction = pipeline.predict(X_pred)

    prediction_result =  {"diagnosis": str(prediction[0])}

    return prediction_result

if __name__ == "__main__":
    print("It works")
    test = predict()
    print(test)
