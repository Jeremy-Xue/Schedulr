import cmu_course_api
import json

with open('test.json','r') as f:
    fullDict = json.loads(f.read())
    courseDict = fullDict["courses"].keys()

csList = ["15-451", "15-112", "15-122", "15-150", "15-210", "15-213", "15-251", "15-451", "21-120", "21-122",
          "21-241"] #Not full list

classesTaken = ["15-122"] #Make it so this is user input
coursesThisYear=[]
def fillClassesTaken():
    while True:
        prompt=input("Would you like to fill a class you've already taken (previously)?")
        if (prompt.lower()=="yes" or prompt.lower()=="y"):
            classes=input("What is the name of the class")
            classesTaken.append(classes)
        else:
            break
    while True:
        prompt = input("Would you like to fill a class you're taking this year already?")
        if (prompt.lower() == "yes" or prompt.lower() == "y"):
            classes2 = input("What is the name of the class")
            coursesThisYear.append(classes2)
        else:
            break
sched = {}

def initSchedule():
    #This will initialize a schedule with all false booleans
    for day in range(1, 6):
        sched[str(day)] = {}
        for rawTime in range(8, 23, 1):
            if(rawTime < 10):
                time = "0" + str(rawTime) + ":00AM"
                sched[str(day)][time] = False
                time = "0" + str(rawTime) + ":30AM"
                sched[str(day)][time] = False
            elif(rawTime < 13):
                time = str(rawTime) + ":00AM"
                sched[str(day)][time] = False
                time = str(rawTime) + ":30AM"
                sched[str(day)][time] = False
            elif(rawTime>=12 and rawTime<13):
                time = "12:00PM"
                sched[str(day)][time] = False
                time = "12:30PM"
                sched[str(day)][time] = False
            elif(rawTime>=13 and rawTime <=23):
                time = "0" + str(rawTime - 12) + ":00PM"
                sched[str(day)][time] = False
                time = "0" + str(rawTime - 12) + ":30PM"
                sched[str(day)][time] = False
    return sched

initSchedule()

def getCourseDuration(courseNum):
    begin = (fullDict["courses"][str(courseNum)]["lectures"][0]["times"][0]["begin"])
    end = (fullDict["courses"][str(courseNum)]["lectures"][0]["times"][0]["end"])
    beginInt = int(begin[:2])
    endInt = int(end[:2])
    if (begin[3] == "3"):
        beginInt += .5
    elif (begin[:2] != "12" and begin[5] == "P"):
        beginInt += 12
    elif (end[:2] != "12" and end[5] == "P"):
        endInt += 12
    elif (end[3] == "5"):
        endInt += 1
    elif (end[3] == "2"):
        endInt += .5
    duration = endInt - beginInt
    return duration

def timeStrToInt(timeStr):
    time = int(timeStr[:2])
    if (timeStr[3] == "3"):
        time += .5
    elif (timeStr[3] == "5"):
        time += 1
    if (timeStr[:2] != "12" and timeStr[5] == "P"):
        time += 12
    if (timeStr[3] == "2"):
        time += .5
    return time

def intToTimeStr(time):
    timeStr = ""
    if(time < 10):
        if(time % 1 == 0):
            timeStr += "0" + str(int(time//1)) + ":00AM"
        else:
            timeStr += "0" + str(int(time//1)) + ":30AM"
    elif(time >= 10 and time < 12):
        if(time % 1 == 0):
            timeStr += str(int(time//1)) + ":00AM"
        else:
            timeStr += str(int(time//1)) + ":30AM"
    elif(time < 13):
        if(time % 1 == 0):
            timeStr += "12:00AM"
        else:
            timeStr += "12:30AM"
    elif(time >= 13 and time <= 23):
        if(time % 1 == 0):
            timeStr += "0" + str(int(time - 12//1)) + ":00PM"
        else:
            timeStr += "0" + str(int(time - 12//1)) + ":30PM"
    return timeStr

def checkAvailability(days, begin, duration):
    beginTime = timeStrToInt(begin)
    for num in range (len(days)):
        day = days[num]
        for block in range (int(duration * 2)):
            time = beginTime + block/2
            timeStr = intToTimeStr(time)
            if(sched[str(day)][timeStr] == True):
                return False
    return True

possibleClasses = []

def returnPossibleClasses(majorList): #sched, , coursesTaken):
    fillClassesTaken()
    for course in range(len(majorList)):
        if majorList[course] in classesTaken or majorList[course] in coursesThisYear:
            continue
        courseNum = majorList[course]
        begin = (fullDict["courses"][str(courseNum)]["lectures"][0]["times"][0]["begin"])
        days = (fullDict["courses"][str(courseNum)]["lectures"][0]["times"][0]["days"])
        courseDuration = getCourseDuration(courseNum)
        unitsum=0
        for course in coursesThisYear:
            unitsum+=(fullDict["courses"][course]["units"])
        maxunits=54
        print (unitsum)
        if(checkAvailability(days, begin, courseDuration)):
            #for check in (fullDict["courses"][str (courseNum)]["prereqs"]):
            for check in coursesThisYear:
                if (not fullDict["courses"][str(courseNum)]["prereqs"]==None and check in fullDict["courses"][str (courseNum)]["prereqs"]):
                    if (unitsum+fullDict["courses"][str(courseNum)]["units"]<maxunits):
                        possibleClasses.append(str(courseNum))
    description=[]
    for cls in possibleClasses:
        description.append(fullDict["courses"][cls]["desc"])
    courseTitle=[]
    for title in possibleClasses:
        courseTitle.append(fullDict["courses"][title]["name"])
    print(possibleClasses)
    print (courseTitle)
    print (description)
    return possibleClasses


returnPossibleClasses(csList)
#so now theres two fields, classestaken and coursesthisyear. classes taken are for classes taken in the years before, while coursesthis year are courses you already know youre taking this year
#so now it does checking agianst both list, does unit limit check against the coursesthisyear, and does not suggest if that class would make the unit limit go over
#i hardcoded the unitlimit to 54 for cs major

#def getMajorCores(major):


#print(courseDict)

#print(fullDict["courses"]["03-230"]["lectures"][0]["times"][0]["begin"])