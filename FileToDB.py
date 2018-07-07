import sys
import pandas as pd
from pandas import Series
import numpy as np
import pyodbc 
import logging
# import matplotlib.pyplot as plt


def ReadFile(filename):

    # Opencls
    # a file
    # C:/Nitin/Data/FundamentalGrowthUS.csv
    # C:/Projects5/Pythion/TestProj1/Data/FundamentalGrowthUS.csv
    myfile = open('C:/Nitin/Data/FundamentalGrowthUS.csv', mode='r', encoding='utf-8')
    #mytxt = myfile.read()

    for line in myfile:
        print(line)
    myfile.close()

def ReadFilePandas():
    colnames = ['Industry Name','Number of Firms','ROE','Retention Ratio','Fundamental Growth ']
    # C:/Nitin/Data/FundamentalGrowthUS.csv
    # C:/Projects5/Pythion/TestProj1/Data/FundamentalGrowthUS.csv
    data = pd.read_csv('C:/Nitin/Data/FundamentalGrowthUS.csv', usecols=colnames)     #,index_col = 'Industry Name'
    data['Country'] = 'USA'
    print(data['Number of Firms']) 

    for index, row in data.iterrows():
        print(row['Industry Name'])
        print(row['Number of Firms'])
        print(row['ROE'])
        print(row['Retention Ratio'])
        print(row['Fundamental Growth '])

    #data['Number of Firms'].plot()

    #print(data.shape)

    #cnxn = pyodbc.connect(
    #            r'Driver={SQL Server Native Client 11.0};'
    #            r'SERVER=f6iq6q5hoj.database.windows.net;'
    #            r'DATABASE=QuantValue;'
    #            r'UID=connectsoft@f6iq6q5hoj;'
    #            r'PWD=!'
    #        )

    #logging.warning("before_request")
    #cursor = cnxn.cursor()
    #cursor.execute("exec [dbo].[QSTickerSignal] 'NYSE'")
    #cursor.execute("exec [dbo].[QSTickerSignal] 'NYSE'")

    #results = cursor.fetchall()

    #for row in results:
    #    print(row.Ticker)

    #cnxn.close()
    #cursor.close()


ReadFilePandas()

# main("Test")

#if __name__ == "__main__":
#    main(sys.argv[1])

