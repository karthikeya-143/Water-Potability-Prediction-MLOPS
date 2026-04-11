import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import os
import pickle
import yaml

n_estimators = yaml.safe_load(open("params.yaml"))["model_building"]["n_estimators"]

train_data = pd.read_csv("./data/processed/train_processed_data.csv")

# X_train=train_data.iloc[:,0:-1].values
# y_train=train_data.iloc[:,-1].values

X_train = train_data.drop("Potability", axis=1)
y_train = train_data["Potability"]

clf=RandomForestClassifier(n_estimators=n_estimators)
clf.fit(X_train,y_train)

pickle.dump(clf,open("model.pkl","wb"))
