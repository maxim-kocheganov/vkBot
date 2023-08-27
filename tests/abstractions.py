from bot.messages import *

def MessageClassTest():
    message = Message()
    message.setText("Test")
    if (message.getText() != "Test"):
        raise Exception('message.getText() != "Test"')
    try:
        message.setText({'something':'somt'})
    except:
        pass
    else:
        raise Exception('message can\'t be set nothing but text')
    conference = Conference()
    conference.
    
    
    
def runTest():
    MessageClassTest()
        
        
