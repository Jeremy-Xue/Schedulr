from flask import Flask, render_template, request
import Schedulr as helper
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Sche-toolR!'

@app.route('/result')
def result():
    return render_template("result.html")

@app.route('/result2')
def result2():
    return render_template("result2.html")

@app.route('/main2')
def main2():

    return render_template("main2.html")

@app.route("/main", methods=["POST","GET"])
def main():
    submit= request.args.get("Subimt")
    if (submit == "Submit"):
        classList= request.args.get("lname").split()
        helper.fillClassesTaken(classList)
        possibleClassList = helper.returnPossibleClasses()
        intendedMajor= request.args.get("fname")
        plannedClasses = request.args.get("planned")
        return redirect("/result")
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)

