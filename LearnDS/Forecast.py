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

def ReadForecastTrainingCSVData():
    try:        
        data = pd.read_csv('C:/Projects/_UBC MDS Project/Initiative3/training_set_forecasting.csv')     #,index_col = 'Industry Name'
        #print(data.head())
        #print(data.describe())
        print(data.count())
        #print(data.column)
        #print(data.shape)

        #print(data.groupby('type').median())
        #data[data.list_price.notnull()].boxplot('list_price','sold_price')
        #plt.show()
        # Use IsNull function to find missing values
        #median_price = data.loc[(data.type == 'single_family') , 'sold_price'].median()
        #print(median_price)
        #data.sqft.plot(kind='hist', title='Histogram for Sq. Ft', color='c', bins=10)
        #data.plot.scatter(x='list_price', y='lot_size', color='c', title='scatter plot')
        #plt.show()
        
        
    except:
         print("Oops!",sys.exc_info()[0],"occured.")
    finally:
        print('Done')


ReadForecastTrainingCSVData()