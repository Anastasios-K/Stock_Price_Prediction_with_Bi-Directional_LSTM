import os
import pandas as pd
from typing import List
import matplotlib.pyplot as plt


from .not_necessary import add_nan_values


def read_data(url_list: List):
    """ Read data from csv. """
    return pd.read_csv(os.path.join(*url_list))


def add_nans(df: pd.DataFrame):
    return add_nan_values(df=df)


def detect_nan_values(df: pd.DataFrame):
    """ Detect nan values. """
    return pd.isna(df).any()


def detect_null_values(df: pd.DataFrame):
    """ Detect null values. """
    return pd.isnull(df).any()


# url_list = ["data", "btcusd_datetime.csv"]
#
# a = read_data(url_list=url_list)
# aa = add_nans(df=a)
#
# x = detect_nan_values(a)
# y = detect_null_values(a)
#
# xxx = pd.read_csv(os.path.join(*["data", "btcusd_datetime.csv"]))

