#!/usr/bin/python
#coding:utf-8
from flask import Flask,url_for,request
app = Flask(__name__)
@app.route('/')
def index():
    return "Index page."
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/number/<int:num>/')
def number(num):
	return "The number is %s." % num


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/opt/uploaded_file.txt')



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
