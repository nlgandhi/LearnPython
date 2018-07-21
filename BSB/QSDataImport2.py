import sys
import pandas as pd
from pandas import Series
import numpy as np
import pyodbc 
import logging
import os


def ReadNYUCompanyLookup():

    try:

        #raw_data_path = os.path.join(os.path.pardir,'data','QuantValue','raw')
        #data_file_path = os.path.join(raw_data_path, 'indname.csv')
        data_file_path = 'C:/Training/BSB/indname.csv'

        #print(data_file_path)
        #print(os.path.realpath(data_file_path))
        #print(os.path.abspath(data_file_path))
        #print(os.path.normpath(data_file_path))

        colnames = ['Industry Group','Company Name','Exchange:Ticker','Country,Broad Group','Sub Group']
        data = pd.read_csv("C:/Training/BSB/indname.csv", usecols=colnames) #index='PassengerId'  encoding="utf-8"
        #C:\Training\BSB
        data.info()

    except:
         print("Oops!",sys.exc_info()[0],"occured.")
    finally:
        print('Done')


ReadNYUCompanyLookup()



