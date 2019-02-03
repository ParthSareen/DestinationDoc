# read the data from the URL and print it
import urllib.request

lat0 = '47.6044'
long0 = '-122.3345'
latEnd = '45.5347'
longEnd = '-122.6231'
modeTravel = 'driving'
startTime = '2017-06-15T8:00:00-07:00'
key = 'Asdk3ejMSqprmdrW3z-cKUKrLSI0CiPikjZ5QuU-fKmdT7xxPbQ3vwpfY9DzsS6D'


def whichDistShortest ():
	#open a connection to a URL using urllib
	webUrl = urllib.request.urlopen('https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins='lat0','long0'&destinations='latE','longE'&travelMode='modeTravel'&startTime='startTime'&timeUnit=minute&key='key)
	#get the result code and print it
	print("result code: " + str(webUrl.getcode()))
	#read the data from the URL and print it
	data = webUrl.read()
	print (data)

#https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=47.6044,-122.3345;47.6731,-122.1185;47.6149,-122.1936&destinations=45.5347,-122.6231;47.4747,-122.2057&travelMode=&key={BingMapsAPIKey}"""
'driving'