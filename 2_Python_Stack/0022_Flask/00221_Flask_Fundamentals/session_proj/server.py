from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

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
    
    session['name'] = request.form["username"]
    session['usermail'] = request.form["email"] 

    return redirect("/show")

@app.route("/show")
def show():
    #print("Showing the User Info From the Form")
    #print(request.form)
    #return render_template('info.html', 
    #name_on_template=session['name'], 
    #email_on_template=session['usermail'])
    return render_template("info.html")

if __name__ == "__main__":
    app.run(debug=True)