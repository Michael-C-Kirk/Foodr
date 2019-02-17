import APIcalls as api
import urllib.parse
import urllib.request
import restarauntURL as restURL

GOOGLE_API_KEY = 'AIzaSyCSZkLStjQk7d1TPs7X7uwGj-yLRyjL2zA'
BASE_URL_PHOTOS = 'https://maps.googleapis.com/maps/api/place/photo?'

def buildPhotoURL(photoReference: str, maxHeight: int):
	'''builds image url'''
	BASE_URL_PHOTO = BASE_URL_PHOTOS
	query_parameters = [
    		('photoreference', photoReference), ('maxheight', maxHeight), ('key', GOOGLE_API_KEY)]

	return BASE_URL_PHOTO + urllib.parse.urlencode(query_parameters)

def ratingParser(infoDict: dict, rating: int, price = 5):
	'''
	infoDict: Dictionary of restaurant information
	rating: Int representing minimum restaraunt rating you prefer
	return: list of rating sorted restaraunt info (dictionary containing all restaraunt data), list of restataunt basic info (name & image)
	'''
	parsedInfo = []
	'''Contains parsed restaraunts name, rating and image url'''
	basicInfo = []

	for place in infoDict['results']:
		try:
			if (place['rating'] >= rating and place['price_level'] <= price and place['opening_hours']['open_now'] == True):
				parsedInfo.append(place)
				photoURL = buildPhotoURL(place['photos'][0]['photo_reference'], 500)
				#rURL = restURL.getRestarauntURL(place)
				basicInfo.append((place['name'], place['rating'], photoURL, place['place_id']))
		except:
			pass
			#("No rating")

	parsedInfo = sorted(parsedInfo, key = lambda pI: pI['rating'], reverse = True)
	basicInfo = sorted(basicInfo, key = lambda bI: bI[1], reverse = True)

	return parsedInfo, basicInfo

def priceParser(infoDict: dict, price: int):
	'''
	infoDict: Dictionary of restaurant information
	rating: Int representing minimum restaraunt rating you prefer
	return: list of price sorted restaraunt info (dictionary containing all restaraunt data), list of restataunt basic info (name & image)
	'''
	parsedInfo = []
	'''Contains parsed restaraunts name, rating and image url'''
	basicInfo = []

	for place in infoDict['results']:
		try:
			if (place['price_level'] <= price and place['opening_hours']['open_now'] == True):
				parsedInfo.append(place)
				photoURL = buildPhotoURL(place['photos'][0]['photo_reference'], 500)
				#rURL = restURL.getRestarauntURL(place)
				basicInfo.append((place['name'], place['rating'], photoURL, place["place_id"]))
		except:
			pass
			#("No price")

	parsedInfo = sorted(parsedInfo, key = lambda pI: pI['rating'], reverse = True)
	basicInfo = sorted(basicInfo, key = lambda bI: bI[1], reverse = True)

	return parsedInfo, basicInfo


if __name__ == '__main__':

	''' returns dictionary of api info param1 = radius, param2 = keyword '''
	foodDict = api.call(100000, "fast food")
	pInfo, bInfo = ratingParser(foodDict, 2)
	print ("bInfo:", bInfo[3])