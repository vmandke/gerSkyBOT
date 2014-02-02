import commands
import json
import os

def getGerritStatus(sLogFile, sQuery, sDomain):
	listDone = [line.strip() for line in open(sLogFile)]
	op=(commands.getstatusoutput(sQuery))
	listStr = op[1].splitlines()

	listToMerge = []
	listToMerge.append([ json.loads(x)   for x in listStr if ('number' in json.loads(x) and sDomain in json.loads(x)['owner']['email']  and str(json.loads(x)['number']) not in  listDone )  ])
	# listMergerd is a list of list 
	listToMerge = listToMerge[0]
	outFile = open(sLogFile,'w')
	outFile.write(("\n".join(listDone)))
	outFile.write("\n");
	outFile.write(("\n".join([ x['number'] for x in  listToMerge ])))
	outFile.close()
	return listToMerge
	

