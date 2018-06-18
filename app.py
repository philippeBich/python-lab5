from flask import Flask, render_template, request, redirect, url_for, session
import database
app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template("list.html", tasks=database.getTasks())

@app.route('/task', methods=['POST','GET'])
def task():
    newtask = request.form.get['taskname']
    database.addTask(newtask)
    return render_template("insert.html", description=newtask, urgency=database.getUrgency(newtask))

@app.route('/delete', methods=['POST','GET'])
def delete():

    id=request.form.get('taskname')
    if id != None:
        database.deleteTask(id)
    return render_template("delete.html")


if __name__ == '__main__':
    app.run()
