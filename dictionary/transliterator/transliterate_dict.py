import sys
import os
import re
import json

"""

This is the code used to transliterate the Amharic-Silte Dictionary
(presented in text file) to MRD(Machine readable dictionary)

"""
def main():	
	with open('transliterator.min.json','r', encoding="UTF-8") as f:
		trans_data = json.loads(f.read())
		#trans_file.close()
		trans_data = eval(trans_data)
		print(trans_data)

	with open('../amh_lex_dic.txt','r', encoding="utf-8") as f:
		dict_data = f.read()

	characters = re.findall('\w',dict_data)

	print ('Transliterating...')

	for char in characters:
		
		if char in trans_data:
			print(char+' = '+trans_data[char])
			dict_data = re.sub(char,trans_data[char],dict_data)

	with open('../amh_lex_dic.trans.txt','w',encoding="utf-8") as new_file:
		new_file.write(dict_data)
		new_file.close()

main()