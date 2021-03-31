import tweepy
import Reddit
import webbrowser
import time
import Private

consumer_key = Private.consumer_key
consumer_secret = Private.consumer_secret
access_token =  Private.access_token
access_token_secret = Private.access_token_secret 
#Reddit.Parse()

def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        return auth
    except Exception as e:
        return None


redditData = Reddit.Parse()
#print(redditData)
topTen = 0
dataString = ''
for key in redditData:
    if topTen < 10:
        dataString = dataString + key + " " + str(redditData[key]) + '\n'
        topTen += 1
print(dataString)
oauth = OAuth()
api = tweepy.API(oauth)
api.update_status(dataString)

