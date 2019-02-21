from flask import Flask
from flask import render_template,request
from flask_cors import *
import sys,os
sys.path.append(os.getcwd())
from hbjsrw import hbjsrwcx
from cxy import cxycx
import json
from gevent import monkey
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hbjswm():
    return render_template("hbjsrw.html")

@app.route('/3/',methods=["POST"])
def hblongs():
    cph = request.form.get("plate_number")
    b = hbjsrwcx.hbjsrw(cph=cph)
    return b

@app.route('/cxy/')
def cxy():
    return render_template("cxy.html")

@app.route('/2/',methods=["POST"])
def cxylongs():
    cph = request.form.get("cph")
    sbm = request.form.get("sbm")
    b = cxycx.cxy1(cph=cph, sbm=sbm)
    return b


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=9900)
    # http_server = WSGIServer(('0.0.0.0', 9900), app)
    # http_server.serve_forever()
