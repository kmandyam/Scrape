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

@app.route("/spectrum" , methods=['GET', 'POST'])

def spectrum():
    urlList = request.form['urlArray']

    urlList = json.loads(urlList)
    print urlList, "FIRST ONE"
    # print urlList

    print "HELLO WORLD", len(urlList)

    # numberOfArticles = len(urlList) + 2
    # #print numberOfArticles
    # conservativeScore = 1
    # liberalScore = 1
    # for url in urlList:
    #     try:
    #         actualURL = url.split("/")[2]
    #     except:
    #         print url, "error!!"
    #     # actualURL = url.split("/")[2]
    #     if "www." in actualURL:
    #         actualURL = actualURL.split("www.")[1]
    #     else:
    #         continue
    #     with open('data_liberal.csv', 'r') as f:
    #         for line in f.read().split('\r'):
    #             if actualURL == line:
    #                 liberalScore += 1
    #     with open('data_conservative.csv', 'r') as f:
    #         for line in f.read().split('\r'):
    #             if actualURL == line:
    #                 conservativeScore += 1
    #
    # #print conservativeScore
    # conservativeScore = float(conservativeScore)/float(numberOfArticles)
    # liberalScore = float(liberalScore)/float(numberOfArticles)
    # #print conservativeScore
    # #print liberalScore
    # val = 0
    # if liberalScore > conservativeScore:
    #     val =  -liberalScore*100
    # elif conservativeScore > liberalScore:
    #     val =  conservativeScore*100
    # else:
    #     val =  0
    # print "FINALLLL VALUEEEEE", str(val)
    return str(len(urlList))

    # return "88"

# @app.route("/credibility", methods=['GET', 'POST'])
#
# def credibility():
#     urlList = request.form['urlArray']
#     urlList = json.loads(urlList)
#     print urlList, "SECOND ONE"
#     # print "FINAL" , urlArray , "FINALLLLLL"
#     numberOfArticles = len(urlList) + 2
#     credibleScore = 1
#     notCredibleScore = 1
#     for url in urlList:
#         actualURL = url.split("/")[2]
#         if "www." in actualURL:
#             actualURL = actualURL.split("www.")[1]
#         else:
#             continue
#         with open('data_liberal.csv', 'r') as f:
#             for line in f.read().split('\r'):
#                 if actualURL == line:
#                     credibleScore += 1
#         with open('data_conservative.csv', 'r') as f:
#             for line in f.read().split('\r'):
#                 if actualURL == line:
#                     notCredibleScore += 1
#
#     credibleScore = float(credibleScore)/float(numberOfArticles)
#     notCredibleScore = float(notCredibleScore)/float(numberOfArticles)
#     val = 0
#     if credibleScore > notCredibleScore:
#         val = credibleScore*100
#         val -= 3
#     elif notCredibleScore > credibleScore:
#         val = (1-notCredibleScore)*100
#         val -= 3
#     else:
#         val = 0
#     print "FINALLLL VALUEEEEE222222", str(val)
#     return str(val)

app.run()
