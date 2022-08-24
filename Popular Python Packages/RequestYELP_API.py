# Cliend ID: 2JUEemPAtWfhby6DZxIyFA
# API Key: OoFEVwuPlmlw6cNtzTEOLPg0A0ZKnaiJU3Bt2EZQnfJKEkcPoZ8sHvp2UIMj0XkmctO9t9OwVXMgNF-h_OiubTX83hxTUPp0HOWRRB205r6gLe-nPq_K8SFgQAThYnYx

# 1: pip install request
import requests
from pprint import pprint
from config import api_key

# API end point in Yelp website
url = "https://api.yelp.com/v3/businesses/search"


# API key


# This Request has two sections/components (it's need YELP)
# 1: header - specify on a few some metadata about this request(key=value pairs)
# 2: pavload
headers = {
    "Authorization": "Bearer " + api_key,
}


params = {
    # location is required parameter
    "location": "NYC",
    # We can use a lots of parametrs
    'term': 'Barber'
}


# Sending http requst with method GET to the API end point
# Return the response object (JSON Data)
response = requests.get(url, headers=headers, params=params)

# print(response.text) - get information about response/data/errors

# Convert the result into a dictonary and get data from main key 'businesses'
# We get a list of dictionaris which we can unpacking
businesses = response.json()['businesses']


# For example get only name of Barbers
for barber in businesses:
    pprint(barber["name"])


# Using list comprehention to get the best barbers
topBarbers = [barber['name']
              for barber in businesses if barber['rating'] > 4.5]

pprint(topBarbers)
