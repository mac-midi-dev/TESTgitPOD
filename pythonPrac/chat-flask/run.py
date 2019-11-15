from flask import Flask 
import os

@app.route('/')

def index():
    return "<h1>Hello There!</h1>"
app.run(host= os.getenv(), port= int( os.getenv('PORT')), debug=True)
