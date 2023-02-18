from flask import Flask
from flask import render_template

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "Location": "Bengaluru, India",
        "salary": "Rs. 15 0000"
    },
    {
        "id": 2,
        "title": "PHD",
        "Location": "Canberra, Aus",
        "salary": "Rs. 15 0000"
    },
    {
        "id": 3,
        "title": "Professor",
        "Location": "Adelaida, Aus",
        "salary": "$ 12 000"
    },
    {
        "id": 3,
        "title": "Professor",
        "Location": "Adelaida, Aus",
    }
]

COMPANY_NAME = "Algebra Phone Book Test"

@app.route("/")
def root_path():
    return render_template("home.html",jobs=JOBS, company_name = COMPANY_NAME)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)