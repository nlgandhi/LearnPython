from flask import Flask, jsonify, request
from pprint import pprint as pp
=======
import logging
>>>>>>> 63b2203841ef3439352fdf283c8ca2e21ddb2e83

# Understanding how to develop API's in Python. 
#Jasonify -  Flask offers the convenient jsonify() function, which returns a JSON object from Python variables:

app = Flask(__name__)

# My first API in Python
incomes = [
  { 'description': 'salary', 'amount': 5000 }
]

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


@app.route('/incomes')
def get_incomes():
  return jsonify(incomes)

# @app.route('/')
# def json_hello():
#    return jsonify({x:x*x for x in range(5)}), 200


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1><p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204

# Sample Call - http://127.0.0.1:5000/api/v1/resources/books?id=1

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
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)



@app.route('/LongAO')
def QuantScreenRouter():

    try:

      logging.warning("before_request")

      cnxn = pyodbc.connect(
              r'Driver={SQL Server Native Client 11.0};'
              r'SERVER=f6iq6q5hoj.database.windows.net;'
              r'DATABASE=QuantValue;'
              r'UID=connectsoft@f6iq6q5hoj;'
              r'PWD=!'
          )

      cursor = cnxn.cursor()
      cursor.execute("exec [dbo].[QuantScreenRouter] 'LONG_AO','Toronto'")
      logging.info("has data")	
      results = cursor.fetchall()
      entries = [dict(title=row['title'], text=row[1]) for row in results]

      #for row in cursor:
      #    print(row.Symbol)

      cnxn.close(cursor)
      cursor.close()

      return entries

    except ValueError:
        pass


if __name__ == '__main__':
    app.run(debug=True)
    

