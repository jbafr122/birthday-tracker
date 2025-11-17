import os
from twilio.rest import Client
import datetime
from datetime import date

client = Client("", "")
bdays = []
date = datetime.datetime.now()

# checks for each name and assigns a birthday accordingly
with open('test.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        combo = line.split()
        name = combo[0]
        if (int(combo[1]) == date.month and int(combo[2]) == date.day):
            bdays.append(name)
print("Today is: ", date)
print(bdays)

message = client.messages.create(
        body="TEST",
        from_="",
        to="",
)
print(message.body)


        
        

    
