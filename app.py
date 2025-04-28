from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
  return "This is my Flask web app page"

if __name__ == "__main__":
  app.run(debug = True)
