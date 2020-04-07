import requests
import json

def getAPIKey():
    with open('api_key.json') as f:
        data = json.load(f)

    return data['key']

def test():
    url = 'http://dev.virtualearth.net/REST/v1/Routes/Driving'

    params = {'waypoint.1': '{{temple university tuttleman learning center}}',
            'waypoint.2': '{{temple ambler campus}}',
            'key': getAPIKey(),
            'distanceUnit': 'mi'
            }


    r = requests.get(url, params=params)
    result = json.loads(r.text)

    print(result['resourceSets'][0]["resources"][0]["travelDistance"])
    print(result['resourceSets'][0]["resources"][0]["travelDuration"])
    print(result['resourceSets'][0]["resources"][0]["travelDurationTraffic"])

test()