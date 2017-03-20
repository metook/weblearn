#!/usr/bin/env python
#coding:utf-8
import os
from flask import Flask,request,render_template,redirect,url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)
UPLOAD_PATH = '/opt'
@app.route('/upload',methods=['GET','POST'])
def upload():
	if request.method == 'GET':
		return render_template('upload.html')
	elif request.method == 'POST':
		f = request.files['file']
		fname = secure_filename(f.filename)
		f.save(os.path.join(UPLOAD_PATH,fname))
		return 'upload success!!!'
@app.route('/')
def index():
	return redirect(url_for('upload'),302)
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=9000,debug=True)

