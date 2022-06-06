import os, sys, traceback, socket
from flask import Flask, request, Response, redirect, render_template, make_response, send_file
from app import app
from myapps.api.blueprint import api
from myapps.api.blueprintv2 import apiv2
app.register_blueprint(api)
app.register_blueprint(apiv2)

@app.route('/')
def defaultroute():
    filename=os.path.join('..', 'static', 'index.html')
    return send_file(filename, 'text/html')

if __name__ == '__main__':
    port = 8090     #default, or override on cmd-line
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port,debug=True)
