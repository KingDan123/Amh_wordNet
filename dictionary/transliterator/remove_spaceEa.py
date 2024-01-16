
import re

"""
This is the code used to minify the transliterator producing a python readable
json file

"""

def main():
	with open('ambigous_dic.json','r',encoding="utf-8") as source:
		data = source.read()
		source.close()

	with open('ambigous_dic.min.json','w',encoding="utf-8") as source:
		data = re.sub(r'[\n\s]','',data)
		data = re.sub(r'\'\'','\'[]\'',data)
	
		data = source.write(data)
		source.close()

main()