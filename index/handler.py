import cache

boto3, Day, Week, requests, json, AWS4Auth, asyncio, os = cache.exports()

loop = asyncio.get_event_loop()

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

    return {'weeklyTravel': results,
    'totalDuration': sum(map(lambda day: sum(travel['duration'] for travel in day.values()), results)),
    'totalDurationTraffic': sum(map(lambda day: sum(travel['durationTraffic'] for travel in day.values()), results)),
    'totalDistance': sum(map(lambda day: sum(travel['distance'] for travel in day.values()), results))
    }

def getAPIKey(key):
    with open('api_key.json') as f:
        data = json.load(f)

    return data[key]

async def getCampuses():
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

async def getTravel(waypoint1, waypoint2):
    university = os.environ['university']

    url = 'http://dev.virtualearth.net/REST/v1/Routes/Driving'

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

    return {(meetingTuple[0]['campus'],meetingTuple[0]['startTime'],meetingTuple[0]['endTime'],
    meetingTuple[1]['campus'],meetingTuple[1]['startTime'],meetingTuple[1]['endTime']): 
    await getTravel(meetingTuple[0]['campus'],meetingTuple[1]['campus']) for meetingTuple in day.meetingTuples}