import boto3
import json
import unittest 

with open("aws_keys.json", "r") as f:
  api_keys = json.load(f)

client = boto3.client('lambda', region_name='us-east-2',
    aws_access_key_id= api_keys['aws_access_key_id'],
    aws_secret_access_key= api_keys['aws_secret_access_key']
    )

def invoke(payload):
  response = client.invoke(FunctionName=api_keys['aws_function_name'],
    Payload=payload)

  return (json.loads(response['Payload'].read()))

'''TEST SCHEDULE WITH ONE CAMPUS'''
def testOneCampus():
  payload = '''{
    "weeknum":1,
    "schedule":[
      {
      "campus": "MN",
      "meetingTimes": [
        {
          "saturday": false,
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
          "endDate": "12/16/2020",
          "thursday": false,
          "building": "SERC",
          "room": "00357",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": false,
          "tuesday": false,
          "wednesday": true,
          "friday": false,
          "startTime": 900,
          "endTime": 1050,
          "startDate": "08/24/2020",
          "monday": false
        },
        {
          "saturday": false,
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
          "endDate": "12/16/2020",
          "thursday": true,
          "building": "BEURY",
          "room": "00164",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": false,
          "tuesday": true,
          "wednesday": false,
          "friday": false,
          "startTime": 1230,
          "endTime": 1350,
          "startDate": "08/24/2020",
          "monday": false
        }
      ],
      "isOpen": true,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 4308},
      {
      "campus": "MN",
      "meetingTimes": [
        {
          "saturday": false,
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
          "endDate": "12/16/2020",
          "thursday": true,
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Kyle Suess"
          ],
          "sunday": false,
          "tuesday": true,
          "wednesday": false,
          "friday": false,
          "startTime": 1400,
          "endTime": 1520,
          "startDate": "08/24/2020",
          "monday": false
        },
        {
          "saturday": false,
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
          "endDate": "12/16/2020",
          "thursday": true,
          "building": "PEARMC",
          "room": "0P015",
          "instructors": [
            "Kyle Harris",
            "Kyle Suess"
          ],
          "sunday": false,
          "tuesday": false,
          "wednesday": false,
          "friday": false,
          "startTime": 1730,
          "endTime": 1920,
          "startDate": "08/24/2020",
          "monday": false
        }
      ],
      "isOpen": true,
      "attributes": {
        "description": "_Core Science &amp; Technology A",
        "isZTCAttribute": false,
        "code": "SA",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "2184",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 2184
      }
    ]
  }'''

  return invoke(payload)

test1Expected = {
  "weeklyTravel": {
    "monday": {},
    "tuesday": {
      "Main,1230,1350,Main,1400,1520": {
        "distance": 0,
        "duration": 0,
        "durationTraffic": 0
      }
    },
    "wednesday": {},
    "thursday": {
      "Main,1230,1350,Main,1400,1520": {
        "distance": 0,
        "duration": 0,
        "durationTraffic": 0
      },
      "Main,1400,1520,Main,1730,1920": {
        "distance": 0,
        "duration": 0,
        "durationTraffic": 0
      }
    },
    "friday": {},
    "saturday": {},
    "sunday": {}
  },
  "totalDuration": 0,
  "totalDurationTraffic": 0,
  "totalDistance": 0
  }

class PathsOneCampus(unittest.TestCase):
  def setUp(self):
    self.results = testOneCampus()

  def runTest(self):
    self.assertEqual(self.results, test1Expected)   #correct results
    self.assertEqual(self.results['totalDuration'], 0)    #duration and distance should be 0 because same campus
    self.assertEqual(self.results['totalDurationTraffic'], 0)
    self.assertEqual(self.results['totalDistance'], 0)

'''TEST SCHEDULE WITH MULTIPLE CAMPUS'''
def testMultiCampuses():
  payload = '''{
  "weeknum": 1,
  "schedule": [
    {
      "campus": "AMB",
      "meetingTimes": [
        {
          "saturday": false,
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
          "endDate": "12/16/2020",
          "thursday": false,
          "building": "ONLINE",
          "room": "CLSRM",
          "instructors": [],
          "sunday": false,
          "tuesday": false,
          "wednesday": true,
          "friday": false,
          "startTime": 1900,
          "endTime": 2130,
          "startDate": "08/24/2020",
          "monday": false
        }
      ],
      "isOpen": true,
      "courseName": "LARC-8496",
      "title": "Landscape Traditions",
      "campusName": "Ambler",
      "crn": 8160
    },
    {
      "campus": "MN",
      "meetingTimes": [
        {
          "saturday": false,
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
          "endDate": "12/16/2020",
          "thursday": false,
          "building": "SERC",
          "room": "00357",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": false,
          "tuesday": false,
          "wednesday": true,
          "friday": false,
          "startTime": 1300,
          "endTime": 1450,
          "startDate": "08/24/2020",
          "monday": false
        },
        {
          "saturday": false,
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
          "endDate": "12/16/2020",
          "thursday": true,
          "building": "TTLMAN",
          "room": "00302",
          "instructors": [
            "Tamer Aldwairi"
          ],
          "sunday": false,
          "tuesday": true,
          "wednesday": false,
          "friday": false,
          "startTime": 1530,
          "endTime": 1650,
          "startDate": "08/24/2020",
          "monday": false
        }
      ],
      "isOpen": true,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 29894
    },
    {
      "campus": "MN",
      "meetingTimes": [
        {
          "saturday": false,
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
          "endDate": "12/16/2020",
          "thursday": true,
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Kyle Suess"
          ],
          "sunday": false,
          "tuesday": true,
          "wednesday": false,
          "friday": false,
          "startTime": 1400,
          "endTime": 1520,
          "startDate": "08/24/2020",
          "monday": false
        },
        {
          "saturday": false,
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
          "endDate": "12/16/2020",
          "thursday": false,
          "building": "PEARMC",
          "room": "0P015",
          "instructors": [
            "Kyle Harris",
            "Kyle Suess"
          ],
          "sunday": false,
          "tuesday": false,
          "wednesday": false,
          "friday": true,
          "startTime": 1400,
          "endTime": 1550,
          "startDate": "08/24/2020",
          "monday": false
        }
      ],
      "isOpen": true,
      "attributes": {
        "description": "_Core Science &amp; Technology A",
        "isZTCAttribute": false,
        "code": "SA",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "2606",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 2606
    },
    {
      "campus": "CC",
      "meetingTimes": [
        {
          "saturday": false,
          "weeks": [
            1,
            2,
            3,
            4,
            5,
            6,
            7
          ],
          "endDate": "10/12/2020",
          "thursday": false,
          "building": "TUCC",
          "room": "00320",
          "instructors": [
            "Karen M. Fox"
          ],
          "sunday": false,
          "tuesday": false,
          "wednesday": true,
          "friday": false,
          "startTime": 1730,
          "endTime": 1850,
          "startDate": "08/24/2020",
          "monday": false
        }
      ],
      "isOpen": true,
      "courseName": "BA-2101",
      "title": "Professional Development Strategies",
      "campusName": "Center City",
      "crn": 44664
    }
  ]
  }'''

  return invoke(payload)


class PathsMultiCampus(unittest.TestCase):
  def setUp(self):
    self.results = testMultiCampuses()

    self.totalDistance = 0
    self.totalDuration = 0
    self.totalDurationTraffic = 0

    #calculate total duration/distance from individual course pairs
    stack = list(self.results.items())
    while stack:
        k, v = stack.pop()
        if isinstance(v, dict):
            stack.extend(list(v.items()))
        else:
            if k == 'distance':
              self.totalDistance += float(v)
            elif k == 'duration':
              self.totalDuration += int(v)
            elif k == 'durationTraffic':
              self.totalDurationTraffic += int(v)

  def runTest(self):
    self.assertNotEqual(self.results['weeklyTravel']['wednesday']['Main,1300,1450,Center City,1730,1850']['distance'], 0)   #ensure non zero distance and duration between different campuses
    self.assertNotEqual(self.results['weeklyTravel']['wednesday']['Main,1300,1450,Center City,1730,1850']['duration'], 0)
    self.assertNotEqual(self.results['weeklyTravel']['wednesday']['Main,1300,1450,Center City,1730,1850']['durationTraffic'], 0)
  
    self.assertEqual(self.results['totalDistance'], self.totalDistance) #ensure total distance/duration/durationTraffic add up to correct result
    self.assertEqual(self.results['totalDuration'], self.totalDuration)
    self.assertEqual(self.results['totalDurationTraffic'], self.totalDurationTraffic)

'''TEST EXCEPTIONS'''
def testNoWeekNumException():
  payload = '''{
    "schedule":[
      {
      "campus": "MN",
      "meetingTimes": [
        {
          "saturday": false,
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
          "endDate": "12/16/2020",
          "thursday": false,
          "building": "SERC",
          "room": "00357",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": false,
          "tuesday": false,
          "wednesday": true,
          "friday": false,
          "startTime": 900,
          "endTime": 1050,
          "startDate": "08/24/2020",
          "monday": false
        },
        {
          "saturday": false,
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
          "endDate": "12/16/2020",
          "thursday": true,
          "building": "BEURY",
          "room": "00164",
          "instructors": [
            "Eugene Kwatny"
          ],
          "sunday": false,
          "tuesday": true,
          "wednesday": false,
          "friday": false,
          "startTime": 1230,
          "endTime": 1350,
          "startDate": "08/24/2020",
          "monday": false
        }
      ],
      "isOpen": true,
      "courseName": "CIS-3207",
      "title": "Introduction to Systems Programming and Operating Systems",
      "campusName": "Main",
      "crn": 4308},
      {
      "campus": "MN",
      "meetingTimes": [
        {
          "saturday": false,
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
          "endDate": "12/16/2020",
          "thursday": true,
          "building": "ANDRSN",
          "room": "00017",
          "instructors": [
            "Kyle Harris",
            "Kyle Suess"
          ],
          "sunday": false,
          "tuesday": true,
          "wednesday": false,
          "friday": false,
          "startTime": 1400,
          "endTime": 1520,
          "startDate": "08/24/2020",
          "monday": false
        },
        {
          "saturday": false,
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
          "endDate": "12/16/2020",
          "thursday": true,
          "building": "PEARMC",
          "room": "0P015",
          "instructors": [
            "Kyle Harris",
            "Kyle Suess"
          ],
          "sunday": false,
          "tuesday": false,
          "wednesday": false,
          "friday": false,
          "startTime": 1730,
          "endTime": 1920,
          "startDate": "08/24/2020",
          "monday": false
        }
      ],
      "isOpen": true,
      "attributes": {
        "description": "_Core Science &amp; Technology A",
        "isZTCAttribute": false,
        "code": "SA",
        "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",
        "courseReferenceNumber": "2184",
        "termCode": "202036"
      },
      "courseName": "KINS-1223",
      "title": "Human Anatomy and Physiology I",
      "campusName": "Main",
      "crn": 2184
      }
    ]
  }'''

  return invoke(payload)

class PathsNoWeekNumException(unittest.TestCase):
  def setUp(self):
    self.results = testNoWeekNumException()

  def runTest(self):
    self.assertTrue('KeyError' in self.results['errorType'])


def testNoScheduleException():
  payload = '''{
    "weekNum": 1
  }'''

  return invoke(payload)

class PathsNoScheduleException(unittest.TestCase):
  def setUp(self):
    self.results = testNoScheduleException()

  def runTest(self):
    self.assertTrue('KeyError' in self.results['errorType'])

'''RUN TESTS'''
suite = unittest.TestSuite()

suite.addTests([PathsOneCampus(),PathsMultiCampus(), PathsNoWeekNumException(), PathsNoScheduleException()])

unittest.TextTestRunner().run(suite)


