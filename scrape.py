from bs4 import BeautifulSoup
import urllib
import csv
from flask import Flask
from flask import request
from flask_cors import CORS
import json

import os, sys, csv, urllib

app = Flask(__name__)
CORS(app)

@app.route("/scrape" , methods=['GET', 'POST'])

def spectrum():
    urlList = request.form['urlArray']

    urlList = json.loads(urlList)
    print urlList, "FIRST ONE"
    # print urlList

    print "HELLO WORLD", len(urlList)
    return str(len(urlList))

app.run()
