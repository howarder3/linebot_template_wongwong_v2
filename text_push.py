from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#---------------- self define module ----------------
import mykey as mykey

#---------------- line settings ----------------
# Channel Access Token
line_bot_api = LineBotApi(mykey.LINE_CHANNEL_ACCESS_TOKEN)

TARGET_PUSH_ID = mykey.LINE_PUSH_TARGET_ID

#---------------------------------------------------

def text_push_message(msg):
	output_message = TextSendMessage(text=msg)
	line_bot_api.push_message(TARGET_PUSH_ID, output_message)