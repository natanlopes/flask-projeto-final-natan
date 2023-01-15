
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Secret Key'

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost/crud'
app.config['SQLALCHEMY TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# db.init_app(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    tefone = db.Column(db.String(100))


def __init__(self, nome, email, telfone):
    self.nome = nome
    self.email = email
    self.tefone = telfone


@app.route('/')
def Index():
    return render_template('index.html')


if __name__ == "__main__":

    app.run(debug=True)
