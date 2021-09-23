from flask import Flask, render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

engine=create_engine(os.getenv('DB_URI'))
db=scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

@app.route("/")
def index():
    rutas=['buscar', 'agregar', 'mostrar']
    return render_template("index.html", rutas=rutas)

@app.route("/buscar", methods=["POST", "GET"])
def buscar():
    return ("<h1>TODO: Busqueda</h1>")

@app.route("/mostrar")
def mostrar():
    movies= db.execute("SELECT * FROM movies LIMIT 10;").fetchall()
    if not movies or not len(movies):
        return render_template("error.html", error=404, message="No encontramos nada.")
    return render_template("mostrar.html", res=movies)

@app.route("/agregar", methods=["POST", "GET"])
def agregar():
    if request.method=="POST":
        name= request.form.get("name")
        year=int(request.form.get("year"))
        desc=request.form.get("description")
        image= request.form.get("imagelink")

        if not name or not year or not desc:
            return render_template("error.html", error=400, message="Falta info")
        db.execute("INSERT INTO movies (name, year, description, image) VALUES (:name, :year, :desc, :image);", {'name':name, 'year':year, 'desc':desc, 'image':image})
        db.commit()
        return render_template("agregar.html")
    else:
        return render_template("agregar.html")