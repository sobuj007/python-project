import json
import time
from  difflib import get_close_matches
data = json.load(open("data.json"))

s= open("testsfile.text",)
s.write("hello")
print( s.read(5))
def findword(w):
    w =w.lower()

    # print(data.values[f])
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))> 0:
        flist = get_close_matches(w, data.keys())[0]
        print('do you search ', flist)
        return data[flist]
    else:
        return "the word doesn't exist. Please double check"

while True:
    word = input("Enter word:")

    if word =='/end':
        break
    else:
        output = findword(word)

        if type(output) == list:
            for items in output:
                print(items)
        else:
            print(output)


