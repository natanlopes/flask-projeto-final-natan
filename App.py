from flask import Flask, render_template, request, redirect, url_for,flash
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
    phone = db.Column(db.String(100))


    def __init__(self, nome, email, phone):
        self.nome = nome
        self.email = email
        self.phone = phone


@app.route('/')
def Index():
    all_data = Data.query.all()
    return render_template('index.html', empregar=all_data)


@app.route('/insert', methods=["POST"])
def insert():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(nome, email, phone)
        db.session.add(my_data)
        db.session.commit()
        flash('Funcionario adcionado com sucesso')
        return redirect(url_for('Index'))


@app.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
        my_data.nome = request.form['nome']
        my_data.email = request.form['nome']
        my_data.phone = request.form['nome']

        db.session.commit()
        flash('Funcionarios atualizado com sucesso')
        return redirect(url_for('Index'))


@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash('Empregado excluido com sucesso')

    return redirect(url_for('Index'))
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)