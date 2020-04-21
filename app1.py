import json
from difflib import get_close_matches as gcm

data = json.load(open('data.json'))


def definition(term):
    term = term.lower()
    if term in data.keys():
        return data[term]
    elif term.title() in data.keys():
        return data[term.title()]
    elif term.upper() in data.keys():
        return data[term.upper()]
    elif len(gcm(term, data.keys())) > 0:
        print("Did you mean '%s'?" % gcm(term, data.keys())[0])
        decision = input("Y or N: ")
        if decision.lower() == "y":
            return data[gcm(term, data.keys())[0]]
        elif decision.lower() == "n":
            return "That word doesn't exist, please check it."
        else:
            return "I'm not sure I understand your query, please try again."
    else:
        return "That word doesn't exist, please check it."


user_input = input("Enter a search term: ")
output = definition(user_input)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
