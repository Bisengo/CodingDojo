from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("dojo_survey_index.html")

@app.route("/process", methods=["POST"])
def process_info():
    return render_template("dojo_survey_result.html", name=request.form['username'], location=request.form['location'], language=request.form['language'], comment=request.form['comment'])

if __name__ == "__main__":
    app.run(debug=True)