from pandas import pandas as pd
import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json


def preprocess(sentence):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(sentence)
    words = [lemmatizer.lemmatize(word.lower()) for word in words if word.lower() not in stop_words]
    return ' '.join(words)


def matter(sentence1, file):
    key = list(file.keys())
    ques = list(file[key[0]])
    for i in range(len(ques)):
        sentence2 = ques[i]

        processed1 = preprocess(sentence1)
        processed2 = preprocess(sentence2)

        vectorizer = TfidfVectorizer().fit_transform([processed1, processed2])
        similarity = cosine_similarity(vectorizer)[0][1]

        if similarity >= 0.6:
            return file[key[1]][i]
        else:
            pass


def function(sentence1):
    file = pd.read_csv("Q and A.csv")
    o = open("synm.json")
    syns = json.load(o)
    syn_key = [syns[i].keys() for i in range(len(syns))]
    syn_key = [i.lower() for il in syn_key for i in il]
    t = []
    for i in syn_key:
        if i.endswith('?'):
            t.append(i[:-1])
        else:
            t.append(i)
    key = list(file.keys())

    ques = list(file[key[0]])

    if matter(sentence1, file) is None:
        sen = sentence1.split(' ')
        lt = []
        for i in sen:
            if i in ques:
                lt.append(i)
            elif i in t:
                for j in range(len(syn_key)):
                    if i == syns[j].keys():
                        lt.append(i)
            else:
                for j in range(len(syn_key)):
                    if i in syns[j][syn_key[j]]:
                        lt.append(i)

    else:
        return matter(sentence1, file)


# Uncomment the following lines if you want to run the code in a loop and take input from the user
# while True:
#     sentence1 = input()
#     print(function(sentence1))
def matter(sentence1, file):
    key = list(file.keys())
    ques = list(file[key[0]])
    for i in range(len(ques)):
        sentence2 = ques[i]

        processed1 = preprocess(sentence1)
        processed2 = preprocess(sentence2)

        # Create a TfidfVectorizer instance
        vectorizer = TfidfVectorizer()

        # Fit-transform the processed sentences
        tfidf_matrix = vectorizer.fit_transform([processed1, processed2])

        # Compute cosine similarity
        similarity = cosine_similarity(tfidf_matrix)[0][1]

        if similarity >= 0.6:
            return file[key[1]][i]
        else:
            pass
