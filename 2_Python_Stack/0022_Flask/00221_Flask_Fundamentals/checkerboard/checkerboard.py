from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def checkerboard1():
    nrow = 8
    ncol = nrow
    return render_template("checkerboard_index.html", rows = nrow, columns=ncol, colorname1="blue", colorname2="red")

@app.route("/<number1>")
def checkerboard2(number1):
    nrow = 8
    ncol = int(number1)
    return render_template("checkerboard_index.html", rows = nrow, columns=ncol, colorname1="blue", colorname2="red")

@app.route("/<number1>/<number2>")
def checkerboard3(number1, number2):
    nrow = int(number1)
    ncol = int(number2)
    return render_template("checkerboard_index.html", rows = nrow, columns=ncol, colorname1="blue", colorname2="red")

@app.route("/<number1>/<number2>/<firstcolor>/<secondcolor>")
def checkerboard4(number1, number2, firstcolor, secondcolor):
    nrow = int(number1)
    ncol = int(number2)
    color1 = firstcolor
    color2 = secondcolor
    return render_template("checkerboard_index.html", rows = nrow, columns=ncol, colorname1=color1, colorname2=color2)
    
if __name__ == "__main__":
    app.run(debug=True)