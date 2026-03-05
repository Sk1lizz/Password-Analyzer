import json


with open(r"config.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)

print(data)