#encoding:utf-8
import datetime
import os.path

import AnimeRetweet
import twitter
import Logging

### storing and display medias included in tweet
class MediaController:
	def preparingPath(self, path):
		if not(path.endswith('/')):
			path += '/'
		
		return path

	def __init__(self, dirpath):
		self.dirpath = self.preparingPath(dirpath)
		self.logpath = './log.json'

	def directoryCheck():
		if not(os.path.isdir(dirpath)):
			os.mkdir(dirpath)
			print(dirpath +" was not found. so directory created.")

	
	

	### distinct movies or pictures
	def mediaCheck(self, ext_med):
		self.mediatype = ext_med["type"]
		
		if self.mediatype == "video":
			return "video"
		elif self.mediatype == "photo":
			return "photo"
		elif self.mediatype == "animated_gif":
			return "gif"
		else:
			Logging.write(self.logpath,"unknown media type:" + mediatype)
			return "photo"

	### download from URL
	def mediaDownload(self, targetMed):
		if self.mediatype == "video":
			url = targetMed["video_info"]["variants"][1]["url"]
			extension = ".mp4"
		elif self.mediatype == "photo":
			url = targetMed["media_url_https"] + ":orig"
			extension = ".jpg"
		elif self.mediatype == "animated_gif":
			url = targetMed["video_info"]["variants"][0]["url"]			
			extension = ".mp4"
		else:
			url = targetMed["media_url_https"]
			extension = ".jpg"

		filename = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
		filename += extension
		try:
			command = 'curl -o ' + self.dirpath + filename + ' -s ' + url
		except:
			print("self.dirpath type is:" + type(self.dirpath))
			print("filename type is:" + type(filename))
			print("url type is:" + type(url))
			return False
		try:
			os.system(command)
		except:
			Logging.write(logpath, "media download error:" +self.mediatype)
		return filename
	
	### display medias to console
	### because use imgcat, it only comes with iTerm
	def med_disp(self,targetMed, filename):
		path = self.dirpath + filename
		if self.mediatype=="photo" and os.path.exists(path):
			command = 'imgcat '+ path
			try:
				os.system(command)
			except:
				print("imgcat error")
				print("Command:" + command)


	### img move to girl/ directory	
	def med_move(self, filename):
		movingpath = self.dirpath + 'girl/'
		command = 'mv ' + self.dirpath + filename + ' ' + movingpath + filename
		try:
			os.system(command)
		except:
			print("moving file failed")


	### main process for medias included tweet
	### storing pictures and movies
	### displaying pictures
	### if detected anime face, retweet
	### tweet["extended_entities"]["media"][i]["media_url_https"]+ ":orig"
	def mediaManage(self, tweet):
		extended_media = False
		if "extended_entities" in tweet:
			extended = tweet["extended_entities"]
			if "media" in extended:
				extended_media = extended["media"]

		if not(extended_media):
			return
		
		isAnimepic = False
		#print(tweet)
		for i in range(len(extended_media)):
			targetMed = extended_media[i]
			self.mediaCheck(targetMed)
			f_name = self.mediaDownload(targetMed)
			if not(f_name):
				return
			self.med_disp(targetMed, f_name)
			if self.mediatype == "photo" and AnimeRetweet.facedetect(self.dirpath + f_name):
				isAnimepic = True
				id = tweet["id_str"]
				self.med_move(f_name)
		if isAnimepic:
			id = tweet["id_str"]
			twitter.retweet(id)
