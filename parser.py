import APIcalls as api
import urllib.parse
import urllib.request

GOOGLE_API_KEY = 'AIzaSyCSZkLStjQk7d1TPs7X7uwGj-yLRyjL2zA'
BASE_URL_PHOTOS = 'https://maps.googleapis.com/maps/api/place/photo?'

def buildPhotoURL(photoReference: str, maxHeight: int):
	'''builds image url'''
	BASE_URL_PHOTO = BASE_URL_PHOTOS
	query_parameters = [
    		('photoreference', photoReference), ('maxheight', maxHeight), ('key', GOOGLE_API_KEY)]

	return BASE_URL_PHOTO + urllib.parse.urlencode(query_parameters)

def ratingParser(infoDict: dict, rating: int):
	'''
	infoDict: Dictionary of restaurant information
	rating: Int representing minimum restaraunt rating you prefer
	return: list of restaraunt parsed info (dictionary containing all restaraunt data), list of restataunt basic info (name & image)
	'''
	parsedInfo = []
	'''Contains parsed restaraunts name and image url'''
	basicInfo = []

	for place in infoDict['results']:
		try:
			if (place['rating'] >= rating):
				parsedInfo.append(place)
				photoURL = buildPhotoURL(place['photos'][0]['photo_reference'], 500)
				basicInfo.append((place['name'], photoURL))
		except:
			pass
			#("No rating")

	parsedInfo = sorted(parsedInfo, key = lambda pI: pI['rating'], reverse = True)
	return parsedInfo, basicInfo

if __name__ == '__main__':

	''' returns dictionary of api info param1 = radius, param2 = keyword '''
	foodDict = api.call(10000, "pizza")
	pInfo, bInfo = ratingParser(foodDict, 3)
	print (bInfo)
