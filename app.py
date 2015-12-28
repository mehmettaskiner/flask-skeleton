from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "hello devops, this is your home."


if __name__ == "__main__":
  app.run()