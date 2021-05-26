from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users", methods=["POST"])
def create_users():
    print("Got Post Info")
    print("*"*50)
    print(request.form)
    name_submitted = request.form["username"]
    print(f"name submitted: {name_submitted}")
    email_submitted = request.form["email"]
    print(f"email submitted: {email_submitted}")
    #return render_template("info.html", name=name_submitted, email=email_submitted)
    return redirect("/show")

@app.route("/show")
def show():
    print("Showing the User Info From the Form")
    print(request.form)
    #return render_template("info.html", name=request.form['username']#, email=request.form['email'])
    #werkzeug.exceptions.BadRequestKeyError: 400 Bad Request: The #browser (or proxy) sent a request that this server could not #understand. KeyError: 'username'
    return render_template("info.html")
if __name__ == "__main__":
    app.run(debug=True)