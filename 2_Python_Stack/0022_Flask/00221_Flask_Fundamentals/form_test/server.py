from flask import Flask, render_template, request
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
    return render_template("info.html", name=name_submitted, email=email_submitted)


if __name__ == "__main__":
    app.run(debug=True)