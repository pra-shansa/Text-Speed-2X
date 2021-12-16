#import packages
from nltk import tokenize
from operator import itemgetter
import math

#Declare Variables
doc = 'Miniature art societies, such as the World Federation of Miniaturists (WFM) and Royal Miniature Society, provide applicable of the maximum size covered by the term.[1] An often-used definition is that a piece of miniature art can be held in the palm of the hand, or that it covers less than 25 square inches or 100 cm². Some exhibits require the subjects to be depicted in 1/6 actual size, and in all paintings the spirit of miniaturisation should be maintained.'

#Remove stopwords
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))

#Find total words in the document 
total_words = doc.split()
total_word_length = len(total_words)
print(total_word_length)

#Find the total number of sentences
total_sentences = tokenize.sent_tokenize(doc)
total_sent_len = len(total_sentences)
print(total_sent_len)

#Calculate TF for each word
tf_score = {}
for each_word in total_words:
    each_word = each_word.replace('.','')
    if each_word not in stop_words:
        if each_word in tf_score:
            tf_score[each_word] += 1
        else:
            tf_score[each_word] = 1

# Dividing by total_word_length for each dictionary element
tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())
print(tf_score)

#Function to check if the word is present in a sentence list
def check_sent(word, sentences): 
    final = [all([w in x for w in word]) for x in sentences] 
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))

#Calculate IDF for each word
idf_score = {}
for each_word in total_words:
    each_word = each_word.replace('.','')
    if each_word not in stop_words:
        if each_word in idf_score:
            idf_score[each_word] = check_sent(each_word, total_sentences)
        else:
            idf_score[each_word] = 1
# Performing a log and divide
idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())
print(idf_score)

#Calculate TF * IDF

tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
print(tf_idf_score)

#Create a function to get N important words in the document
def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
    return result
#Get the top 5 words of significance
print(get_top_n(tf_idf_score, 5))