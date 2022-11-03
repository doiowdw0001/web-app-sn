from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as data
from flask_login import UserMixin


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata_register.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Register(db.Model, UserMixin):
    id = data.Column(data.Integer,primary_key=True) 
    name_lastname = data.Column(data.String(100),nullable=False)
    password = data.Column(data.Integer,nullable=False) 
    tel = data.Column(data.Integer,nullable=False) 
    group = data.Column(data.String(100),nullable=False) 
    gender = data.Column(data.String(50),nullable=False) 
    major = data.Column(data.String(100),nullable=False) 
    email = data.Column(data.String(100),nullable=False) 

with app.app_context():
 db.create_all()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/datasave',methods=['POST'])
def datasave():
    name_lastname = request.form["name_lastname"]
    password = request.form["password"]
    tel = request.form["tel"]
    group = request.form["group"]
    gender = request.form["gender"]
    major = request.form["major"]
    email = request.form["email"]
    register = Register(name_lastname = name_lastname,password = password,tel = tel,group = group,gender = gender,major = major,email = email)
    db.session.add(register)
    db.session.commit()
    return redirect('/register')

@app.route('/addschool')
def school():
    register = Register.query.all()
    return render_template('addschool.html',register = register)

@app.route('/showdatas')
def showdatas():
   registers = Register.query.all()
   return render_template("show.html",registers=registers)
app.run(debug=1)