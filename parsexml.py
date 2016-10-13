from bs4 import BeautifulSoup
import os


# print os.listdir("dataset")

extractedXmls = []

def extractContent(filePath):
	catchphrases = []
	xmlText = open(filePath).read()
	xml     =  BeautifulSoup(xmlText, "html.parser")
	for tag in xml.findAll('catchphrase'):
		catchphrases.append(tag.text)
	doc = {
		"catchphrases" : catchphrases,
		# "sentence"     : xml.sentences.text
	}
	extractedXmls.append(doc)



for root, dirs, files in os.walk("dataset", topdown=False):
    for name in files:
        # print(os.path.join(root, name))
        extractContent(os.path.join(root, name))


print extractedXmls


# 


# # print xml.findAll('catchphrase')

# 



# print catchphrases
# # print xml.sentences.text


# y=BeautifulSoup(x)