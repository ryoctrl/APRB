#encoding: utf-8
### prepare for Twitter client main function.
import requests
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
import json
import os
import subprocess
import time

### prepare for waiting key method.
import fcntl
import termios
import sys
import os

### preapare for thread processing
import threading
import datetime

### prepare self made classes
import MediaController
import Logging

### preapre loading config module
#import ConfigParser
import configparser

def getAuth():
	#config = ConfigParser.SafeConfigParser()
	config = configparser.SafeConfigParser()
	config.read("config.ini")
	user = config.get("settings", "user")
	env_data = open('.env','r')
	apidata = json.load(env_data)
	env_data.close()

	apidata = apidata[user]

	api_key = apidata["api_key"]
	api_secret = apidata["api_secret"]
	access_token = apidata["access_token"]
	access_secret = apidata["access_secret"]

	return OAuth1(api_key, api_secret, access_token, access_secret)

def retweet(id):
	auth = getAuth()
	url = "https://api.twitter.com/1.1/statuses/retweet/" + id + ".json"
	## 例外処理
	try:
		r = requests.post(url, auth=auth)
		if r.status_code == 200:
			print("Anime Pic Retweeted")
		else:
 			print("Error StatusCode:" + str(r.status_code))
	except:
		print("retweet request was failed")

def tweet(message):
	auth = getAuth()
	url = "https://api.twitter.com/1.1/statuses/update.json"
	params = {
		"status": message
	}
	r = requests.post(url, auth = auth, params=params)
	if r.status_code == 200:
		print("Follow and tweet succeeded")
	else:
		print("Follow succeeded, but tweet failed")
		print("Errorcode: " + str(r.status_code))

	message = {
	
		"method":"tweet",
		"message":message,
		"Status_Code": r.status_code
	
	}

	Logging.write('tweet.log', message)


def follow(followto, fromuser):
	auth = getAuth()

	url = "https://api.twitter.com/1.1/friendships/create.json"

	params = {
	        "screen_name": followto
	}
	r = requests.post(url,auth=auth, params=params)

	if r.status_code == 200:
		text = followto + u"先生をフォローしました"
		tweet(text)
	else:
		text =  followto + u"先生をフォローできませんでした"
		tweet(text)

	message = {
		
		"method":"follow",
	        "ReplyFrom":fromuser,
	        "FollowTo":followto,
	        "Status_Code":r.status_code
	}
	
	Logging.write('follow.log', message )	
