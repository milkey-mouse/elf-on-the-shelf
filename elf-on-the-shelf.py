import requests
import answers

def day1(text):
    return 42
        
#Session cookie from browser
session = "keepthissecret"

if session == "keepthissecret":
    print("Did you remember to change your session ID?")

maxday = 0
for k in globals().keys():
    if k.startswith("day"):
        day = int(k[3:])
        if day > maxday:
            maxday = day

for i in range(1,maxday+1):
    answer = str(globals()["day"+str(i)](requests.get("http://adventofcode.com/day/" + str(i) + "/input", cookies={"session": session}).text))
    print("Day " + str(i) + ": " + answer)
    requests.post("http://adventofcode.com/day/" + str(i) + "/answer", data={"level": i, "answer": answer}, cookies={"session": session})
