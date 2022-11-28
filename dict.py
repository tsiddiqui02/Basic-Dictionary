import json
from difflib import get_close_matches

data = json.load(open("data.json"))
x = "word not found"

def main():
    y = True
    while y:
        word = input("Enter Word:")
        print(find(word))
        reply()
       
def find(s):
    s = s.lower()
    if s in data:
        return data[s]
    elif len(get_close_matches(s, data.keys())) > 0:
        res = input("did you mean %s instead Y or N?:" % get_close_matches(s,data.keys())[0]) 
        res = res.lower()
        while res != 'y' and res != 'n': 
            res = input("invalid. Plese type in Y OR N: ")
        if res == "y":
            return data[get_close_matches(s,data.keys())[0]]
        else:
            return x
    else:
            return x #instead of return x put name of function in function we will include similarity ratio and have return x at end

def reply():
    reply = input("would you like to try again? Y or N: ")
    reply = reply.lower()
    while reply != 'y' and reply != 'n': 
        reply = input("invalid. Please type in Y OR N: ")
    if reply == 'y':
        main()
    else:
        exit() 

main()