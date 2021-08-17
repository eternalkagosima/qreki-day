#!/usr/bin python3
# -*- coding: utf-8 -*-

# flask run
# localhost:5000/?year=2021&month=2&day=25
# {"day":14,"leap_month":0,"month":1,"rokuyou":"\u53cb\u5f15","year":2021}

from flask import Flask, jsonify, make_response, request
import json
from qreki import Kyureki

api = Flask(__name__)

@api.route('/', methods=['GET'])
def calcRoku():
	year = int(request.args.get("year"))
	month = int(request.args.get("month"))
	day = int(request.args.get("day"))
	qrk = Kyureki(year,month,0,day)
	qstr = qrk.from_ymd(year,month,day)
	result = {
		'year': 	qstr[0],
		'month':	qstr[1],
		'leap_month':	qstr[2],
		'day':		qstr[3],
		'rokuyou':	qrk.rokuyou
	}
	return make_response(jsonify(result))

if __name__ == '__main__':
	api.run(host='0.0.0.0', port=5000,debug=True)