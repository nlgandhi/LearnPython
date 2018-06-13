from flask import Flask, jsonify, request
import logging

#Jasonify -  Flask offers the convenient jsonify() function, which returns a JSON object from Python variables:

app = Flask(__name__)

# My first API in Python
incomes = [
  { 'description': 'salary', 'amount': 5000 }
]


@app.route('/incomes')
def get_incomes():
  return jsonify(incomes)

@app.route('/')
def json_hello():
    return jsonify({x:x*x for x in range(5)}), 200

@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204

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
    

