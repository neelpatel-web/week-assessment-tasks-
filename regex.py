import re
import json

ip = input("enter email for validatio : ")
pattern = r'^[A-Za-z0-9_-]+\@[a-z]+\.[a-z]+'

pas = input("Enter valid Pass : ")
password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"


if re.match(pattern,ip) and re.match(password_regex,pas):
    with open('user.json','r') as userdata:
        data = json.load(userdata)
    if ip in data:
        print("user already exists..")
    else:
        print("user add to data")
        with open('user.json','w') as d:
            data[ip]= pas
            json.dump(data,d,indent=4)
else:
    print("invalid")