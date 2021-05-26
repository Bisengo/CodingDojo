from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default_index():
    return "visit http://localhost:5000/play to start playing"

@app.route("/play")
def box_index():
    return render_template("playground_level1.html", times=3)

@app.route("/play/<number>")
def box_repeat_index(number):
    repeat = int(number)
    return render_template("playground_level2.html", times=repeat)

@app.route("/play/<number>/<newcolor>")
def box_color_index(number, newcolor):
    repeat = int(number)
    return render_template('playground_level3.html', times = repeat, color = newcolor)

if __name__ == "__main__":
    app.run(debug=True)