from day import Day

class Week():

    def __init__(self, schedule):
        self.monday = None
        self.tuesday = None
        self.wednesday = None
        self.thursday = None
        self.friday = None
        self.saturday = None
        self.sunday = None
        
        self.sortedDays(schedule)

    def sortedDays(self, schedule):
        days = [[] for i in range(7)]

        for course in schedule:
            dictAppend = {'campus': course['campus'],
            'courseName': course['courseName']}
            for meetingTime in course['meetingTimes']:
                if meetingTime['monday']:
                    days[0].append({**meetingTime, **dictAppend})
                if meetingTime['tuesday']:
                    days[1].append({**meetingTime, **dictAppend})
                if meetingTime['wednesday']:
                    days[2].append({**meetingTime, **dictAppend})
                if meetingTime['thursday']:
                    days[3].append({**meetingTime, **dictAppend})
                if meetingTime['friday']:
                    days[4].append({**meetingTime, **dictAppend})
                if meetingTime['saturday']:
                    days[5].append({**meetingTime, **dictAppend})
                if meetingTime['sunday']:
                    days[6].append({**meetingTime, **dictAppend})
                    
        sort = lambda meetingTime: meetingTime['startTime']

        self.monday = Day(sorted(days[0], key=sort))
        self.tuesday = Day(sorted(days[1], key=sort))
        self.wednesday = Day(sorted(days[2], key=sort))
        self.thursday = Day(sorted(days[3], key=sort))
        self.friday = Day(sorted(days[4], key=sort))
        self.saturday = Day(sorted(days[5], key=sort))
        self.sunday = Day(sorted(days[6], key=sort))