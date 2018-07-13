import pandas as pd
import random
import numpy as np
import pyodbc 
import sys
import matplotlib.pyplot as plt

def TestPlot():
    x = np.linspace(0, 20, 100)
    plt.plot(x, np.sin(x))
    #plt.show(block=False)
    plt.show()
    input('press <ENTER> to continue')    

def TestPandasWithCSV():
    try:
        data = pd.read_csv('C:/Projects/_UBC MDS Project/Initiative3/Initiative3_TrainingSet.CSV')     #,index_col = 'Industry Name'
        print(data.groupby('style').median())
        #print(data.head())
        #data.sqft.plot(kind='hist', title='Histogram for Sq. Ft', color='c', bins=10)
        #data.plot.scatter(x='list_price', y='lot_size', color='c', title='scatter plot')
        #plt.show()
        #print(data.head())
        #print(data.describe())
        
    except:
         print("Oops!",sys.exc_info()[0],"occured.")
    finally:
        print('Done')



# Test Pandas Functionality
def TestPandasWithDB():
    try:
        cnxn = pyodbc.connect(
                r'Driver={SQL Server Native Client 11.0};'
                r'SERVER=f6iq6q5hoj.database.windows.net;'
                r'DATABASE=QuantValue;'
                r'UID=@f6iq6q5hoj;'
                r'PWD=!'
            )
            
        #logging.warning("before_request")
        #cursor = cnxn.cursor()
        sql = "select * from [dbo].[TickerInfo] where [Exchange] = 'NYSE'"
        #cursor.execute("select * from [dbo].[TickerInfo] where [Exchange] = 'NYSE'")
        #results = cursor.fetchall()
        data = pd.read_sql(sql,cnxn)
        #print(data.head())
        #print(data.tail())
        #print(data.info())
        #print(data.BETA.quantile(.25))
        #print(data.BETA.quantile(.50))
        #print(data.BETA.std())
        #data.BETA.plot(kind='box')
        #print(data.AO_RECOSUMMARY.value_counts())
        #print(data.AO_RECOSUMMARY.plot(kind='hist', tittle='histogram for Age', color='c'))
        #print(data.describe())

        #print(data)
        cnxn.close()

    except:
         print("Oops!",sys.exc_info()[0],"occured.")
    finally:
        print('Done')


# yield is a keyword that is used like return, except the function will return a generator.
def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

def PandasWithDict():
    dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98] }
    brics = pd.DataFrame(dict)

    # Pandas can be loaded directly from csv files
    # cars = pd.read_csv('cars.csv')
    # cars = pd.read_csv('cars.csv', index_col = 0)

    #Add new index values
    brics.index = ["BR", "RU", "IN", "CH", "SA"]

    # Is label-based, which means that you have to specify rows and columns based on their row and column label
    print(brics.loc[['IN', 'CH']])
    #The key difference between an array and a list is, arrays are designed to handle vectorized operations while a python list is not.
    list1 = [0,1,2,3,4]
    arr1d = np.array(list1)
    # Add 2 to each element of arr1d
    arr1d + 2


#TestPandasWithDB()
#PandasWithDict()
#TestPlot()
TestPandasWithCSV()