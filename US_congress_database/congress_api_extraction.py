import requests
import json
import configparser
import csv

parser = configparser.ConfigParser()
parser.read("pipeline.conf")
request = parser.get("us_congress_api", "request")
key = parser.get("us_congress_api", "key")

api_response = requests.get(request + key)

# create a json object from the response content
response_json = json.loads(api_response.content)
print(response_json)