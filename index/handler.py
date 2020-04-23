import cache

Day, Week, requests, json, asyncio, os, deepcopy = cache.exports()

loop = asyncio.get_event_loop()

buildings = {"1300CB":"1300 CECIL B MOORE AVENUE",
"1700NB":"1700 N. BROAD STREET",
"1810LW":"1810 LIACOURAS WALK",
"1940NR":"1940 RESIDENCE HALL-LIACOURAS WALK",
"ALTER":"ALTER HALL AUDITORIUM",
"AMBRHT":"AMBLER-BRIGHT HALL",
"AMCOTT":"AMBLER-COTTAGE HALL",
"AMDIXN":"AMBLER DIXON HALL",
"AMDOUG":"AMBLER-DOUGLASS",
"AMGYM":"AMBLER GYMNASIUM",
"AMJUST":"AMBLER-HILDA JUSTICE HALL",
"AMLBRY":"AMBLER LIBRARY",
"AMLRNC":"AMBLER LEARNING CENTER",
"AMNGRN":"AMBLER GREENHOUSE",
"AMROSE":"AMBLER-ROSE COTTAGE",
"AMWIDE":"AMBLER-WIDENER HALL",
"ANDRSN":"ANDERSON HALL",
"ANNBRG":"ANNENBERG HALL",
"AZABU":"AZABU HALL",
"BARTNA":"BARTON HALL (A)",
"BARTNB":"BARTON HALL (B)",
"BEURY":"BEURY HALL",
"BIOSCI":"BIOLOGY-LIFE SCIENCES",
"CNWELL":"CONWELL HALL",
"ENGARC":"ENGINEERING BUILDING",
"FWCCTR":"TU FORT WASHINGTON",
"GLFLTR":"GLADFELTER HALL",
"HCHERS":"HARRISBURG-HERSEY",
"HCHUNT":"HARRISBURG-HUNTINGDON",
"HCLANC":"HARRISBURG-LANCASTER",
"HCPOTT":"HARRISBURG-POTTSVILLE",
"HGSC":"HOWARD GITTIS STUDENT CENTER",
"HRSBG":"HARRISBURG CAMPUS",
"JONES":"JONES HALL",
"JPNANX":"JAPAN CAMPUS ANNEX",
"KRESGE":"KRESGE SCIENCE HALL",
"MCGONH":"MCGONIGLE HALL",
"MEDRB":"MEDICAL RESEARCH BUILDING",
"MITA":"MITA HALL",
"MITTEN":"MITTEN HALL",
"MITTENX":"MITTEN ANNEX",
"OLDDNT":"DENTAL SCHOOL",
"PEARSH":"PEARSON HALL",
"PHRMAH":"PHARMACY-ALLIED HEALTH",
"PODMED":"COLLEGE OF PODIATRIC MEDICINE",
"PRESSR":"PRESSER HALL",
"RITTER":"RITTER HALL",
"ROCKHL":"ROCK HALL",
"RTTERX":"RITTER ANNEX",
"SFC":"STUDENT FACULTY CENTER",
"SPKMAN":"SPEAKMAN HALL",
"STUPAV":"STUDENT PAVILION RECREATION FACILITIES",
"TMLSON":"TOMLINSON HALL",
"TTLMAN":"TUTTLEMAN",
"TUCC":"TUCC 1515 MARKET STREET",
"TYLER":"TYLER SCHOOL OF ART",
"WCHMAN":"WACHMAN HALL",
"WEISS":"WEISS HALL"
}

def lambda_handler(event,context):
    return loop.run_until_complete(job(event,context))

async def job(event, context):
    schedule = event['schedule']
    weeknum = event['weeknum']

    sortedWeek = Week(Day, schedule, weeknum)

    # is this parallelized?
    tasks = [calculateTravel(sortedWeek.monday), calculateTravel(sortedWeek.tuesday), 
    calculateTravel(sortedWeek.wednesday), calculateTravel(sortedWeek.thursday), 
    calculateTravel(sortedWeek.friday), calculateTravel(sortedWeek.saturday), calculateTravel(sortedWeek.sunday)]

    results = await asyncio.gather(*tasks)
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


    return {'weeklyTravel': dict(zip(weekdays,results)),
    'totalDuration': sum(map(lambda day: sum(travel['duration'] for travel in day.values()), results)),
    'totalDurationTraffic': sum(map(lambda day: sum(travel['durationTraffic'] for travel in day.values()), results)),
    'totalDistance': sum(map(lambda day: sum(travel['distance'] for travel in day.values()), results))
    }

def getAPIKey(key):
    #with open('api_key.json') as f:
    #    data = json.load(f)

    #return data[key]

    return os.environ[key]

# async def getCampuses():
#     session = requests.Session()

#     APPSYNC_API_ENDPOINT_URL = 'https://taytm4ui6fhxjf3utp7p5foos4.appsync-api.us-east-2.amazonaws.com/graphql'

#     query = """query GetCampuses(
#       $school: String = "temple",
#       $term: Int = 202036,
#       $method: String = "getCampuses"
#       ) {
#       getBannerMetadata(school: $school, term: $term, method: $method) {
#          code
#          description
#       }
#       }"""

#     response = session.request(
#         url=APPSYNC_API_ENDPOINT_URL,
#         method='POST',
#         headers={'x-api-key': getAPIKey('appsync_key')},
#         json={'query': query}
#     )

#     campusDict = {}

#     for i in response.json()['data']['getBannerMetadata']:
#         campusDict[i['code']] = i['description']

#     return campusDict

async def getTravel(waypoint1, waypoint2, walking=False):
    university = os.environ['university']

    url = 'http://dev.virtualearth.net/REST/v1/Routes/Walking' if walking else 'http://dev.virtualearth.net/REST/v1/Routes/Driving'

    params = {'waypoint.1': '{{{} {}}}'.format(university, waypoint1),
              'waypoint.2': '{{{} {}}}'.format(university, waypoint2),
              'key': getAPIKey('bing_key'),
              'distanceUnit': 'mi'
              }

    r = requests.get(url, params=params)
    result = json.loads(r.text)

    return {'distance': result['resourceSets'][0]["resources"][0]["travelDistance"],
    'duration': result['resourceSets'][0]["resources"][0]["travelDuration"],
    'durationTraffic': result['resourceSets'][0]["resources"][0]["travelDurationTraffic"]
    }

async def calculateTravel(day):
    #campuses = getCampuses()
    newList = []

    for meetingTuple in day.meetingTuples:
        if (meetingTuple[0]['campusName'] == meetingTuple[1]['campusName'] and
        meetingTuple[0]['building'] != None and meetingTuple[1]['building'] != None):
            meetingTuple = deepcopy(meetingTuple)
            meetingTuple[0]['campusName'] = buildings.get(meetingTuple[0]['building'],meetingTuple[0]['building']).title()
            meetingTuple[1]['campusName'] = buildings.get(meetingTuple[1]['building'],meetingTuple[1]['building']).title()
            meetingTuple[0]['walking'] = True
        else:
            meetingTuple[0]['walking'] = False
        newList.append(meetingTuple)

    return {'{},{},{},{},{},{}'.format(meetingTuple[0]['campusName'],meetingTuple[0]['startTime'],meetingTuple[0]['endTime'],
    meetingTuple[1]['campusName'],meetingTuple[1]['startTime'],meetingTuple[1]['endTime']): 
    await getTravel(meetingTuple[0]['campusName'],meetingTuple[1]['campusName'],meetingTuple[0]['walking']) for meetingTuple in newList}