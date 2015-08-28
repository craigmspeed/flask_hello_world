# hello_world.py
from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        
        <img src="http://placekitten.com.s3.amazonaws.com/homepage-samples/408/287.jpg">
    """
    return html.format(name.title())
    
@app.route("/hello/jedi/<first>/<last>")
def hello_jedi(first,last):
    html="""
    <h1>
        Hello Jedi {}!
    </h1>
    """
    return html.format(last[:3]+first[:2])

    
if __name__=="__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))