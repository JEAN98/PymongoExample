from pymongo import MongoClient
import pymongo
from Team import Team
from Problem import Problem
from bson.objectid import ObjectId

client = MongoClient()
mongoClient = MongoClient('mongodb://localhost:27017/')
myDB = client.Game#DataBaseName
collectionTeams = myDB.Teams#Collection of teams
collectionProblem = myDB.Problem#Collection of Problem

teamsList = {
    Team(5,'Panama'),
    Team(2,'Suiza'),
    Team(3,'CostaRica'),
    Team(4,'Serbia')
}

problemsList = {
    Problem(1,'Sumar'),
    Problem(2,'Restar'),
    Problem(3,'Multiplicar'),
    Problem(4,'Dividir')
}
def inserIntoTeams():
    for team in teamsList:
       collectionTeams.insert(team.toDBCollection())
    print("Information was saved")

def insertIntoProblems():
    for problem in problemsList:
        collectionProblem.insert(problem.toDBCollection())
    print("Information was saved")

def printCollection():
    data = collectionTeams.find()
    print("Teams quantity: ",data.count())
    if data.count() > 0:
        for team in data:
            print(team['description'], "\n id: " + str(team['id']),"ObjectID: " + str(team['_id']) + "\n")
    else:
        print("The collection is empty!")

def printTeamsDESCENDING():
    result = collectionTeams.find().sort("id", pymongo.DESCENDING)
    for team in result:
        print(team['description'], "\n id: " + str(team['id']),"ObjectID: " + str(team['_id']) + "\n")


def printProblems():
    data = collectionProblem.find().sort("id", pymongo.ASCENDING)
    for problem in data:
        print(problem['description'], "\n id:"+ str(problem['id'])," ObjectID: " + str(problem['_id']) + "\n" )


def printProblemsByQuery():
    result = collectionProblem.find().sort("id", pymongo.DESCENDING).limit(1)
    for problem in result:
        print(problem['description'], "\n id:" + str(problem['id']), " ObjectID: " + str(problem['_id']) + "\n")

def updateByID():
    #Here we can update the data by objectID
    collectionTeams.update_one({'_id':ObjectId('your objectID')},
                               {'$set':{
                            'id':2222222
                           }})
    print("The information was updated!")

def searchByRegex():
    #Here we can search the information by regular expression
    result = collectionTeams.find({'description': {'$regex': '^C'}})
    for team in result:
        print (team['description'], "\n id: " + str(team['id']),"ObjectID: " + str(team['_id']) + "\n")

def removeAll():
    collectionTeams.delete_many({})
    collectionProblem.delete_many({})
    print("The data was removed!")


"""
Below of this comment appear all methods, you can try them
with only remove "#" and then run the console app.
I recommend you that use the methods in different executions,
because through of this way you can analyze the function of each one.
"""


inserIntoTeams()
insertIntoProblems()
#printProblems()
#printTeamsDESCENDING()
#updateByID()  #You must add your object id in the function
#printProblemsByQuery()
#searchByRegex()
#removeAll()