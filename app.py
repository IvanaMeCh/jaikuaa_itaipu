from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

# Clase Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animal.db'
db = SQLAlchemy(app)
app.app_context().push()

# Clase Animal


class Animal(db.Model):
    # creamos las columnas para la base de datos
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    nombre_cientifico = db.Column(db.String(200))
    habitat = db.Column(db.String(200))
    dato_curioso = db.Column(db.String(200))
    descripcion = db.Column(db.String(200))
    audio_video = db.Column(db.String(200))
    url_imagen = db.Column(db.String(200))

# index para ingresar datos a la base de datos


@app.route('/crear-animal', methods=['POST'])
def crear():
    animal = Animal(nombre=request.form['nombre'], 
                    nombre_cientifico=request.form['nombre_cientifico'],   
                    habitat=request.form['habitat'],
                    dato_curioso=request.form['dato_curioso'], 
                    descripcion=request.form['descripcion'], 
                    audio_video=request.form['audio_video']),
    db.session.add(animal)
    db.session.commit()
    return render_template('agregar.html')

# index para visualizar el animal que el cliente desee


@app.route('/animal/<id>')
def animal(id):
    id = int(id)
    ver = Animal.query.all()
    animal = ver[id-1]
    return render_template('/view-animal.html', animal=animal)


@app.route('/')
def prueba():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
