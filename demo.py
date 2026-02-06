import json

with open('demo.json','r') as demo:
    data = json.load(demo)

print(data)

data['name']='Neel'

with open('demo.json','w') as demo:
    json.dump(data,demo,indent=4)


# Python dictionary
# python_dict = {
#     "name": "John Doe",
#     "age": 28,
#     "city": "Houston",
#     "is_employed": True,
#     "spouse": None
# }

# data = json.dumps(python_dict,indent=4)
# print(data)



# with open('demo.json','w') as d:
#     json.dump(python_dict,d,indent=4)


# # Convert Python dict to JSON string (Serialization)
# json_string = json.dumps(python_dict, indent=4)
# print(f"JSON String:\n{json_string}")
# print(f"Type after dumps: {type(json_string)}")

# # Convert JSON string back to Python dict (Deserialization)
# back_to_dict = json.loads(json_string)
# print(f"\nPython Dict: {back_to_dict}")
# print(f"Type after loads: {type(back_to_dict)}")

# with open('json.json','r') as f:
#     data = json.load(f)

# print(type(data))
# print(data[0:2])

# print(json.dumps(data,indent=4))

# for i in data:
#     for f in i['friends']:
#         print(f['name'])


# for i in data:
#     print("Greeting msg for",i['name'],i['greeting'])