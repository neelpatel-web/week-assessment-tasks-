data = []

with open('server.log','r') as log:
    for i in log:
        data.append(i.strip())

count =0
msg=[]
for i in data:
    if 'ERROR' in i:
        count+=1
        ind = i.index('ERROR')
        msg.append(i[ind+5:])

print(count)
print(msg)
