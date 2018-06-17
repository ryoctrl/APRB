#encoding: utf-8
### prepare for Twitter client main function.
import requests
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
import json
import os
import time
import twitter


### prepare self made classes
import MediaController
import Logging
import authcontroller as ac
 
mc = MediaController.MediaController("./pictures")

def  replyProcess(tweet):
	tome = False
	try:
		for i in xrange(len(tweet["entities"]["user_mentions"])):
			if tweet["entities"]["user_mentions"][i]["screen_name"] == "best_of_asi":
				tome = True
	except:
		return
	if not(tome):	
		return
	
	replytxt = tweet["text"]
	replytxt = replytxt.split(" ")
	### reply => "@best_of_asi $request $message"
	if not(len(replytxt) == 3):
		return

	request = replytxt[1]
	followUser = ""
	if request == "follow":
		followUser = replytxt[2]
	fromUser = tweet["user"]["screen_name"]
	
	print "ReplyFrom : " + fromUser
	print "request : " + request
	print "{0}to : {1}".format(request, followUser)
	twitter.follow(followUser, fromUser)


def displayTweet(tweet):
        tweetBy = tweet["user"]["name"]
        tweetById = tweet["user"]["screen_name"]
        tweet_text = tweet["text"]

        print(tweetBy + " @" + tweetById)
        print(tweet_text)
        mc.mediaManage(tweet)
	print("")

def run():
	url = "https://userstream.twitter.com/1.1/user.json"


        auth = ac.createNewAuth("best_of_asi")


        #connect to streaming api server
        r = requests.get(url, auth=auth, stream=True)

        comingFirst = False;

        #display received tweets after convert to json object
        for line in r.iter_lines():
                #print line
                if not(comingFirst):
                        print "ReadyForRetweet"
                        comingFirst = True
                if not(line):
                        continue
                tweet = json.loads(line)
                if "friends" in tweet:
                        continue
                if "delete" in tweet:
                        continue
                if "event" in tweet:
                        continue
                if tweet["user"]["screen_name"] == "best_of_asi":
                        continue
                if "entities" in tweet and "user_mentions" in tweet["entities"]:
                        replyProcess(tweet)
                if not("extended_entities" in tweet):
                        continue
                if "entities" in tweet and "user_mentions" in tweet["entities"]:
                        replyProcess(tweet)
                displayTweet(tweet)

if __name__ == "__main__":
	run()
