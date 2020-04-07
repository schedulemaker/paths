import requests
import json
from requests_aws4auth import AWS4Auth
import boto3

def getCampuses():
    session = requests.Session()

    APPSYNC_API_ENDPOINT_URL = 'https://otymenn5hncylox27rmmlwodcy.appsync-api.us-east-2.amazonaws.com/graphql'

    query = """query GetCampus( 
    $event: BannerProxyInput = {
        school: "temple"
        term: 202036
        method: "getCampus"
    }
    ) {
    getBannerMetadata(event: $event) {
        code
        description
    }
    }"""

    response = session.request(
        url = APPSYNC_API_ENDPOINT_URL,
        method = 'POST',
        headers= {'x-api-key': getAPIKey('appsync_key')},
        json= {'query': query}
    )

    campusDict = {}

    for i in response.json()['data']['getBannerMetadata']:
        campusDict[i['code']] = i['description']

    return campusDict

def getAPIKey(key):
    with open('api_key.json') as f:
        data = json.load(f)

    return data[key]

def testBingMaps():
    url = 'http://dev.virtualearth.net/REST/v1/Routes/Driving'

    params = {'waypoint.1': '{{temple university tuttleman learning center}}',
            'waypoint.2': '{{temple ambler campus}}',
            'key': getAPIKey('bing_key'),
            'distanceUnit': 'mi'
            }


    r = requests.get(url, params=params)
    result = json.loads(r.text)

    print(result['resourceSets'][0]["resources"][0]["travelDistance"])
    print(result['resourceSets'][0]["resources"][0]["travelDuration"])
    print(result['resourceSets'][0]["resources"][0]["travelDurationTraffic"])

    print(getCampuses())

print(getCampuses())