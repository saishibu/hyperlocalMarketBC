#!/usr/bin/python3
#(c)Sai Shibu
#201904170935ISTV1
#Sample program for Rest APIs
#Install Required Packages
#	1)Flask (pip install Flask)
#	2)Flask-ext MySQL (pip install Flask-MySQL)
#	3)Flask - Jsonify(mostly included with Flask)

#import necessary modules
from flask import Flask, jsonify,request
import os
import dispenserHelper as dh
import fuzzy
#assign a Flask Class
app=Flask(__name__)
global lastaddress

@app.route('/Dispenser/getAddress')
def getAddress():
	address=dh.addressGen()
	return str(address)

@app.route('/Dispenser/getBalance/<addy>')
def getbal(addy):
	bal=dh.getBalance(addy)
	return str(bal)

@app.route('/Dispenser/sendData/<address>/<data>')
def sendData(address,data):
	
	rc=dh.sendData(address,data)
	if rc==0:
		return "Transaction failed"
	elif rc==1:
		return "Transaction success"
	else:
		return "Transaction not processed"

@app.route('/Dispenser/sendMoney/<address>/<data>/<money>')

def sendMoney(address,data,money):
	rc=dh.sendMoney(address,data,money)
	if rc==0:
		return "Transaction failed"
	elif rc==1:
		return "Transaction success"
	else:
		return "Transaction not processed"

@app.route('/Dispenser/getCost/BS/<v1>/<v2>')
def getCostBS(v1,v2):
	cost=fuzzy.BS(int(v1),int(v2))
	return str(cost)

@app.route('/Dispenser/getCost/BP/<v1>/<v2>')
def getCostBP(v1,v2):
	cost=fuzzy.BP(int(v1),int(v2))
	return str(cost)

@app.route('/Dispenser/getCost/WP/<v1>/<v2>/<v3>')
def getCostWP(v1,v2,v3):
	cost=fuzzy.WP(int(v1),int(v2),int(v3))
	return str(cost)

@app.route('/Dispenser/getCost/WS/<v1>/<v2>')
def getCostWS(v1,v2,v3):
	cost=fuzzy.WP(int(v1),int(v2))
	return str(cost)

@app.route('/Dispenser/getCost/EP/<v1>/<v2>/<v3>')
def getCostEP(v1,v2,v3):
	cost=fuzzy.WP(int(v1),int(v2),int(v3))
	return str(cost)

@app.route('/Dispenser/getCost/ES/<v1>/<v2>/<v3>/<v4>')
def getCostES(v1,v2,v3,v4):
	cost=fuzzy.WP(int(v1),int(v2),int(v3),int(v4))
	return str(cost)


#Start the Flask program
if __name__ == '__main__':
#app.run will make the APIs available on this particular IP address and Port 5000
#0.0.0.0  ip means any one can access.
    app.run(host="0.0.0.0",port=4000,debug=1)

