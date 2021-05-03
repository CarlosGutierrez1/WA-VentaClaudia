from flask import Flask, render_template, request, redirect, flash, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ecw12345'
app.config['MYSQL_DB'] = 'wa-ventaspe'

mysql = MySQL(app)

app.secret_key = "UnaContras3nas3cr3ta"

@app.route('/')
def Rindex():
    return render_template('index.html')

@app.route('/Ingresarventa1')
def Ringresardatos():
    productosobtenidos, tamaño = ObtenerProductos()
    # tamaño = len(productosobtenidos)
    print(productosobtenidos)
    print(tamaño)
    return render_template('Ingresarventa1.html', productosobtenidos=productosobtenidos, tamaño=tamaño)

@app.route('/Mostrardatos')
def RMostrardatos():
    return render_template('Mostrardatos.html')

@app.route('/buscarproductoslive', methods=['POST','GET'])
def Buscarproductoslive():
    searchbox = request.form.get("text")
    cur = mysql.connection.cursor()
    query = "select idProducto, nombre from producto where nombre LIKE '{}%' limit 3".format(searchbox)#This is just example query , you should replace field names with yours
    cur.execute(query)
    result = cur.fetchall()
    print (result)
    return jsonify(result)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

def ObtenerProductos():
    cur = mysql.connection.cursor()
    query = ("select idProducto, nombre from producto")
    existe = cur.execute(query)
    print(existe)
    productos = ()
    cantidad =0
    if existe !=0:
        for i in range(existe):
            productos += cur.fetchone()
            cantidad +=1
        print(productos)
        return productos, cantidad;
    else:
        flash('No hay ningun producto registrado!', 'alert-danger')
        return render_template('index.html');


if __name__ == '__main__':
    app.run(debug=True)
