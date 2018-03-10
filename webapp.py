from flask import *
from flask import session as login_session
from sqlalchemy.exc import IntegrityError
from model import *
# from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
import locale, os

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# LOCAL
engine = create_engine('sqlite:///database.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET','POST'])
def home():
	if request.method == 'GET':
		allMessages = session.query(Messages).all()
		return render_template('index.html',allMessages=allMessages)
	else:
		message = Messages(name = request.form['name'], message= (request.form['message'] + ' b3rdi'))
		session.add(message)
		session.commit()
		return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)