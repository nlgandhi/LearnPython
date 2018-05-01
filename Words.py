import sys
import smtplib
from urllib.request import urlopen

# Test Code python words.py http://sixty-north.com/c/t.txt

def fetch_words(url):
    """
    Fetch data from a URL
    
        Args:
            url: The URL of a UTF-8 text document 

        Returns:
            A list of strings containing the words from the document.
    """
    with urlopen(url) as story:
        story_words = []  
        for line in story:        
            line_words = line.decode('utf-8').split()        
            for word in line_words:
                story_words.append(word)                
    return story_words


def print_items(items):
    """Print the data that we have fetched"""
    for item in items:
        print(item)


def main(url):    
    #words = fetch_words('http://sixty-north.com/c/t.txt')
    words = fetch_words(url)
    print_items(words)

main('http://sixty-north.com/c/t.txt')

#if __name__ == '__main__':
#    main(sys.argv[1])




