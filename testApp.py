#app.py

from flask import Flask, request #import main Flask class and request object
import requests
import json
import pprint
# 	url = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=AvZXOOO79Ko1HoL-HN1VuNQU0qtL842kjYVWuh3dL1uBLawZzHb9yydtD8rqhduA' % (physio, longs, lat)

app = Flask(__name__) #create the Flask app

@app.route('/physio')
def physio():
	url = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=AvZXOOO79Ko1HoL-HN1VuNQU0qtL842kjYVWuh3dL1uBLawZzHb9yydtD8rqhduA' % ('physiotherapy', '47.602038', '-122.333964')
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
	return json.dumps(Dict)
@app.route('/dentist')
def dentist():
	url2 = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=AvZXOOO79Ko1HoL-HN1VuNQU0qtL842kjYVWuh3dL1uBLawZzHb9yydtD8rqhduA' % ('dentist', '47.602038', '-122.333964')
	#print(url)
	re2 = requests.get(url2)
	returning2 = json.loads(re2.text)
	#return returning['resourceSets']['0']['estimatedTotal']
	#print(type(returning['resourceSets'][0]['resources']))
	#print(returning['resourceSets'][0]['resources'][0]['point']['coordinates'])
	Dict2 = {}
	for i in range(len(returning2['resourceSets'][0]['resources'])-1):
		Result_name2 = returning2['resourceSets'][0]['resources'][i]['name']
		Result_coordinates2=returning2['resourceSets'][0]['resources'][i]['point']['coordinates']

		print(Result_name2)
		Dict2[str(i)] = [Result_name2,Result_coordinates2]
	return json.dumps(Dict2)

@app.route('/form-example')
def formexample():
	return 'Todo...'

@app.route('/json-example')
def jsonexample():
	return 'Todo...'

if __name__ == '__main__':
	app.run(debug=True, port=5000) #run app in debug mode on port 5000
