from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def countVisit():
    if "visits" not in session:
        # print("key 'visits' does not exist")
        session['visits'] = 0
    session['visits'] += 1
    return render_template('index.html')

@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/increment', methods=['POST'])
def addTwoVisits():
    session['visits'] += 1
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['visits'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)