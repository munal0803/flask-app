from flask import Flask, render_template

app = Flask(__name__)


JOBS = [
  {"name":"Data Scientist", "location":"San Francisco", "salary":"$100,000"},
   {"name":"Data Scientist", "location":"San Francisco", "salary":"$100,000"},
   {"name":"Data Scientist", "location":"San Francisco", "salary":"$100,000"}
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")
