import json


def DisAmb_fun(amb_array,stem_words):

# Load JSON data from a file or API response
    with open("dictionary/transliterator/Amh_DisAmb.json", 'r', encoding='utf-8') as f:
        data = json.load(f)

   # print(amb_array)
   # print(stem_words)
# Loop through the students and courses to find the desired data
    count = 0
    for word_dict in data["data"]:
        if word_dict["Word"] in amb_array:
            count += 1
   # print(count)
    for text in data['data']:
        for i in amb_array:
            for j in stem_words:
                if text['Word'] == i:
                    if count > 1:
                        if text['Word'] == i and text['link']==j:
                            print('Ambigous word defn: '+ text['defn'])

                    else:
                        if text['Word'] == i:
                             print('Ambigous word defn: '+ text['defn'])

    return
