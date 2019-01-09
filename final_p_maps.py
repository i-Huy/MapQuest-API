# @file: final_p_maps.py handles the api
# @author: Huy
# @date: 12.11.18
# @version: Initial HN

import json
import http.client
import urllib.request
import urllib.error
import urllib.parse

API_KEY = "LrWe3gQF9bX9EtX13O5dH3ALghMOnwTZ"

# if no route is found
class RouteNotFoundError(Exception):
    pass

# Takes in tuple (direction api) start and end, returns the json text
def handle_api_dir(start_end: tuple) -> "json text":
    start_point,end_point = start_end
    http="http://open.mapquestapi.com/directions/v2/route?key="+ API_KEY +"&ambiguities=ignore&from="+start_point+"&to="+end_point
    response = urllib.request.urlopen(http)
    json_text = response.read().decode(encoding = "utf-8")
    json_text_fin = json.loads(json_text)

    if json_text_fin["info"]["messages"] == ["We are unable to route with the given locations."]:
        raise RouteNotFoundError

    return json_text_fin

# takes in dictionary (elevation api) lat and long, returns json text
def handle_api_elv(latlong: dict) -> "json text":
    elevation_http="http://open.mapquestapi.com/elevation/v1/profile?key=h9l8GngD4qpZ2qCfrc1KuGcx09tOELvt&shapeFormat=raw&unit=f&latLngCollection=" + str(latlong["lat"])+ "," + str(latlong["lng"])
    response_elv = urllib.request.urlopen(elevation_http)
    json_text_elv = response_elv.read().decode(encoding = "utf-8")
    final_elevation=json.loads(json_text_elv)
    return final_elevation
