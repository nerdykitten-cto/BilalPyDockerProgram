from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World</h1>\n<h3>This is a page for the PyDocker Flask App</h3>"

if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0", debug=True)
