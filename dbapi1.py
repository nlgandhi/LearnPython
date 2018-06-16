import flask
from flask import request, jsonify
import pyodbc 
import logging


app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Quant Value API</h1>
<p>Reference API for Quant Value.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    #conn = sqlite3.connect('books.db')
    #conn.row_factory = dict_factory
    #cur = conn.cursor()
    #all_books = cur.execute('SELECT * FROM books;').fetchall()

    cnxn = pyodbc.connect(
                r'Driver={SQL Server Native Client 11.0};'
                r'SERVER=f6iq6q5hoj.database.windows.net;'
                r'DATABASE=QuantValue;'
                r'UID=connectsoft@f6iq6q5hoj;'
                r'PWD=buysell1!'
            )

    logging.warning("before_request")
    cursor = cnxn.cursor()
    cursor.execute("exec [dbo].[QuantScreenRouter] 'LONG_AO','Toronto'")
    results = cursor.fetchall()

    return jsonify(results)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    #query = query[:-4] + ';'
    #conn = sqlite3.connect('books.db')
    #conn.row_factory = dict_factory
    #cur = conn.cursor()
    #results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()