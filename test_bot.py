from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#docs https://chatterbot.readthedocs.io/en/stable/setup.html

#read_only: = true : disable the bot ability to learn in the actual conversation

my_bot = ChatBot(
    'long2',
    read_only=True,
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ])

while True:
    try: 
        print("Question: ")
        question= input()      
        res=my_bot.get_response(question)
        print("Response: "+str(res))
        
    except(KeyboardInterrupt, EOFError, SystemExit):
        break