import APIcalls as api
import json
import urllib.parse
import urllib.request

GOOGLE_API_KEY = 'AIzaSyCSZkLStjQk7d1TPs7X7uwGj-yLRyjL2zA'
BASE_URL_REVIEWS = 'https://maps.googleapis.com/maps/api/place/details/json?'
#placeid=ChIJx2CibP8f3YARcQbnMMHF4g4&fields=name,rating,review&key=

def getRestarauntURL(restarauntDict: dict):
	'''
		restarauntDict: dictionary for a SINGLE restaraunt with json information
		return: string representing restaraunt url in google
	'''
	BASE_URL_REVIEW = BASE_URL_REVIEWS
	query_parameters = [
		('placeid', restarauntDict['place_id']), ('fields', 'name,url'), ('key', GOOGLE_API_KEY)]

	placeDetailsURL = BASE_URL_REVIEW + urllib.parse.urlencode(query_parameters)

	placeDetailsDict = api.get_result(placeDetailsURL)
	return placeDetailsDict['result']['url'] 

if __name__ == '__main__':

	pass
	#foodDict = api.call(100000, "fast food")
	#getRestarauntURL(foodDict['results'][0])