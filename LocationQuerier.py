import requests
import xml.etree.ElementTree

URL = "http://api.geonames.org/search"

def query_location(location_name):
    """
    Make an API call to retrieve the normalized location based on
    the provided search string
    """

    request_params = {"q": location_name,
                      "username" : "dimagi"}

    # Make the call
    response = requests.get(URL, params=request_params)
    if response.status_code != 200:
        print "Web call error"
        return

    # Parse XML result
    tree = xml.etree.ElementTree.fromstring(response.text.encode("utf-8"))
    # Ensure that results were found
    if len(tree) <= 1:
        print "No results for query: {0}".format(location_name)
        return
    # Grab the first latitude and longitude from XML
    latitude = tree[1].find("lat").text
    longitude = tree[1].find("lng").text

    return latitude, longitude