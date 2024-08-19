# Ctrl + ] = comenta all selected:

from ast import Expression
from xml.dom.pulldom import ErrorHandler
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key="claveS3creta"

@app.route('/usuario/')
def index():
  return render_template('usuario/index.html') 


@app.route('/')
def inicio():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000, host="0.0.0.0")
