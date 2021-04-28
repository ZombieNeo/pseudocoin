from random import *
import time 
from datetime import datetime
nonce = randint(1,1000000)
start = datetime.now()
attempts = 0
loops = 0
while True:
    attempts = attempts + 1
    guess = randint(1,1000000)
    print(guess)
    if guess == nonce:
        end = datetime.now()
        print("started @" +str(start)+" finished @ "+str(end))
        print("WINNER!")
        print("in "+str(attempts)+" attempts")
        f = open("log.txt","a")
        f.write("nonce = "+str(nonce)+ " completed "+str(start)+","+str(end)+"\n")
        f.close()
        attempts = 0
        loops = loops + 1
        nonce = nonce = randint(1,1000000)
        while loops > 3:
            time.sleep(100000)
        
       