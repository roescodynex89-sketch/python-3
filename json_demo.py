import json

user={
    "name":"steve smith",
    "age":22,
    "country":"aus",
    "ROLE":"batsman"
}
json_data=json.dumps(user)
data=json.loads(json_data)
print(data)
print(type(data))