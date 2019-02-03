#app.py

from flask import Flask, request #import main Flask class and request object
import requests
import json
import pytest

# 	url = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=AvZXOOO79Ko1HoL-HN1VuNQU0qtL842kjYVWuh3dL1uBLawZzHb9yydtD8rqhduA' % (physio, longs, lat)

app = Flask(__name__) #create the Flask app

@app.route('/physio')
def physio():
	url = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=AvZXOOO79Ko1HoL-HN1VuNQU0qtL842kjYVWuh3dL1uBLawZzHb9yydtD8rqhduA' % ('physiotherapy', '47.602038','-122.333964')
	#print(url)
	re = requests.get(url)
	returning = json.loads(re.text)
	#return returning['resourceSets']['0']['estimatedTotal'] '47.602038','-122.333964'
	#print(type(returning['resourceSets'][0]['resources']))
	#print(returning['resourceSets'][0]['resources'][0]['point']['coordinates'])
	Dict = {}
	for i in range(len(returning['resourceSets'][0]['resources'])-1):
		Result_name = returning['resourceSets'][0]['resources'][i]['name']
		Result_coordinates=returning['resourceSets'][0]['resources'][i]['point']['coordinates'] #

		print(Result_name)
		Dict[str(i)] = [Result_name,Result_coordinates]
	returnFile = json.dumps(Dict)
	payload = returnFile

	r = requests.post('https://www.jsonstore.io/71fc6d609168087b1bd76dea68e7694b4f451bfa7bf7ab5ebb4717dd15bb65d8', json = payload)
	return returnFile

@app.route('/dentist')
def dentist():
	url2 = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=AvZXOOO79Ko1HoL-HN1VuNQU0qtL842kjYVWuh3dL1uBLawZzHb9yydtD8rqhduA' % ('dentist', '47.602038','-122.333964')
	#print(url)
	re2 = requests.get(url2)
	returning2 = json.loads(re2.text)
	#return returning['resourceSets']['0']['estimatedTotal']
	#print(type(returning['resourceSets'][0]['resources']))
	#print(returning[f 'resourceSets'][0]['resources'][0]['point']['coordinates'])
	Dict2 = {}
	for i in range(len(returning2['resourceSets'][0]['resources'])-1):
		Result_name2 = returning2['resourceSets'][0]['resources'][i]['name']
		Result_coordinates2=returning2['resourceSets'][0]['resources'][i]['point']['coordinates']

		print(Result_name2)
		Dict2[str(i)] = [Result_name2,Result_coordinates2]#47.602038,-122.333964
	returnFile = json.dumps(Dict)
	payload = returnFile
	r = requests.post('https://www.jsonstore.io/71fc6d609168087b1bd76dea68e7694b4f451bfa7bf7ab5ebb4717dd15bb65d8', json = payload)

	return json.dumps(Dict2)
@app.route('/psychologist')
def psychologist():
	url = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=AvZXOOO79Ko1HoL-HN1VuNQU0qtL842kjYVWuh3dL1uBLawZzHb9yydtD8rqhduA' % ('psychologist', '47.602038','-122.333964')
	#print(url)
	re = requests.get(url)
	returning = json.loads(re.text)
	#return returning['resourceSets']['0']['estimatedTotal']
	#print(type(returning['resourceSets'][0]['resources']))
	#print(returning['resourceSets'][0]['resources'][0]['point']['coordinates'])
	Dict = {}
	for i in range(len(returning['resourceSets'][0]['resources'])-1):
		Result_name = returning['resourceSets'][0]['resources'][i]['name']
		Result_coordinates=returning['resourceSets'][0]['resources'][i]['point']['coordinates']

		print(Result_name)
		Dict[str(i)] = [Result_name,Result_coordinates]
	returnFile = json.dumps(Dict)
	payload = returnFile
	r = requests.post('https://www.jsonstore.io/71fc6d609168087b1bd76dea68e7694b4f451bfa7bf7ab5ebb4717dd15bb65d8', json = payload)

	return json.dumps(Dict)

@app.route('/clinic')
def clinic():
	url = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=AvZXOOO79Ko1HoL-HN1VuNQU0qtL842kjYVWuh3dL1uBLawZzHb9yydtD8rqhduA' % ('psychologist', '47.602038','-122.333964')
	#print(url)
	re = requests.get(url)
	returning = json.loads(re.text)
	#return returning['resourceSets']['0']['estimatedTotal']
	#print(type(returning['resourceSets'][0]['resources']))
	#print(returning['resourceSets'][0]['resources'][0]['point']['coordinates'])
	Dict = {}
	for i in range(len(returning['resourceSets'][0]['resources'])-1):
		Result_name = returning['resourceSets'][0]['resources'][i]['name']
		Result_coordinates=returning['resourceSets'][0]['resources'][i]['point']['coordinates']

		print(Result_name)
		Dict[str(i)] = [Result_name,Result_coordinates]
	returnFile = json.dumps(Dict)
	payload = returnFile
	r = requests.post('https://www.jsonstore.io/71fc6d609168087b1bd76dea68e7694b4f451bfa7bf7ab5ebb4717dd15bb65d8', json = payload)

	return json.dumps(Dict)

@app.route('/doctor')
def doctor():
	url = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=AvZXOOO79Ko1HoL-HN1VuNQU0qtL842kjYVWuh3dL1uBLawZzHb9yydtD8rqhduA' % ('psychologist', '47.602038','-122.333964')
	#print(url)
	re = requests.get(url)
	returning = json.loads(re.text)
	#return returning['resourceSets']['0']['estimatedTotal']
	#print(type(returning['resourceSets'][0]['resources']))
	#print(returning['resourceSets'][0]['resources'][0]['point']['coordinates'])
	Dict = {}
	for i in range(len(returning['resourceSets'][0]['resources'])-1):
		Result_name = returning['resourceSets'][0]['resources'][i]['name']
		Result_coordinates=returning['resourceSets'][0]['resources'][i]['point']['coordinates']

		print(Result_name)
		Dict[Result_name] = [Result_coordinates]
	returnFile = json.dumps(Dict)
	payload = returnFile
	r = requests.post('https://www.jsonstore.io/71fc6d609168087b1bd76dea68e7694b4f451bfa7bf7ab5ebb4717dd15bb65d8', json = payload)

	return json.dumps(Dict)

@app.route('/cisco')
def cisco():
	headers = {
    'X-Cisco-Meraki-API-Key': '4a1b555c1cacfb693bcf07f569119e7a0fbeec18',
	}
	re = requests.get('https://api.meraki.com/api/v0/devices/Q2GV-XLK8-MDBK/camera/analytics/recent', headers=headers)
	returning = json.loads(re.text)
	
	payload = re
	yeet = requests.post('https://www.jsonstore.io/039e0e4f386c305904fa8f4ff8b2f4953466ffb2537854a943978dba2fa3336e', json = payload)

	return re

@app.route('/json-example')
def jsonexample():
	return 'Todo...'

if __name__ == '__main__':
	app.run(debug=True, port=5000) #run app in debug mode on port 5000
