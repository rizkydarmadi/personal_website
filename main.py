from crypt import methods
from flask import Flask, render_template
from markupsafe import Markup


app = Flask(__name__)

@app.route("/")
def home():
    # ambil content home dari database
    data = '''
    <h1>This is Home</h1>
    '''

    content = {
    "content": data, 
}
    return render_template('base.html',data=content)

@app.route("/library")
def library():
    # simpan data ke database
    data = '''
    <h1>This is library</h1>
    '''

    content = {
    "content": data, 
}
    return render_template('base.html',data=content)

@app.route("/contact")
def contact():
    # simpan data ke database
    data = '''

    <h1>this is contact</h1>


    '''

    content = {
    "content": data, 
}
    return render_template('base.html',data=content)