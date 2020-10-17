from flask import *
from functools import wraps
import sqlite3
import time
import pandas as pd
from flask import session



DATABASE = 'dataweb.db'

app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.config.from_object(__name__)

def connect_db():
    con = sqlite3.connect('dataweb.db')
    cursor = con.cursor()
    print('La base funcionò bien')

def run_query(query='',parameters=()):
    conn = sqlite3.connect('dataweb.db')
    cursor = conn.cursor()                 # Crear un cursor
    cursor.execute(query, parameters)                  # Ejecutar una consulta
    if query.upper().startswith('SELECT'):
       data= cursor.fetchall()               # Traer los resultados de un select
       
    else:
        conn.commit()                          # Hacer efectiva la escritura de datos
        data = None
         
    #cursor.close()                         # Cerrar el cursor
    #conn.close()                           # Cerrar la conexión
    #conn.close()                           # Cerrar la conexión
    
    return data





@app.route('/')
def index():

    #query = 'SELECT * FROM datosclientes'
    #curs  = run_query(query)
    #return render_template('index_desa.html', contacts = curs)
     return render_template('layout1.html')
     

@app.route('/Login')
def crear():
    return render_template('crear.html')

@app.route('/crear_datos', methods = ['POST'])
def crear_datos():
      
    if request.method == 'POST':

        fullname = request.form['fullname']
        email = request.form['email']

        query1 = "SELECT * FROM datosclientes WHERE fullname ='%s' and email ='%s'" % (fullname,email)
        result1 = run_query(query1)
        #print(result1)
        
        if result1:
            result2 = list(result1[0])
        #print(result2[0])  
        
        if result1:
            #flash ('Existe El Contacto:'+ result2[0])
            session['username'] = result2[0]
            session['rol'] = result2[2]

            #return 'Nombre Usuario: ' + session['username'] + '---'+session['rol']
            return render_template('layout2.html')
        else:
            return 'No existe el contacto, crear una cuenta de usuario'

            
if __name__ == '__main__':
    app.run(port = 3000, debug=True)





#connect_db()
#index()
#run_query()