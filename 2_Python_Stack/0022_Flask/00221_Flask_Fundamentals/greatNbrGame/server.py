from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "akuna matata"

@app.route("/")
def home():
    randomNumber = random.randint(1, 100)
    #print(randomNumber)
    if 'rnkey' not in session:
        session['rnkey'] = randomNumber

    if 'userguess' not in session:
        session['userguess'] = False

    if "attempt" not in session:
        session['attempt'] = 0

    return render_template(
        "index.html", 
        randnum=session['rnkey'], 
        userguess=session["userguess"],
        count=session["attempt"])

@app.route("/guess", methods=['POST'])
def guess():
    print(request.form)
    guess = int(request.form["userguess"]) # typecasting to int
    session["userguess"] = guess
    session['attempt'] += 1
    return redirect("/render")

@app.route("/render")
def guessed():
    return render_template("guessed.html", randnum=session['rnkey'],userguess=session["userguess"])

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)