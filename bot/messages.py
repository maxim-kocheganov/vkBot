class MasterDB:
    def __init__(self):
        self.conferences = []
        self.messages = []
    def newConference(self,conference):
        conferences.append(conference)
    def newMessage(self,message):
        messages.append(message)
        

class Conference:
    def __init__(self):
        self.messages = []
        self.conferenceID = None 
    def addMessage(self,messageID):
       self.messages.append()
    
class Message:
    def __init__(self,ID, text):
        self.msgID = ID
        self.raw = None
        self.setText(text)
    def getText(self):
        return self.raw
    def setText(self, text):
        if (isinstance(text,str)):
            self.raw = text
        else:
            raise TypeError("Can't set that as text") 
