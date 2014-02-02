import Skype4Py

def writeToSkype( sBookmarkedChatTopic, sMessage ):
	# Create an instance of the Skype class.
	skype = Skype4Py.Skype()
	# Connect the Skype object to the Skype client.
	skype.Attach()
	for chat in skype.BookmarkedChats:
	    if chat.Topic == sBookmarkedChatTopic:
		chat.SendMessage(sMessage)
    



#writeToSkype('Office Office !!!','hello')
