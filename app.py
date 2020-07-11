import os
import string

from datetime import datetime  # Todo oluşturulma tarihlerini sakla
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


__author__ = "Nazımcan İslam"


dir_path: str = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.secret_key = 'admin'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + dir_path.replace("\\", "/") + "/todo.db"

db = SQLAlchemy(app)


class Todo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    complete = db.Column(db.Boolean)
    date = db.Column(db.DateTime, nullable=False)
    finished_date = db.Column(db.DateTime, nullable=True)


@app.route("/")
def index():

    todos = Todo.query.all()

    return render_template("index.html", todos=todos)


@app.route("/add", methods=["GET", "POST"])
def add_todo():

    if request.method == "POST":

        title = string.capwords(request.form.get("todo_name").capitalize())
        
        content = request.form.get("todo_content")
        content = content[0].upper() + content[1:]

        now = datetime.now()

        new_todo = Todo(title=title, content=content, complete=False, date=now, finished_date=None)

        db.session.add(new_todo)
        db.session.commit()

        return redirect(url_for("index"))

    else:
        return redirect(url_for("index"))


@app.route("/complete/<string:id>")
def complete_todo(id):

    todo = Todo.query.filter_by(id=id).first()

    if todo == None:
        return redirect(url_for("index"))

    else:
        if todo.complete == False:
            todo.complete = True
            todo.finished_date = datetime.now()
        else:
            todo.complete = False
            todo.finished_date = None

        db.session.commit()
        return redirect(url_for("index"))


@app.route("/delete/<string:id>")
def delete_todo(id):

    todo = Todo.query.filter_by(id=id).first()

    if todo == None:
        return redirect(url_for("index"))

    else:
        db.session.delete(todo)
        db.session.commit()

        return redirect(url_for("index"))


@app.route("/delete/all")
def delete_all_todos():

    todos = Todo.query.all()

    if todos == []:
        return redirect(url_for("index"))

    return render_template("delete_all_todos.html", todos=todos)


@app.route("/delete/all/sure")
def delete_all_todos_sure():

    todos = Todo.query.all()

    for x in range(len(todos) - 1, -1, -1):
        db.session.delete(todos[x])

    db.session.commit()

    return redirect(url_for("index"))


@app.route("/detail/<string:id>")
def detail_todo(id):

    todo = Todo.query.filter_by(id=id).first()

    if todo == None:
        return redirect(url_for("index"))
    else:
        return render_template("detail.html", todo=todo)


@app.route("/edit/<string:id>")
def edit_todo(id):

    todo = Todo.query.filter_by(id=id).first()

    if todo == None:
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo)


@app.route("/change/<string:id>", methods=["GET", "POST"])
def change_todo(id):

    todo = Todo.query.filter_by(id=id).first()

    if todo == None:
        return redirect(url_for("index"))

    else:
        new_title = request.form.get("new_todo_name").capitalize()
        new_content = request.form.get("new_todo_content")
        new_content = new_content[0].upper() + new_content[1:]
        keep_current_date = request.form.get("keep_date")

        todo.title = new_title
        todo.content = new_content

        if keep_current_date != True:
            todo.date = datetime.now()

        db.session.commit()

        return redirect(url_for("index"))



@app.errorhandler(404)
def todo_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
