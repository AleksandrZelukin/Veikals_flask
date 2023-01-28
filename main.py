from flask import Flask

app = Flask(__name__)


app.route('/')
def index():
    return "Sveiki"


if __name__ =="__maim__":
    app.run()