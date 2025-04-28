from flask import Flask

@app.route("/")
def hello():
  return "This is my flask web app page"

if __name__ == "__main__":
  app.run(debug = True)
