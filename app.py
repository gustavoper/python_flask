from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello world</h1>"


@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)


@app.route("/browser")
def browser():
    user_agent = request.headers.get('User-Agent')
    return "<p>Your browser is {}".format(user_agent)

@app.route("/createcookie")
def createcookie():
    response = make_response("I'm creating some cookies for you")
    response.set_cookie('cookie','asdff')
    return response


app.add_url_rule("/","index", index)


if __name__ == '__main__':
    app.run()