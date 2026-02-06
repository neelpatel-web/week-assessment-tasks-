import json
from datetime import datetime 

with open('ticket.json','r') as t:
    data = json.load(t)


#Read JSON from file
print(data)

#count total ticket
print(len(data))

#count open vs close ticket
open =0
close = 0

for i in data:
    if i['status'] == 'open':
        open+=1
    else:
        close+=1

print("Total open ticket : ",open)
print("Total close ticket : ",close)


#Ticket by priority

prio = {}

for i in data:
    if i['priority'] not in prio:
        prio[i['priority']]=1
    else:
        prio[i['priority']]+=1

print(prio)


#only open ticket
print("only open ticket id ")
for i in data:
    if i['status']=='open':
        print(i['id'])

print()
#ticket after certain time 
time = "14-08-2020"
print("ticket after certain date")
time = datetime.strptime(time,"%d-%m-%Y")

for i in data:
    ntime = datetime.strptime(i['created'],"%Y-%m-%d")
    if ntime > time:
        print(i['id'])


