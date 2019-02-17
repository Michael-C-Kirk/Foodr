import APIcalls as api
import json
import urllib.parse
import urllib.request

GOOGLE_API_KEY = 'AIzaSyCSZkLStjQk7d1TPs7X7uwGj-yLRyjL2zA'
BASE_URL_REVIEWS = 'https://maps.googleapis.com/maps/api/place/details/json?'
#placeid=ChIJx2CibP8f3YARcQbnMMHF4g4&fields=name,rating,review&key=

def getRestarauntURL(restarauntID: str):
	'''
		restarauntDict: string representing a single restaraunt place_id
		return: string representing restaraunt url in google
	'''
	print(restarauntID)
	BASE_URL_REVIEW = BASE_URL_REVIEWS
	query_parameters = [
		('placeid', restarauntID), ('fields', 'name,url'), ('key', GOOGLE_API_KEY)]

	placeDetailsURL = BASE_URL_REVIEW + urllib.parse.urlencode(query_parameters)

	placeDetailsDict = api.get_result(placeDetailsURL)
	print(placeDetailsDict)
	return placeDetailsDict['result']['url'] 

if __name__ == '__main__':
	url = getRestarauntURL('ChIJCfEnZvfe3IAR-wUoHk2ewtg')
	print(url)
	pass
	#foodDict = api.call(100000, "fast food")
	#getRestarauntURL(foodDict['results'][0])
