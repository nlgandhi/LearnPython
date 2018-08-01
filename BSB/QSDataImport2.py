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
<<<<<<< HEAD
        data_file_path = 'C:/Training/BSB/indname.csv'
=======
        #data_file_path = 'C:/Projects1/QuantValuationData/Adamodar_NYU/2018/CompanyLookup/indname.csv'
        #C:\Projects1\QuantValuationData\Adamodar_NYU\2018\CompanyLookup
>>>>>>> 186fdc9921cef9a263e5946646f378819841e593

        #print(data_file_path)
        #print(os.path.realpath(data_file_path))
        #print(os.path.abspath(data_file_path))
        #print(os.path.normpath(data_file_path))

<<<<<<< HEAD
        colnames = ['Industry Group','Company Name','Exchange:Ticker','Country,Broad Group','Sub Group']
        data = pd.read_csv("C:/Training/BSB/indname.csv", usecols=colnames) #index='PassengerId'  encoding="utf-8"
        #C:\Training\BSB
=======
        colnames = ['Industry Group','Company Name','Exchange:Ticker','Country','Broad Group','Sub Group']
        data = pd.read_csv('C:/Projects1/QuantValuationData/Adamodar_NYU/2018/CompanyLookup/indname.csv', usecols=colnames,  encoding='ISO-8859-1') #index='PassengerId' 
        data['Year'] = '2017'  
        data['Ticker'] = ''
        data['Exchange'] = '' 
>>>>>>> 186fdc9921cef9a263e5946646f378819841e593
        data.info()

        #data = data.fillna(-99)     
        #print(data.shape)

        cnxn = pyodbc.connect(
                    r'Driver={SQL Server Native Client 11.0};'
                    r'SERVER=f6iq6q5hoj.database.windows.net;'
                    r'DATABASE=QuantValue;'
                    r'UID=@f6iq6q5hoj;'
                    r'PWDbuysell1!'
                )

        #logging.warning("before_request")
        cursor = cnxn.cursor()    
        data = data.fillna(0)     

        for index, row in data.iterrows():
            try:
                x,y = row['Exchange:Ticker'].split(':')            
                data['Ticker'] = y
                data['Exchange'] = x 
                        
                params = (row['Year'],row['Ticker'],row['Exchange'],row['Industry Group'],
                        row['Company Name'],row['Exchange:Ticker'],row['Country'],row['Broad Group'],row['Sub Group'])
                cursor.execute('{CALL [NYUCompanyLookup_Add](?,?,?,?,?,?,?,?,?)}', params)
                cursor.commit()            
            except:
                pass

        cnxn.close()
        cursor.close()


    except:
         #print("Oops!",sys.exc_info()[0],"occured.")
         pass
    #finally:
    #    print('Done')


ReadNYUCompanyLookup()



