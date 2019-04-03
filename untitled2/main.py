import urllib2
import urllib
import json
import os
import datetime
from flask import render_template, Flask,jsonify,make_response, Response
os.environ['no_proxy']='*'

app = Flask(__name__)


def wpjson():
    r = urllib2.urlopen('http://192.168.10.1/test.json')
    data=json.load(r)
    return data

@app.route('/')
def index():
    data = wpjson()
    data['datum']=datetime.datetime.fromtimestamp(float(data['datum'])).isoformat()
    return render_template('datawp.jinja2',data=data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
app.run(host='0.0.0.0',port = port)
