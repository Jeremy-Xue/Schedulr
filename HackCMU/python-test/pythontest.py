import cmu_course_api
import json

with open('test.json','r') as f:
    startDict = json.loads(f.read())
    courseDict = startDict["courses"].keys()


csList = ["15-128", "15-122", "15-150", "15-210", "15-213", "15-251", "15-451", "21-120", "21-122",
          "15-151", "21-241", "15-359"]

global classesTaken = ["15-112"]

def fillClassesTaken(classList):
    classList += str

def initSchedule():
    for day in range(5)
#def getMajorCores(major):


#print(courseDict)

print(startDict["courses"]["03-230"]["lectures"][0]["times"][0]["days"])
