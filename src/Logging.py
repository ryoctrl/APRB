#encoding:utf-8
import os
import sys
import os.path
import json
import datetime

### filepathを/で分解してディレクトリ群とファイル名に分ける
### ディレクトリ群を検索してなければ作成
### ファイル名を検索してなければ作成したい
def fileCheck(filepath):
	if os.path.exists(filepath):
		return True
	else:
		return False

def write(filepath, message):
	if not(fileCheck(filepath)):
		print("Logfile not found")
		return
	
	file = open(filepath, 'r')
	datas = json.load(file)
	file.close


	date = datetime.datetime.today().strftime("%Y%m%d%H%M%S")

	newdata = {
		date:message
		#"createdAt":datetime.datetime.today().strftime("%Y%m%d%H%M%S"),
		#"message":message
	}
	datas.update(newdata)


	file = open(filepath, 'w')
	json.dump(datas, file, indent=4)
	file.close()
	print("Logging completed")
