import os

from loremipsum import get_paragraphs
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    hostname = os.popen('hostname').read().strip()
    content = get_paragraphs(2)
    return render_template('home.html', content=content)
