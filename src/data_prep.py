import pandas as pd
import os
import numpy as np

train_data = pd.read_csv("./data/raw/train_data.csv")
test_data = pd.read_csv("./data/raw/test_data.csv")

def fill_missing_with_median(df):
    for column in df.columns:
        median_value = df[column].median()
        df[column] = df[column].fillna(median_value)
    return df

train_processed_data = fill_missing_with_median(train_data)
test_processed_data = fill_missing_with_median(test_data)

data_path = os.path.join("data", "processed")
os.makedirs(data_path, exist_ok=True)

train_processed_data.to_csv(os.path.join(data_path, "train_processed_data.csv"), index=False)
test_processed_data.to_csv(os.path.join(data_path, "test_processed_data.csv"), index=False)