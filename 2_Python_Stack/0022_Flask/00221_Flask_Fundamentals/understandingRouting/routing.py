"""
Assignment: Understanding Routing
Objectives:
Practice building a server with Flask from scratch
Get comfortable with routes and passing information to the routes

Create a server file that generates the specified responses for the following url requests:

localhost:5000/ - have it say "Hello World!"
localhost:5000/dojo - have it say "Dojo!"

Create one url pattern and function that can handle the following examples:
    localhost:5000/say/flask - have it say "Hi Flask!"
    localhost:5000/say/michael - have it say "Hi Michael!"
    localhost:5000/say/john - have it say "Hi John!"

Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
    localhost:5000/repeat/35/hello - have it say "hello" 35 times
    localhost:5000/repeat/80/bye - have it say "bye" 80 times
    localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hellow World!"

@app.route('/dojo')
def dojo():
    return "dojo"

@app.route('/say/<name>')
def say(name):
    return f"Hi {name}"

@app.route('/repeat/<repeat_number>/<repeat_str>')
def repstr(repeat_number,repeat_str):
    newstr = ""
    for i in range(int(repeat_number)):
        newstr += repeat_str +" "
    return newstr

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)