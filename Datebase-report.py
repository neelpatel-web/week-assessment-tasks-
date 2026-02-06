from datetime import datetime

sales = [
    {"date": "2020-01-01", "amount": 1200},
    {"date": "2020-01-03", "amount": 950},
    {"date": "2024-01-05", "amount": 800},
    {"date": "2024-01-07", "amount": 1750},
    {"date": "2024-01-10", "amount": 1500},
    {"date": "2024-01-12", "amount": 600},
    {"date": "2024-01-15", "amount": 2200},
    {"date": "2026-01-18", "amount": 1300},
    {"date": "2026-01-20", "amount": 900}
]

sdate = datetime.strptime(input("Enter starting date : "),"%Y-%m-%d")
edate = datetime.strptime(input("Enter ending date : "),"%Y-%m-%d")
inrangesale =[]
total = 0
count =0
max = 0
min = sales[0]['amount']

for i in sales:
    cdate = datetime.strptime(i['date'],"%Y-%m-%d")

    if cdate > sdate and cdate < edate:
        inrangesale.append(i)
        total += i['amount']
        count+=1

        if max < i['amount']:
            max = i['amount']
        if min > i['amount']:
            min = i["amount"]


print("in range sale : ",inrangesale)
print("Total sales : ",total)
print("max sale in day : ",max)
print("min sale in day : ",min)
print("avg sale in range : ",total/count)