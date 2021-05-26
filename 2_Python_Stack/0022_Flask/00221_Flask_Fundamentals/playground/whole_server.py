from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def default_index():
    return "visit http://localhost:5000/play to start playing"

@app.route("/play")
def box_index():
    Color = "blue"
    return render_template('playground_whole.html', times=3, color=Color)

@app.route("/play/<number>")
def box_repeat_index(number):
    repeat = int(number)
    Color = "blue"
    return render_template('playground_whole.html', times=repeat, color=Color)

@app.route("/play/<number>/<newcolor>")
def box_color_index(number, newcolor):
    repeat = (int(number))
    return render_template('playground_whole.html', times = repeat, color = newcolor)


if __name__ == "__main__":
    app.run(debug = True)
