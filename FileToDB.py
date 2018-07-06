import sys
import pandas as pd
from pandas import Series
import numpy as np


def ReadFile(filename):

    # Open a file
    myfile = open('C:/Nitin/Data/FundamentalGrowthUS.csv', mode='r', encoding='utf-8')
    #mytxt = myfile.read()

    for line in myfile:
        print(line)
    myfile.close()

def ReadFilePandas():
    colnames = ['Industry Name','Number of Firms','ROE','Retention Ratio','Fundamental Growth ']
    data = pd.read_csv('C:/Nitin/Data/FundamentalGrowthUS.csv',index_col = 'Industry Name', usecols=colnames)     
    print(data) #names=colnames
    print(data.shape)


ReadFilePandas()

# main("Test")

#if __name__ == "__main__":
#    main(sys.argv[1])

