from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from datetime import datetime
import pyodbc
import json
import logging


app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)  # api is a collection of objects, where each object contains a specific functionality (GET, POST, etc)


# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/api/v2/resources/books/all', methods=['GET'])
def api_all2():
    
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
    #cursor.execute("select top 100 Ticker from [dbo].[TickerMaster]")

    rows = cursor.fetchall()

    rowarray_list = []
    for row in rows:
        t = (row.Symbol, row.Exchange, row.CompanyName, 
             str(row.LastPrice))
        rowarray_list.append(t)

    # CompanyName, Symbol, Exchange
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(rowarray_list)




@app.route('/', methods=['GET'])
def home():
    return '''<h1>API with Data Access Test</h1>
<p>Tech POC to get this working.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all1():
    return jsonify(books)



@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    # results = []

    cnxn = pyodbc.connect(
                r'Driver={SQL Server Native Client 11.0};'
                r'SERVER=f6iq6q5hoj.database.windows.net;'
                r'DATABASE=QuantValue;'
                r'UID=connectsoft@f6iq6q5hoj;'
                r'PWD=!'
            )

    logging.warning("before_request")
    cursor = cnxn.cursor()
    #cursor.execute("exec [dbo].[QuantScreenRouter] 'LONG_AO','Toronto'")
    cursor.execute("select top 100 Ticker from [dbo].[TickerMaster]")

    rows = cursor.fetchall()

    rowarray_list = []
    for row in rows:
        t = (row.Ticker)
        rowarray_list.append(t)

  
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(rowarray_list)




app.run()

#if __name__ == '__main__':
#    app.run(debug=True)