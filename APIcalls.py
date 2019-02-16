import json
import urllib.parse
import urllib.request

GOOGLE_API_KEY = 'AIzaSyCSZkLStjQk7d1TPs7X7uwGj-yLRyjL2zA'
LOCATION_API_KEY = '610c80ba84b43729198fb6fa18a0216e'
BASE_URL_PLACES = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'#?location=-33.8670522,151.1957362&radius=1500&type=restaurant&keyword=cruise&key=YOUR_API_KEY'
BASE_URL_LOCATION = 'http://api.ipstack.com/check?access_key=610c80ba84b43729198fb6fa18a0216e&fields=main'

def build_url_location() -> str:
    pass
    

def build_url_place(latlong: str, raduis: str, keyword: str) -> str:
    '''builds search url'''
    BASE_URL_PLACE = BASE_URL_PLACES + '?location=' + latlong +'&'
    query_parameters = [
        ('radius', raduis), ('type', 'food'), ('keyword',keyword), ('key', GOOGLE_API_KEY)]

    return BASE_URL_PLACE + urllib.parse.urlencode(query_parameters)



def get_result(url: str) -> dict:
    '''
    This function takes a URL and returns a Python dictionary representing the
    parsed JSON response.
    '''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode('UTF-8')

        return json.loads(json_text)

    finally:
        if response != None:
            response.close()

def call(radius: str, keyword: str) -> dict:
    location = get_result(BASE_URL_LOCATION)
    locstr = str(location['latitude']) + ','+ str(location['longitude'])

    furl = build_url_place(locstr, '2000', 'mexican')

    final = get_result(furl)
    return final


if __name__ == '__main__':
    
    location = get_result(BASE_URL_LOCATION)
    locstr = str(location['latitude']) + ','+ str(location['longitude'])
    print(locstr)

    furl = build_url_place(locstr, '2000', 'mexican')
    print(furl)

    final = get_result(furl)
    print(final)

