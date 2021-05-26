from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    # fruit bought
    strawberry_qty = request.form['strawberry']
    raspberry_qty = request.form['raspberry']
    apple_qty = request.form['apple']

    # buyer info
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    studentId = request.form['student_id']
    count = int(strawberry_qty) + int(raspberry_qty) + int(apple_qty)
    print(f"Charging { first_name } { last_name } for { count } fruit") 
    return render_template("checkout.html", firstN=firstName, lastN=lastName, studentid=studentId, qtystraw=strawberry_qty, qtyraspb=raspberry_qty, qtyapple=apple_qty)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)