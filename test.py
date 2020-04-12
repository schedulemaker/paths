import requests
import json
from requests_aws4auth import AWS4Auth
import boto3
from week import Week


def getCampuses():
    session = requests.Session()

    APPSYNC_API_ENDPOINT_URL = 'https://taytm4ui6fhxjf3utp7p5foos4.appsync-api.us-east-2.amazonaws.com/graphql'

    query = """query GetCampuses(
      $school: String = "temple",
      $term: Int = 202036,
      $method: String = "getCampuses"
      ) {
      getBannerMetadata(school: $school, term: $term, method: $method) {
         code
         description
      }
      }"""

    response = session.request(
        url=APPSYNC_API_ENDPOINT_URL,
        method='POST',
        headers={'x-api-key': getAPIKey('appsync_key')},
        json={'query': query}
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

    params = {'waypoint.1': '{{temple university main campus}}',
              'waypoint.2': '{{temple university center city }}',
              'key': getAPIKey('bing_key'),
              'distanceUnit': 'mi'
              }

    r = requests.get(url, params=params)
    result = json.loads(r.text)

    print(result['resourceSets'][0]["resources"][0]["travelDistance"])
    print(result['resourceSets'][0]["resources"][0]["travelDuration"])
    print(result['resourceSets'][0]["resources"][0]["travelDurationTraffic"])

def getTravel(waypoint1, waypoint2):
    url = 'http://dev.virtualearth.net/REST/v1/Routes/Driving'

    params = {'waypoint.1': '{{temple university {}}}'.format(waypoint1),
              'waypoint.2': '{{temple university {}}}'.format(waypoint2),
              'key': getAPIKey('bing_key'),
              'distanceUnit': 'mi'
              }

    r = requests.get(url, params=params)
    result = json.loads(r.text)

    return {'distance': result['resourceSets'][0]["resources"][0]["travelDistance"],
    'duration': result['resourceSets'][0]["resources"][0]["travelDuration"],
    'durationTraffic': result['resourceSets'][0]["resources"][0]["travelDurationTraffic"]
    }

def testSchedule():
    schedule = [
        {
            "isOpen": True,
            "campus": "Center City",
            "meetingTimes": [
                {
                    "saturday": False,
                    "weeks": [
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7,
                        8,
                        9,
                        10,
                        11,
                        12,
                        13,
                        14,
                        15,
                        16
                    ],
                    "thursday":False,
                    "building":"TUCenter City",
                    "room":"00315",
                    "instructors":[

                    ],
                    "sunday":False,
                    "tuesday":True,
                    "wednesday":False,
                    "friday":False,
                    "startTime":1730,
                    "endTime":2050,
                    "monday":False
                }
            ],
            "courseName":"FMA-5671",
            "title":"Film History and Theory",
            "crn":44774
        },
        {
            "isOpen": True,
            "campus": "Main",
            "meetingTimes": [
                {
                    "saturday": False,
                    "weeks": [
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7,
                        8,
                        9,
                        10,
                        11,
                        12,
                        13,
                        14,
                        15,
                        16
                    ],
                    "thursday":False,
                    "building":"SERC",
                    "room":"00357",
                    "instructors":[
                        "Eugene Kwatny"
                    ],
                    "sunday":False,
                    "tuesday":False,
                    "wednesday":True,
                    "friday":False,
                    "startTime":900,
                    "endTime":1050,
                    "monday":False
                },
                {
                    "saturday": False,
                    "weeks": [
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7,
                        8,
                        9,
                        10,
                        11,
                        12,
                        13,
                        14,
                        15,
                        16
                    ],
                    "thursday":True,
                    "building":"BEURY",
                    "room":"00164",
                    "instructors":[
                        "Eugene Kwatny"
                    ],
                    "sunday":False,
                    "tuesday":True,
                    "wednesday":False,
                    "friday":False,
                    "startTime":1230,
                    "endTime":1350,
                    "monday":False
                }
            ],
            "courseName":"CIS-3207",
            "title":"Introduction to Systems Programming and Operating Systems",
            "crn":4308
        },
        {
            "campus": "Main",
            "meetingTimes": [
                {
                    "saturday": False,
                    "weeks": [
                        1,
                      2,
                      3,
                      4,
                      5,
                      6,
                      7,
                      8,
                      9,
                      10,
                      11,
                      12,
                      13,
                      14,
                      15,
                      16
                    ],
                    "thursday":False,
                    "building":None,
                    "room":None,
                    "instructors":[

                    ],
                    "sunday":False,
                    "tuesday":False,
                    "wednesday":False,
                    "friday":False,
                    "startTime":0,
                    "endTime":0,
                    "monday":False
                }
            ],
            "isOpen":True,
            "attributes":{
                "description": "GenEd Race &amp; Diversity",
                "isZTCAttribute": False,
                "code": "GD",
                "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
                "courseReferenceNumber": "25550",
                "termCode": "202036"
            },
            "courseName": "ANTH-0831",
            "title": "Immigration and the American Dream",
            "crn": 25550
        },
        {
            "campus": "Main",
            "meetingTimes": [
                {
                    "saturday": False,
                    "weeks": [
                        1,
                      2,
                      3,
                      4,
                      5,
                      6,
                      7,
                      8,
                      9,
                      10,
                      11,
                      12,
                      13,
                      14,
                      15,
                      16
                    ],
                    "thursday":True,
                    "building":"ANDRSN",
                    "room":"00017",
                    "instructors":[
                        "Kyle Harris",
                        "Kyle Suess"
                    ],
                    "sunday":False,
                    "tuesday":True,
                    "wednesday":False,
                    "friday":False,
                    "startTime":1400,
                    "endTime":1520,
                    "monday":False
                },
                {
                    "saturday": False,
                    "weeks": [
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7,
                        8,
                        9,
                        10,
                        11,
                        12,
                        13,
                        14,
                        15,
                        16
                    ],
                    "thursday":True,
                    "building":"PEARMC",
                    "room":"0P015",
                    "instructors":[
                        "Kyle Harris",
                        "Kyle Suess"
                    ],
                    "sunday":False,
                    "tuesday":False,
                    "wednesday":False,
                    "friday":False,
                    "startTime":1730,
                    "endTime":1920,
                    "monday":False
                }
            ],
            "isOpen":True,
            "attributes":{
                "description": "_Core Science &amp; Technology A",
                "isZTCAttribute": False,
                "code": "SA",
                "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
                "courseReferenceNumber": "2184",
                "termCode": "202036"
            },
            "courseName": "KINS-1223",
            "title": "Human Anatomy and Physiology I",
            "crn": 2184
        }
    ]

    sortedWeek = Week(schedule)

    print(calculateTravel(sortedWeek.tuesday))
    
def calculateTravel(day):
    #campuses = getCampuses()

    return {(meetingTuple[0]['courseName'],meetingTuple[0]['startTime'],meetingTuple[0]['endTime'],
    meetingTuple[1]['courseName'],meetingTuple[1]['startTime'],meetingTuple[1]['endTime']): getTravel(meetingTuple[0]['campus'],meetingTuple[1]['campus']) for meetingTuple in day.meetingTuples}


testSchedule()