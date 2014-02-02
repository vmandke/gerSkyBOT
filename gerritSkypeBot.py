import gerrit
import skype
import json


sQuery = ""
sLogMergeFile = ""
sOpenLogFile = ""
sEmailDomain = ""
sBookmarkedChatTopic = ""

def readConfig():
	global sQuery, sLogMergeFile, sOpenLogFile, sEmailDomain, sBookmarkedChatTopic
	jdata=open('config.json')
	jConfig = json.load(jdata)
	sQuery = (  "ssh  -p " + jConfig['port'] 
		 + " " + jConfig['gerritUserName'] + "@" + jConfig['gerritReviewURL']
		 + "  gerrit query --format=JSON  limit:" + jConfig['limitOfOutput']
		 + "  status:" ) ;
	sEmailDomain = jConfig['commonEmailDomain']
	sOpenLogFile = jConfig['openLogFile']
	sLogMergeFile = jConfig['mergesLogFile']
	sBookmarkedChatTopic = jConfig['BookmarkedChatTopic']


readConfig()

def updateStatus(statusType):
	global sQuery
	sQuery = sQuery + statusType
	if statusType == merged:
		newStatus = gerrit.getGerritStatus(sLogMergeFile, sQuery, sEmailDomain)
		for x in newStatus:
			sMessage = 'GERRIT BOT ::: ' + x['owner']['name'] + "'s patch " + x['url'] + " has been merged (y)"
			skype.writeToSkype(sBookmarkedChatTopic, sMessage)
	else:
		newStatus = gerrit.getGerritStatus(sOpenLogFile, sQuery, sEmailDomain)
		for x in newStatus:
			sMessage = 'GERRIT BOT ::: ' + x['owner']['name'] + " has submitted patch " + x['url']
			skype.writeToSkype(sBookmarkedChatTopic, sMessage)


