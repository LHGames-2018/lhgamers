from helper.structs import *

#path ici est une liste de Point avec des coord global

def goingTo(path=[]):
    stepInPath = []
    for i in range(len(path)):
        if(i < len(path)-1):
            #print("Sub between {} {}".format(path[i+1],path[i]))
            stepInPath.append(path[i+1] - path[i])
    return stepInPath


def pathStrToPoint(path=[]):
    rList = []
    if(path is not None):
        for e in path:
            rList.append(Point(int(e.split(",")[0]), int(e.split(",")[1])))
    return rList