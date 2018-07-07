import pandas as pd
import random
import numpy as np

#The key difference between an array and a list is, arrays are designed to handle vectorized operations while a python list is not.
list1 = [0,1,2,3,4]
arr1d = np.array(list1)
# Add 2 to each element of arr1d
arr1d + 2


# yield is a keyword that is used like return, except the function will return a generator.
def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

# for random_number in lottery():
#        print("Number is... %d!" %(random_number))


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


# print(brics)