import sys
import smtplib
from urllib.request import urlopen
import requests
import json

# Test Code python words.py http://sixty-north.com/c/t.txt

def fetch_words(url):
    """
    Fetch data from a URL
    
        Args:
            url: The URL of a UTF-8 text document 

        Returns:
            A list of strings containing the words from the document.
    """
 
    json_data = '{"name": "Brian", "city": "Seattle"}'
    python_obj = json.loads(json_data)
    print(python_obj["name"])


    parameters = {"lat": 40.71, "lon": -74}
    response = requests.get("http://api.open-notify.org/iss-now.json")
    #print(response.status_code)
    print(response.text)
    #data = json.load(response.text)
    #print(data)

    with urlopen(url) as story:
        story_words = []  
        for line in story:        
            line_words = line.decode('utf-8').split()        
            for word in line_words:
                story_words.append(word)                
    return story_words

# Understanding Errorrs in Python
# Exception TYpes include NameError, ValueError, SyntaxError, IndentationError, KeyError, IndexError and others
# e is the named reference to the except object
# raise simply re-raises the exception
def print_items(items):
    """Print the data that we have fetched"""
    try:
        for item in items:
            print(item)
    except (ValueError, TypeError) as e:
        pass


def main(url):    
    #words = fetch_words('http://sixty-north.com/c/t.txt')
    words = fetch_words(url)
    print_items(words)

main('http://sixty-north.com/c/t.txt')

#if __name__ == '__main__':
#    main(sys.argv[1])




