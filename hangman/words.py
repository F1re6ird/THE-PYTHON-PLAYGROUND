import json

filename = "./word_bank.json"

with open(filename, 'r') as file:
    data = json.load(file)
