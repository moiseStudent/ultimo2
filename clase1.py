# Aplicacion con FLask #
from flask import Flask, render_template

app = Flask(__name__)

### Filtro personalizado ###
#@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')

app.add_template_filter(today, "today")

#@app.add_template_global
def multiply(str,num):
    return str * num

#app.add_template_global(multiply,"multiply")

from datetime import datetime


@app.route('/')
@app.route('/index')
def index():

    my_friends = ["Moises","ALexander","Perez","Gutierrez"]
    name = "Moises"
    date = datetime.now()

    return render_template(
        'index.html',
        name = name,
        my_friends = my_friends,
        date = date,
        multiply = multiply
    )

@app.route('/moises/')
@app.route('/moises/<string:name>')
@app.route('/moises/<string:name>/<int:age>')

def moises(name=None,age=None):

    if name == None and age == None:
        return 'Hola mundo...'
    
    elif name != None:
        return f"Hola,{name}. Como estas hoy ?"
    
    else:
        return f"Hola{name} tu edad es {age}"
    
from markupsafe import escape


@app.route('/code/<path:code>')
def code(code):
    return f"{escape(code)}"

if __name__ == '__main__':
    app.run(debug=True)
