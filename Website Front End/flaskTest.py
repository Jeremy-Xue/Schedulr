from flask import Flask, render_template, request
import Schedulr as helper
app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to Sche-toolR!'

@app.route("/main", methods=["POST","GET"])
def main():
    if (request.method =="POST"):
        classList= request.args.get("lname")
        intendedMajor= request.args.get("fname")
        plannedClasses = request.args.get("planned")
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)

