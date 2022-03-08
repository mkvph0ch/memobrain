from sklearn import set_config; set_config(display='diagram')
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd
from data import get_data, clean_data
from encoders import CustomColumnTransformer

class Trainer():

    def __init__(self, X, y):
        self.pipeline = None
        self.X = X
        self.y = y

    def set_pipeline(self):
        '''We create a pipeline that will apply transformations to the data set: Scale and encode.'''

        standard_features = ['Age']
        robust_features = ['eTIV', 'MMSE']
        minmax_features = ['EDUC', 'SES']
        nothing_to_scale = ['nWBV','ASF']
        binary_cat = ['M/F']

        numerical_features = standard_features + robust_features + minmax_features + nothing_to_scale

        numerical_transformer = CustomColumnTransformer([
            ('s_scaler', StandardScaler(), standard_features),
            ('m_scaler', MinMaxScaler(), minmax_features),
            ('r_scaler', RobustScaler(), robust_features)],
            remainder='passthrough')

        pre_pipe = CustomColumnTransformer([
            ('num_transformer', numerical_transformer, numerical_features),
            ('encoder', OneHotEncoder(drop = "if_binary"), binary_cat)])
    

        self.pipeline = Pipeline([
            ('preprocessor', pre_pipe),
            ("classifier", RandomForestClassifier(n_estimators= 100, max_features= 'auto', max_depth= 8, criterion= 'gini'))])

        def run(self):
            """set and train the pipeline"""
            self.set_pipeline()
            self.pipeline.fit(self.X, self.y)

        def evaluate(self, X_test, y_test):
            """evaluates the pipeline on df_test and return the RMSE"""
            y_pred = self.pipeline.predict(X_test)
            acc = accuracy_score(y_pred, y_test)
            rec = recall_score(y_pred, y_test)
            prec = precision_score(y_pred, y_test)
            return round(acc, 3), round(rec, 3), round(prec, 3)

        def save_model(self):
            """Save the model into a .joblib format"""
            joblib.dump(self.pipeline, 'model.joblib')
            print(colored("model.joblib saved locally", "green"))


if __name__ == "__main__":
    df = get_data()
    X, y = clean_data(df)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    trainer = Trainer(X_train, y_train)
    trainer.run()
    acc, rec, prec = trainer.evaluate(X_test, y_test)
    print(f"Accuracy: {acc}, Recall: {rec}, Precision: {prec}")