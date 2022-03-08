from sklearn import set_config; set_config(display='diagram')
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
import joblib
import pandas as pd

class Trainer():

    def get_data():
        '''Import the data from raw_data in the project folder'''
        data = pd.read_csv("~/code/mkvph0ch/memobrain/raw_data/OASIS2/oasis_longitudinal_demographics.csv")
        return data

    def prep_data(data):
            '''drops unneeded columns:
    - 'MR Delay', 'Group' and 'Visit' (this information does not apply to the analysis)
    - 'Hand' (all patients are right handed)
    - 'Subject ID', 'MRI ID' (they are just identification strings)

    It splits the dataset into X and y. The target column 'CDR' is transformed into a binary class, giving the value of 0 to Non Demented and 1 to Demented (some level).'''
        X=data.drop(columns=['CDR', 'MR Delay', 'Subject ID', 'MRI ID', 'Group', 'Visit', 'Hand'])
        y=data['CDR'].apply(lambda x: 1 if x>0 else 0)
        return X, y

    def __init__(self, X, y):
        self.pipeline = None
        self.X = X
        self.y = y

    def set_pipeline(self):
        '''We create a pipeline with all the transformations that will be applied to the data set: Impute, scale and encode.'''
        
        pipe1 = make_pipeline(SimpleImputer(strategy="median"), RobustScaler())

        preproc = ColumnTransformer([
                            ('encoder', OneHotEncoder(drop = "if_binary"), ["M/F"]),
                            ('imp_scaler', pipe1, ['MMSE']),
                            ('imputer', SimpleImputer(strategy="median"), ['SES']),
                            ('s_scaler', StandardScaler(), ['Age']),
                            ('m_scaler', MinMaxScaler(), ['EDUC']),
                            ('r_scaler', RobustScaler(), ['eTIV'])],
                            remainder='passthrough')

        self.pipeline = Pipeline([
            ('preproc', preproc),
            ("classifier", SVC(kernel="rbf", C= 10, gamma=1))])
            #("classifier", KNeighborsClassifier(n_neighbors= 1))])

        def run(self):
            """set and train the pipeline"""
            self.set_pipeline()
            self.pipeline.fit(self.X, self.y)

        def evaluate(self, X_test, y_test):
            """evaluates the pipeline on df_test and return the RMSE"""
            y_pred = self.pipeline.predict(X_test)
            rmse = compute_rmse(y_pred, y_test)
            return round(rmse, 2)





    '''We get name of columns and rename them as the were before'''

    oasis2_scaled=pd.DataFrame(preproc.fit_transform(X,y), columns = preproc.get_feature_names_out())
    oasis2_scaled = oasis2_scaled.rename(columns={"s_scaler__Age": "Age",
                                "m_scaler__EDUC": "Educ",
                                "r_scaler__eTIV": "eTIV",
                                "r_scaler__MMSE": "MMSE",
                                "remainder__M/F": "M/F",
                                "remainder__SES": "SES",
                                "remainder__nWBV": "nWBV",
                                "remainder__ASF": "ASF"})

    oasis2_scaled = oasis2_scaled[["M/F", "Age", "Educ", "SES", "MMSE", "eTIV", "nWBV", "ASF"]]



joblib.dump(pipeline, 'model.joblib')