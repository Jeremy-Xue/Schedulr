import cmu_course_api
import json

with open('test.json','r') as f:
    startDict = json.loads(f.read())
    courseDict = startDict["courses"].keys()

"""
csList = ["15-128", "15-122", "15-150", "15-210", "15-213", "15-251", "15-451", "21-120", "21-122",
          "15-151", "21-241", "15-359"]

global classesTaken = ["15-112"]

def fillClassesTaken(classList):
    classList += str"""

def initSchedule():
    sched = {}
    for day in range(5):
        sched[str(day)] = {}
        for rawTime in range(8, 23, 1):
            if(rawTime < 13):
                    time = str(rawTime) + ":00AM"
                    time = str(rawTime) + ":30AM"
            elif(rawTime>=12 and rawTime<13):
                    time = "12:00PM"
                    time = "12:30PM"
            elif(rawTime>13 and rawTime <=23):
                    time = str(rawTime - 12) + ":00PM"
                    time = str(rawTime - 12) + ":30PM"
            sched[str(day)][time] = False
    return sched


#def getMajorCores(major):


#print(courseDict)

#print(startDict["courses"]["03-230"]["lectures"][0]["times"][0]["days"])
