from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tmppw@localhost/testdb'
app.config['SECRET_KEY'] = 'tmppw'
db = SQLAlchemy(app)
db.create_all()


# %%
@app.route('/')
def hello_world():
    print('Returning Hello World')
    return '<h1>Hello, World!</h1>'


@app.route('/about')
def introduce():
    print('Returning introduction')
    return '<p>My Name is Satoshi Suzuki</p>'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return self.username


@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        db.session.add(User(username="Flask", email="example@example.com"))
        db.session.commit()
        return 'added'
    if request.method == 'GET':
        users = User.query.all()
        return users
