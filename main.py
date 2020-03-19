from flask import Flask
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)





@app.route('/')
def index():
    f=open("index.html","r")
    tmp=f.read()
    f.close()
    return tmp


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {"pdf","txt"}

@app.route('/print1', methods=['GET', 'POST'])
def upload1_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(".", filename))
            os.system("lp "+filename)
            os.remove(filename)
    return "<script>alert('完成');window.location='/'</script>"


@app.route('/print2', methods=['GET', 'POST'])
def upload2_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(".", filename))
            os.system("lp -o sides=two-sided-long-edge "+filename)
            os.remove(filename)
    return "<script>alert('完成');window.location='/'</script>"


@app.route('/print3', methods=['GET', 'POST'])
def upload3_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(".", filename))
            os.system("lp -o sides=two-sided-short-edge "+filename)
            os.remove(filename)
    return "<script>alert('完成');window.location='/'</script>"
