import Skype4Py
#Use logging for debugging
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

def attachToSkype():
	global skype		
	# Connect the Skype object to the Skype client.
	skype.Attach()	

def writeToSkype( sBookmarkedChatTopic, sMessage ):
	for chat in skype.BookmarkedChats:
		if chat.Topic == sBookmarkedChatTopic:
			chat.SendMessage(sMessage)
    

