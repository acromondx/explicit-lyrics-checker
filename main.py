import csv
from collections import Counter
from lyrics_extractor import SongLyrics

ENGINE_ID = "*********************" #Google Custom Search Engine ID
API_KEY = "*********************************" # Google Custom Search API KEY

def lyrics2list(lyrics):
    res = list(lyrics.split(" "))
    return res

extract_lyrics = SongLyrics(API_KEY, ENGINE_ID)
data = extract_lyrics.get_lyrics("Fack by Eminem")
lyrics = data['lyrics']
title = data['title']

lyrics_list = lyrics2list(lyrics)

bad_words = []
with open('bad-words.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        bad_words.append(row[0])


hmm = []
for i in lyrics_list:
  if i in bad_words:
    # hmm.append(i.title())
    hmm.append(i)

counter_dict= Counter(hmm)

dict_badwords = {**counter_dict}
dict_badwords

dict_badwords_sorted= dict(sorted(dict_badwords.items(), key=lambda x: x[1],reverse=True))

# generator
# def output(dict_lyrics):
#   for key,value in dict_lyrics.items():
#     yield key,value
# a = output(dict_badwords_sorted)

#print outcome
if len(dict_badwords) == 0:
  print(f"I found 0 bad words in the {title}")
else:
  print(f"I found {sum(dict_badwords.values())} bad words in {title}:\n")
  for key,value in dict_badwords_sorted.items():
    print(key,value)
