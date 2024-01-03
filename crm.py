import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.sqlite3'
# create new instance from the SQLALCHEMY DB for our new db
db = SQLAlchemy(app)
app.app_context().push()

# Test DataBase

lessons = [
            {
            'Title':'if-else',
            'In':'python',
            'By':'Joseph'
            },
            {
            'Title':'For loop',
            'In':'python',
            'By':'Joseph'
            },
           {
            'Title':'While loop',
            'In':'python',
            'By':'Joseph'
            }
            ]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',lessons=lessons,title='Home')


@app.route("/about")
def about():
    return render_template('about.html',title = 'About')


# DATA BASE: 

class User(db.Model):  # Create a class to represent table in the database
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(25), nullable = False)
    lname = db.Column(db.String(25), nullable = False)
    username = db.Column(db.String(25), unique = True, nullable = False)
    email = db.Column(db.String(125), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)
    lessons = db.relationship('Lesson',backref= 'author' , lazy = True)


    def __repr__(self) -> str:
        return f"User('{self.fname}','{self.lname}','{self.username}','{self.email}')"
    
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False)
    thumbnail = db.Column(db.String(20), nullable = False, default = 'default_thumbnail.jpg')
    slug = db.Column(db.String(32), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    course_id = db.Column(db.String(60), db.ForeignKey('course.id'), nullable = False)
    def __repr__(self) -> str:
        return f"User('{self.title}, '{self.content}')"
    
class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), unique = True, nullable = False)
    descriptiom = db.Column(db.String(150), nullable = False)
    thumbnail = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    lessons = db.relationship('lesson', backref = 'course_name', lazy=True)

    def __repr__(self) -> str:
        return f"User('{self.title}')"
    

# create_db()
if __name__ =='__main__':
    app.run(debug=True)
