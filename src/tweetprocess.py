#encoding: utf-8
### prepare for Twitter client main function.
import requests
from requests_oauthlib import OAuth1
import json
#import ConfigParser
import configparser
import sys

### prepare self made classes
import MediaController
import authcontroller as ac
import twitter
import UrlController

mc = MediaController.MediaController("./pictures")
config = configparser.SafeConfigParser()
config.read("config.ini")

currentuser = config.get("settings", "user")

uc = UrlController.UrlController()



def  replyProcess(tweet):
        tome = False
        try:
        	for i in range(len(tweet["entities"]["user_mentions"])):
        		if tweet["entities"]["user_mentions"][i]["screen_name"] == currentuser:
        			tome = True
        except:
        	return
        if not(tome):	
        	return
        
        replytxt = tweet["text"]
        replytxt = replytxt.split(" ")
        ### reply => "@$currentuser $request $message"
        if not(len(replytxt) == 3):
        	return

        request = replytxt[1]
        followUser = ""
        if not(request == "follow"):
        	return
        followUser = replytxt[2]
        fromUser = tweet["user"]["screen_name"]
        
        twitter.follow(followUser, fromUser)


def displayTweet(tweet):
        tweetBy = tweet["user"]["name"]
        tweetById = tweet["user"]["screen_name"]
        tweet_text = tweet["text"]

        print(tweetBy + " @" + tweetById)
        print(tweet_text)
        mc.mediaManage(tweet)
        print("━━━━━━━━━━━━━")

def isFriendsJsonObject(tweet):
        if "friends" in tweet:
        	return True
        return False

def isDeleteJsonObject(tweet):
        if "delete" in tweet:
        	return True
        return False

def isEventJsonObject(tweet):
        if "event" in tweet:
        	return True
        return False

def isMyTweet(tweet):
        ### ToDo:ユーザー名をハードコーディング出なくconfigからの読み込みに変更
        if not("user" in tweet):
        	return False
        if tweet["user"]["screen_name"] != "best_of_asi":
        	return False
        return True

def tweetmanagement(tweet):
         if isFriendsJsonObject(tweet):
                return False
         if isDeleteJsonObject(tweet):
                return False
         if isEventJsonObject(tweet):
                return False
         if isMyTweet(tweet):
                return False
         if not("extended_entities" in tweet):
                return False
         return True        

def run():
        
        url = uc.getUrl("userstream")
        auth = ac.createNewAuth(currentuser)
        try:
        	r = requests.get(url, auth=auth, stream=True)
        except:
        	print("Connection Error, Please connect to internet")
        	sys.exit()
        comingFirst = False;
        for line in r.iter_lines():
                if not(comingFirst):
                        print("ReadyForRetweet")
                        comingFirst = True
                if not(line):
                        continue
                tweet = json.loads(line)
                #print(tweet)
                isProc = tweetmanagement(tweet)
                if isProc:
                        displayTweet(tweet)
