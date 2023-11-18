import datetime as dt
import os
import pandas as pd


def read_csv_file():
    data_set = pd.read_csv('loan_payments.csv')
    return data_set

read_csv_file()