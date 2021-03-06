import requests
import answers

def day1(text):
    return 42
        
#Session cookie from browser
session = "keepthissecret"

if session == "keepthissecret":
    print("Did you remember to change your session ID?")

def get_input(i):
    try:
        with open(i + "_input.txt", "r"):
            return i.read()
    except:
        time.sleep(30)
        text = requests.get("http://adventofcode.com/day/" + str(i) + "/input", cookies={"session": session}).text
        with open(i + "_input.txt", "w"):
            i.write(text)
        return text

maxday = 0
for k in globals().keys():
    if k.startswith("day"):
        day = int(k[3:])
        if day > maxday:
            maxday = day

for i in range(1,maxday+1):
    answer = str(globals()["day"+str(i)](get_input(str(i))))
    print("Day " + str(i) + " answer: " + answer)
    #requests.post("http://adventofcode.com/day/" + str(i) + "/answer", data={"level": i, "answer": answer}, cookies={"session": session})
