#chatterbot-corpus : has all the responses
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from web import name
#read_only=True : used to disable chatbots ability to learn after the training
#chatterbot.logic.MathematicalEvaluation : helps to solve maths problems
#chatterbot.logic.BestMatch : used to choose best match from the list of responses
my_bot = ChatBot(name = 'Cia', read_only = True, logic_adapters = ['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch']) 

# small_talk = ['Hi',
#               'Hey',
#               'Hello',
#               'Hi there!',
#               'How do you do ?',
#               'How are you ?',
#               "I'm fine",
#               'Great!']

# bot_challenge = ['Aree you a bot/human?', 'I am Cia, a talkbot made by Ritika, Tanmay and Rohit.']
# math_talk = ['Pythagoras Theorem : a² + b² = c²']
# math_talk1 = ['Area of circle' ,'3.14r²']
list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk, math_talk1, bot_challenge):
    list_trainer.train(item)

def talkbot_func():
    while True:
        req = input( 'You: ')
        #req = req.upper()
            
        if req == 'Bye' or req == 'bye' or req == 'BYE':
            print('Bot: Bye, have a great day!')
            break
        else:
            res = my_bot.get_response(req)
            print("Bot:",res)