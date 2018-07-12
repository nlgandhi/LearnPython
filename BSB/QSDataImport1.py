import sys
import pandas as pd
from pandas import Series
import numpy as np
import pyodbc 
import logging
# import matplotlib.pyplot as plt


def ReadFile(filename):

    myfile = open('C:/Nitin/Data/FundamentalGrowthGlobal.csv', mode='r', encoding='utf-8')
    
    #mytxt = myfile.read()
    for line in myfile:
        print(line)
    myfile.close()


def ReadGrowthFile():
    # try:

    colnames = ['Industry Name','Number of Firms','ROE','Retention Ratio','Fundamental Growth ']
    # data = pd.read_csv('C:/Projects5/Pythion/TestProj1/Data/FundamentalGrowthEmrg.csv', usecols=colnames)     #,index_col = 'Industry Name'
    data = pd.read_csv('C:/Projects5/Pythion/TestProj1/Data/GrowthFundamental/Global/fundgrGlobal13.csv', usecols=colnames)     #,index_col = 'Industry Name'

    data['Country'] = 'GLOBAL'
    data['Year'] = '2013'  
    data = data.fillna(-99)     

    #print(data.shape)

    cnxn = pyodbc.connect(
                r'Driver={SQL Server Native Client 11.0};'
                r'SERVER=f6iq6q5hoj.database.windows.net;'
                r'DATABASE=QuantValue;'
                r'UID=@f6iq6q5hoj;'
                r'PWD=!'
            )

    #logging.warning("before_request")
    cursor = cnxn.cursor()    

    for index, row in data.iterrows():
        if ( len(str(row['ROE'])) > 0): 
            row['ROE'] = str(row['ROE']).replace("%", "")
            row['ROE'] = str(row['ROE']).replace("NA", "")
        if ( len(str(row['Retention Ratio'])) > 0):
            row['Retention Ratio'] = str(row['Retention Ratio']).replace("%", "")     
            row['Retention Ratio'] = str(row['Retention Ratio']).replace("NA", "")     
        if ( len(str(row['Fundamental Growth '])) > 0):
            row['Fundamental Growth '] = str(row['Fundamental Growth ']).replace("%", "")
            row['Fundamental Growth '] = str(row['Fundamental Growth ']).replace("NA", "")

        params = (row['Country'],row['Year'],row['Industry Name'],row['Number of Firms'],
                row['ROE'],row['Retention Ratio'],row['Fundamental Growth '])
        cursor.execute('{CALL [NYUDataGrowth_Add](?,?,?,?,?,?,?)}', params)
        cursor.commit()            

    cnxn.close()
    cursor.close()

    # except:
    #     print("Error: ") #+ e.message

    # finally:
    #     print("Finally is called directly after executing the try statement whether an exception is thrown or not.")
    #     cnxn.close()
    #     cursor.close()


def ReadYHDailyData():
    try:
        colnames = ['Date','Open','High','Low','Close','Adj Close','Volume']    						
        data = pd.read_csv('C:/Projects5/Pythion/TestProj1/Data/Yahoo/Daily/MSFT.csv', usecols=colnames)     #,index_col = 'Industry Name'  
        data = data.fillna(-99)     

        cnxn = pyodbc.connect(
                    r'Driver={SQL Server Native Client 11.0};'
                    r'SERVER=f6iq6q5hoj.database.windows.net;'
                    r'DATABASE=QuantValue;'
                    r'UID=@f6iq6q5hoj;'
                    r'PWD=!'
                )
        cursor = cnxn.cursor()    

        for index, row in data.iterrows():           
            #params = (row['Country'],row['Year'],row['Industry Name'],row['Number of Firms'],
            #        row['ROE'],row['Retention Ratio'],row['Fundamental Growth '])
            #cursor.execute('{CALL [NYUDataGrowth_Add](?,?,?,?,?,?,?)}', params)
            #cursor.commit()            
            print(row['Open'])

        #cnxn.close()
        #cursor.close()
    
    except:
        print("Error: ")

    finally:
        print("Done.")
        #cnxn.close()
        #cursor.close()


# ReadGrowthFile()
ReadYHDailyData()

# main("Test")

#if __name__ == "__main__":
#    main(sys.argv[1])

