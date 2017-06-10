#-*- coding: utf-8 -*-
from tenlineapp import app

def run_server():
    app.run("0.0.0.0", 5000, debug=True, use_reloader=True)

if __name__ == '__main__':
    run_server()