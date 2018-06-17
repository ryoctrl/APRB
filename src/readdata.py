import json
import os.path
import newUser



def existFile(filepath):
	if os.path.exists(filepath):
		return True
	f = open(filepath, 'w')
	f.write( {"api_secret": "0zpV5zL1WyohMl3p17Ixe6NHvxflNuDMzP1bAHz4qDFuN5RrbV","api_key": "a1rWnrTFDoqqHG13i7OInPIzI"})
	f.close()
	return False

def createNewUser(username):
	print("User:" + username  + "'s file does not exist! create new user!")
	f = open(".env", "r")
	data = json.load(f)
	f.close()
	#newUser.createNewUser(data["api_key"], data["api_secret"])

def getUserinfo(username):
	envFile = '.env'
	if not(existFile(envFile)):
		print("env file does not exist! so new file created!")
		createNewUser(username)
		return False

	env_data = open('.env','r')
	apidata = json.load(env_data)
	env_data.close()	
	
	if not(username in apidata):
		createNewUser(username)
		return False

	apidata = apidata[username]

	api_key = apidata["api_key"]
	api_secret = apidata["api_secret"]
	access_token = apidata["access_token"]
	access_secret = apidata["access_secret"]
	
	return api_key, api_secret, access_token, access_secret

if __name__ == "__main__":
	print(getUserinfo("mosin_n"))

