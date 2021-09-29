#docs https://chatterbot.readthedocs.io/en/stable/setup.html
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import csv

file = open("covid_data.csv")
csvreader = csv.reader(file)
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

ans = []
for row in rows:
    ans.append(f"Location: {row[0]}, Cases: {row[1]}, Deaths: {row[2]}, Recoveries: {row[3]}" )

#read_only: = true : disable the bot ability to learn in the actual conversation
my_bot = ChatBot(
    'LongPro',
    read_only=True, 
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ])

data_to_train=[]
for count,row in enumerate(rows) :
    data_to_train.append(f"Covid situation in the {row[0]}?")
    data_to_train.append(ans[count])

list_trainer = ListTrainer(my_bot)

# print(data_to_train)
list_trainer.train(data_to_train)

#close .csv file
file.close()