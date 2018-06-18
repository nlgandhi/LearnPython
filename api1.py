from flask import Flask, jsonify, request
from pprint import pprint as pp
import logging

# Understanding how to develop API's in Python. 
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
    try:


if __name__ == '__main__':
    app.run(debug=True)
    

