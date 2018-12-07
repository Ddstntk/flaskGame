from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Siema siema o tej porze każdy wypić może jakby nie było jest bardzo miło'


if __name__ == '__main__':
    app.run()
