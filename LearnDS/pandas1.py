import pandas as pd
import random
import numpy as np

def Test2():
    try:
        cnxn = pyodbc.connect(
                r'Driver={SQL Server Native Client 11.0};'
                r'SERVER=f6iq6q5hoj.database.windows.net;'
                r'DATABASE=QuantValue;'
                r'UID=connectsoft@f6iq6q5hoj;'
                r'PWD=!'
            )


        logging.warning("before_request")
        cursor = cnxn.cursor()
        cursor.execute("exec [dbo].[QuantScreenRouter] 'LONG_AO','Toronto'")
        results = cursor.fetchall()
        #entries = [dict(title=row['Symbol'], text=row[1]) for row in results]

        #for row in results:
        #    print(row.Symbol)

        cnxn.close()
        cursor.close()
        return results


    except ValueError:
        pass
    finally():
        print('Done')


    # Test the following
    # df.head()
    # df.tail()
    # df[['Name','Age']]
    # df.loc[5:10,['Name','Age']]
    # df.describe()
    # df.Attribute.mean()
    # df.Attribute.median()
    # For percentile use the quantile function available in Pandas
    # df.Attribute.quantile(.25)
    # df.Attribute.quantile(.50)
    # df.Attribute.std()
    #Create Box Plot
    #df.Fare.plot(kind='box')
    #df.sex.value_counts()
    #df.Attribute.value_counts().plot(kind='bar')
    #df.Attribute.plot(kind='hist', tittle='histogram for Age', color='c')


# yield is a keyword that is used like return, except the function will return a generator.
def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

def Test2():
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