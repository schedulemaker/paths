class Day():

    def __init__(self, meetingTimes):
        self.meetingTimes = meetingTimes
        self.meetingTuples = []
        self.generateTuples()

    def generateTuples(self):
        for i in range(1, len(self.meetingTimes)):
            self.meetingTuples.append((self.meetingTimes[i-1], self.meetingTimes[i]))