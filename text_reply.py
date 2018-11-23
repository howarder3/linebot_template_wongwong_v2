from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#---------------- self define module ----------------
import text_push as text_push


#---------------- end of define module ----------------

def text_reply_message(user_message):
    if(user_message == "test"):
        output_message = "This is a test."
    elif(user_message == "push"):
        text_push.text_push_message("This is a Push test.")
        output_message = "This is Push test reply."
    else:  
        output_message = user_message  

    return TextSendMessage(text=output_message)