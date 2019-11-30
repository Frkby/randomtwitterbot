
import tweepy
import time
import string
import random
credentials = []
recoveryData = []
# Eskeetit
# Function: Reads the contents of a text file that contains the twitter API
#           OAuth credentials to the credentials list. If i was less lazy
#           I would make this used for all file reading and writing
#           but im  Australian and not German
def ReadFile():
    credentialsDoc = open("credentialsTextDocument.txt", "r")
    for line in credentialsDoc:
        credentials.append(line)
    credentialsDoc.close()
    
# Function: Takes the credentials from the ReadFile Function and uses them for OAuth
def AssignAuthValues():
    consumer_key = credentials[0].rstrip()
    consumer_secret = credentials[1].rstrip()
    access_token = credentials[2].rstrip()
    access_token_secret = credentials[3].rstrip()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    global api
    global numOfTweets
    api = tweepy.API(auth)
def RandomGenerator(size=280, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))
# Function: Tweets to the account
# Variable: String
def PostTweet(x):
    api.update_status(x)

