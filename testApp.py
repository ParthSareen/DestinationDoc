#app.py

from flask import Flask, request #import main Flask class and request object
import requests
import json
import pprint

app = Flask(__name__) #create the Flask app

@app.route('/query-example')
def query_example():
	categ=request.args["categ"]
	lat=request.args["lat"]
	longs=request.args["longs"]
	url = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=AvZXOOO79Ko1HoL-HN1VuNQU0qtL842kjYVWuh3dL1uBLawZzHb9yydtD8rqhduA' % (categ, lat, longs)
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

		@app.route('/form-example')
		def formexample():
			return 'Todo...'

@app.route('/json-example')
def jsonexample():
   return 'Todo...'

if __name__ == '__main__':
   app.run(debug=True, port=5000) #run app in debug mode on port 5000
