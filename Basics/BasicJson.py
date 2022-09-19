import json

person = {
    "fname": "Mike",
    "lname": "Hawk",
    "Age": 26
}

personjson = json.dumps(person)

print(personjson)

person = json.loads(personjson)

print(person)