# from serpwow.google_search_results import GoogleSearchResultsimport
from serpwow.google_search_results import GoogleSearchResults
import geocoder
import json
serpwow = GoogleSearchResults("7491F4F9F2204722BD6A2BEEFAB0158E")
ipad = geocoder.ip('me')


def searchparams(cityname):

    q = "Pharmacy Stores near "+cityname
    location = cityname+","+str(ipad[0])
    params = {
        "q": q,
        "type": location,
        "country_code": "GB"
    }

    # retreive the google sewarc results
    result_json = serpwow.get_json(params)
    names = result_json['local_results']
    print(names)
    return names
