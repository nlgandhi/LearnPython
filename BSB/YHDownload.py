
import requests
from requests import session
import os
from dotenv import load_dotenv, find_dotenv
import os

# pip install --upgrade setuptools
# pip install -U python-dotenv
# pip install python-dotenv


def getDailyData():
    try:        

        url = 'https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1528604489&period2=1531196489&interval=1d&events=history&crumb=UGZmg7nPKPh'
        # Setup a session
        with session() as c:
            # get request
            response = c.get(url)
            print(response.text)

    except:
        print('Error')
    finally:
        print('Done')


getDailyData()
