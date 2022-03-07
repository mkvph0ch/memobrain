from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
import pandas as pd
import joblib

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
def predict(sex='F', age = 20, Educ='Some college', SES=1, MMSE=25, eTIV=1.2, nWBV=0.8, ASF=0.5):

    # Encode male and female
    sex = sex.replace('M', '1')
    sex = sex.replace('F', '0')

    # Encode Education
    #Educ = Educ.map({''})

    result = {
    "M/F": int(sex),
    "Age": int(age),
    "Educ": str(Educ),
    "SES": float(SES),
    "MMSE": float(MMSE),
    "eTIV": float(eTIV),
    "nWBV": float(nWBV),
    "ASF": float(ASF)
    }

    X_pred = pd.DataFrame(result, index=[0])

    # pipeline = joblib.load("model.joblib")
    # prediction = pipeline.predict(X_pred)

    # prediction_result =  {"diagnosis": prediction[0]}

    return X_pred

if __name__ == "__main__":
    print("1234")
    result = predict()
    print(result)
