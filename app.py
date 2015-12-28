from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def index():
  return 'hello devops, this is your home. <br><a href="./endpoint">click me</a>'


@app.route("/endpoint")
def endpoint():
  devops = {
    'name': 'Mehmet Taskiner', 
    'github': 'http://github.com/mehmettaskiner'
  }
  return jsonify(devops)


if __name__ == "__main__":
  app.run()