import handler
import os

os.environ['university'] = 'temple university'

#add key here to test
os.environ['bing_key'] = None

event = {'weeknum': 1,
    'schedule': [
        {
            "isOpen": True,
            "campusName": "Center City",
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
            "campusName": "Main",
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
            "campusName": "Main",
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
            "campusName": "Main",
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
                    "building":"RTTERX",
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
}

print(handler.lambda_handler(event, None))