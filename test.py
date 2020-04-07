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

def sortedMeetingTimes(schedule):
    days = {'monday': [], 
    'tuesday': [], 
    'wednesday':[], 
    'thursday': [], 
    'friday': [], 
    'saturday':[], 
    'sunday': []}
    

    for course in schedule:
        for meetingTime in course['meetingTimes']:
            if meetingTime['monday']:
                days['monday'].append(meetingTime)
            if meetingTime['tuesday']:
                days['tuesday'].append(meetingTime)
            if meetingTime['wednesday']:
                days['wednesday'].append(meetingTime)
            if meetingTime['thursday']:
                days['thursday'].append(meetingTime)
            if meetingTime['friday']:
                days['friday'].append(meetingTime)
            if meetingTime['saturday']:
                days['saturday'].append(meetingTime)
            if meetingTime['sunday']:
                days['sunday'].append(meetingTime)
            
    for day in days.keys():
        days[day] = sorted(days[day], key=lambda meetingTime: meetingTime['startTime'])

    return days

schedule = [
      {
         "isOpen":True,
         "campus":"CC",
         "meetingTimes":[
            {
               "saturday":False,
               "weeks":[
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
               "building":"TUCC",
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
         "isOpen":True,
         "campus":"MN",
         "meetingTimes":[
            {
               "saturday":False,
               "weeks":[
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
               "saturday":False,
               "weeks":[
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
         "campus":"MN",
         "meetingTimes":[
            {
               "saturday":False,
               "weeks":[
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
            "description":"GenEd Race &amp; Diversity",
            "isZTCAttribute":False,
            "code":"GD",
            "class":"net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
            "courseReferenceNumber":"25550",
            "termCode":"202036"
         },
         "courseName":"ANTH-0831",
         "title":"Immigration and the American Dream",
         "crn":25550
      },
      {
         "campus":"MN",
         "meetingTimes":[
            {
               "saturday":False,
               "weeks":[
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
               "saturday":False,
               "weeks":[
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
            "description":"_Core Science &amp; Technology A",
            "isZTCAttribute":False,
            "code":"SA",
            "class":"net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
            "courseReferenceNumber":"2184",
            "termCode":"202036"
         },
         "courseName":"KINS-1223",
         "title":"Human Anatomy and Physiology I",
         "crn":2184
      }
   ]

print(sortedMeetingTimes(schedule))