from flask import Flask,render_template,url_for,redirect,request,flash
from flask_sqlalchemy import SQLAlchemy
import os,uuid


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'url_shortner.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#for production
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Urls(db.Model):
    id_ = db.Column('id_',db.Integer,primary_key=True)
    long = db.Column('long',db.String())
    short = db.Column('short',db.String())

    def __init__(self,long,short):
        self.long = long
        self.short = short



@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == "POST":
        url_received = request.form["url"]
        found_url = Urls.query.filter_by(long=url_received).first()

        if found_url:
            flash('Url already exist...')
            return redirect(url_for("home"))
        else:
            short = str(uuid.uuid4().hex).replace('-','')[:10]
            inst = Urls(long=url_received,short=short)
            db.session.add(inst)
            db.session.commit()
            flash('url shorted successfully...')
            return render_template("index.html",url=f'http://localhost:5000/{short}')
    else:
        return render_template('index.html')

@app.route('/<code>',methods=['GET'])
def url_node(code):
    if request.method == "GET":
        long = Urls.query.filter_by(short=code).first()
        if long:
            return redirect(long.long)
        else:
            flash('this url does not exist...')
            return redirect(url_for('home'))
    flash('post request does not exist....')
    return redirect(url_for('home'))

@app.route('/list',methods=['GET'])
def list_ur():
    list = Urls.query.all()
    return render_template('all.html',list=list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)