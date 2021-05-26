from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "hello world"

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>')
def hello3(name):
    print(name)
    return "hello, " + name

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id



if __name__ == "__main__":
    app.run(debug= True)