# test
from flask import Flask, make_response, redirect
import os
from flask.ext.script import Manager
from os import environ

app=Flask(__name__)

manager = Manager(app)

@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response
    
@app.route('/redirect')
def index2():
    return redirect('http://www.example.com')

if __name__ == "__main__":
    manager.run()

    # app.run(host=environ['IP'],
            # port=int(environ['PORT']))