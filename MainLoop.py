# python pls
from TwitterBot import *
import time

#Setup
ReadFile()
AssignAuthValues()

while True:
    StringToTweet = RandomGenerator()
    PostTweet(StringToTweet)    
    time.sleep(86400) # 1 day in unix time
    