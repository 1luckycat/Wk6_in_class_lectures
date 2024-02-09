import decimal
import requests
import requests_cache
import json


# setup our api cache location (this will be a temporary database storing our api calls)
requests_cache.install_cache('image_cache', backend='sqlite')



def get_image(search):
    # 4 parts to every api:
    # 1. url Required
    # 2. queries/parameters (optional)
    # 3. headers/authorization (optional)
    # 4. body/posting (optional)
    url = "https://google-search72.p.rapidapi.com/imagesearch"

    querystring = {"q": search,"gl":"us","lr":"lang_en","num":"10","start":"0"}

    headers = {
	    "X-RapidAPI-Key": "dd03695a23msh3f0275a27580377p1bec69jsn1a5632f1e109",
	    "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)  # get method typically dont have a body

    data = response.json()

    img_url = ''
    
    if 'items' in data.keys():
        img_url = data['items'][0]['originalImageUrl']
    
    return img_url



# this is for flask backend to be able to work with any frontend
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):   # obj = any data obj from frontend
        if isinstance(obj, decimal.Decimal): #if the object is a decimal we are going to encode it 
                return str(obj)  # if its a decimal, we will change it to a string
        return json.JSONEncoder(JSONEncoder, self).default(obj) #if not the JSONEncoder from json class can handle it
    
