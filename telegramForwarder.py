import telegram # pip install python-telegram-bot

TOKEN = "1466021539:AAGp5pryLtMONjzPl0QrdGGI1-VrrEDFN1c"  # Replace telegram bot api token here
START_MSG = 1  # Change value according your requirement
STOP_MSG = 10  # Change value according your requirement
DEST_ID = "@sourceUsername"  # change with your Source Channal Username/ID
SRC_ID = "@destinationUsername"  # change with your Destination/Backup Channal Username/ID

auth = telegram.Bot(token=TOKEN)
def forward(START_MSG):
    try :
        for msg in range (START_MSG,STOP_MSG+1):
            telegram.Bot.forwardMessage(auth, chat_id=DEST_ID, from_chat_id=SRC_ID, message_id=msg)
    except telegram.error.BadRequest:
        START_MSG = msg+1
        forward(START_MSG)

if __name__ == "__main__":
    forward(START_MSG)