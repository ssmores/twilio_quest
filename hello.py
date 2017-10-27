"""Hello World example, using Flask."""


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Simple route that returns 'Hello World'."""

    return 'Hello World! This should work?'


if __name__ == '__main__':

    #host is updated to run from within Vagrant
    app.run(debug=True, host='0.0.0.0')