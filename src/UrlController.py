import json




class UrlController:
	def __init__(self):
		self.filename = "./environments/urls"

	def getUrl(self, query):
		file = open(self.filename)
		datas = json.load(file)
		file.close()

		return datas[query]


if __name__ == "__main__":
	uc = UrlController()
	print(uc.getUrl("test"))
