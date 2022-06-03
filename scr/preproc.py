import os
import pandas as pd


def read_data():
    """ Read data from csv. """
    return pd.read_csv(os.path.join("data", "btcusd_datetime.csv"))


def detect_nan_values(df):
    """ Detect nan values. """
    return pd.isna(df).any()


def detect_null_values(df):
    """ Detect null values. """
    return pd.isnull(df).any()


a = read_data()
x = detect_nan_values(a)
y = detect_null_values(a)