# Amharic Ambiguous word Finder

import json
import re

from nltk.tokenize import word_tokenize

am_stopwords = {"ነው", "ነበር", "እስከ", "ና", "እና", "ወይም", "ይህን", "ይህንን", "ላይ", "በ"}

back = ""


def amharic_tokenizer(text):
    tokens = word_tokenize(text)
    words = list(set(tokens))
    # Remove punctuation and numbers
    words = [word for word in words if word.isalpha()]

    # Remove stop words
    words = [word for word in words if word not in am_stopwords]

    return words


# input TEXT as an Input
text = input("Enter Your Sentence text: ")

# call function tokenizer
amharic_tokenizer(text)

print('\n---Tokenized word---')
print(amharic_tokenizer(text))
array = amharic_tokenizer(text)


def transliterate(user_input):
    with open("dictionary/transliterator/transliterator.min.json", 'r', encoding='utf-8') as trans_file:
        trans_data = json.loads(trans_file.read())
        trans_file.close()
        trans_data = eval(trans_data)

    characters = re.findall('\w', user_input)

    for char in characters:
        if char in trans_data:
            print(char + ' = ' + trans_data[char])
            user_input = re.sub(char, trans_data[char], user_input)

    return user_input


def stem(input1):
    # RULE 1 - Take input as it is
    print(input1)
    collection = [input1]

    # RULE 2 - Take out the right most suffix - From input 1
    input2 = re.match("(.+)(iwu|wu|wi|awī|na|mi|ma|li|ne|ache|ni)", input1)
    if input2:
        print(input2.group(1) + '-' + input2.group(2))
        input2 = input2.group(1);
        collection.append(input2)
    else:
        input2 = input1

    # RULE 3 - Take out the inner most suffix
    input3 = re.match('(.+)(ochi|bache|wache)', input2)
    input3 = re.match('(.+)(chi|ku|ki|ache|wal)', input2) if not input3 else input3
    if input3:
        print(input3.group(1) + '-' + input3.group(2))
        input3 = input3.group(1)
        collection.append(input3)
    else:
        input3 = input2

    # RULE 4 - Take out the most left prefix - From input 1
    input4 = re.match('(yemī|yete|inide|inidī|āli)(.+)', input1)
    input4 = re.match('(ye|yi|masi|le|ke|inid|be|sile|ā)(.+)', input1) if not input4 else input4
    if input4:
        print(input4.group(1) + '-' + input4.group(2))
        input4 = input4.group(2)
        collection.append(input4)
    else:
        input4 = input1

    # RULE 5 - Take out the right most suffix - From input 4
    input5 = re.match('(.+)(iwu|wu|w|awī|na|mi|ma|li|ne|che)', input4)
    if input5:
        print(input5.group(1) + '-' + input5.group(2))
        input5 = input5.group(1)
        collection.append(input5)
    else:
        input5 = input4

    # RULE 6 - Take out the inner most suffix - From input 4
    input6 = re.match('(.+)(ochi|bache|wache)', input5)
    input6 = re.match('(.+)(chi|ku|ki|che|wal)', input5) if not input6 else input6
    if input6:
        print(input6.group(1) + '-' + input6.group(2))
        input6 = input6.group(1)
        collection.append(input6)
    else:
        input6 = input5

    # RULE 7 - Take out the inner most prefix - From input 1
    input7 = re.match('(te|mī|mi|me|mayit|ma|bale|yit)(.+)', input4)
    if input7:
        print(input7.group(1) + '-' + input7.group(2))
        input7 = input7.group(2)
        collection.append(input7)
    else:
        input7 = input4

    # RULE 8 - Take out the right most suffix - From input 7
    input8 = re.match('(.+)(iwu|wu|w|awī|na|mi|ma|li|ne)', input7)
    if input8:
        print(input8.group(1) + '-' + input8.group(2));
        input8 = input8.group(1)
        collection.append(input8)
    else:
        input8 = input4

    # RULE 9 - Take out the innermost suffix - From input 8
    input9 = re.match('(.+)([^iīaeou])’?', input8)
    if input9:
        print(input9.group(1) + '-' + input9.group(2));
        input9 = input9.group(1)
        collection.append(input9)
    else:
        input9 = input4

    print(collection)

    return collection


def disambuigate(stems):
    with open('dictionary/amh_lex_dic.trans.txt', 'r', encoding='utf-8') as dictionary:
        lexical_data = dictionary.read()
        dictionary.close()

    match = None
    string_size = 0
    for stem in stems:
        temp = re.search('(' + stem + ')', lexical_data)
        if temp:
            if (len(stem) > string_size):
                string_size = len(stem)
                match = temp
        else:
            # Rule 10
            stem = re.match(r'(.+)[īaou]\b', stem)
            if stem:
                stems.append(re.sub(r'(.+)[īaou]\b', r'\1e', stem.group()))
                stems.append(re.sub(r'(.+)[īaou]\b', r'\1i', stem.group()))

    return match


# Check word Form ambigous Dictionary
def str_check(amb):
    with open('dictionary/amh_ambigous_dic.txt', 'r', encoding='utf-8') as dictionary:
        lexical_data = dictionary.read()
        dictionary.close()

    match = None
    string_size = 0

    # search ambigous word meaning

    temp = re.search('(' + amb + ')', lexical_data)
    if temp:
        print(temp.group(1))
        if len(amb) > string_size:
            string_size = len(amb)
            match = temp.group()

    return match


# Change English to Amharic
def chn_EN_Am(text):
    with open("dictionary/transliterator/Tran_En_Amh.min.json", 'r', encoding='utf-8') as trans_file:
        trans_data = json.loads(trans_file.read())
        trans_file.close()
        trans_data = eval(trans_data)

        for char in text:
            if char in trans_data:
                Tex_Cha = re.sub(char, trans_data[char], char)

        return Tex_Cha

def DisAmb_fun(amb_array,stem_words):

# Load JSON data from a file or API response
    with open("dictionary/transliterator/Amh_DisAmb.json", 'r', encoding='utf-8') as f:
        data = json.load(f)

# Loop through the students and courses to find the desired data
    for text in data['data']:
        for i in amb_array:
            for j in stem_words:
                if text['Word'] == i:
                    if text['link'] ==j:
                        print(text['defn'])

    return



# Main Part
def main():
    temp = []
    stem_words=[]
    for user_input in array:

        print('\n ---Normalize and transliterate---')
        user_input = transliterate(user_input)

        print('\n ---Stemming---')
        stems = stem(user_input)
        final = str_check(chn_EN_Am(stems))

        if (len(stems) > 1):
            print('\n ---Stem word in amharic character---')
            output = disambuigate(stems)
            if output:
                if final:
                    print(chn_EN_Am(stems))
                    temp.append(final)
                    stem_words.append(chn_EN_Am(stems))
                else:
                    print(chn_EN_Am(stems))
                    stem_words.append(chn_EN_Am(stems))
            else:
                if final:
                    print(chn_EN_Am(stems))
                    temp.append(final)
                    stem_words.append(chn_EN_Am(stems))
                else:
                    print(chn_EN_Am(stems))
                    stem_words.append(chn_EN_Am(stems))
        else:
            if final:
                print(chn_EN_Am(stems))
                temp.append(final)
                stem_words.append(chn_EN_Am(stems))
            else:
                print(chn_EN_Am(stems))
                stem_words.append(chn_EN_Am(stems))
    print('\n---Input Sentence---' + '\n' + text)
    print('\n\n ----Ambiguous words from the sentence-----')
    if len(temp) > 1:
        for i in temp:
            print('Words use for definition ፡'+ i)
    elif len(temp) == 1:
        print(temp)
    else:
        print('\n ---There is No Ambiguous Word---')
    import Ambiguous_check as amb
    amb.DisAmb_fun(temp, stem_words)


main()
