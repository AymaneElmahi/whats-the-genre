import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import tensorflow as tf
import plotly.graph_objs as go
import string 
import nltk
nltk.download('stopwords')
import nlp
import spacy
from nltk.stem.snowball import FrenchStemmer
from collections import Counter
from nltk.corpus import stopwords

custom_stopwords = ["the", "a", "an", "and", "or", "of", "to", 
                    "in", "for", "on", "with", "at", "by", 
                    "from", "as", "into", "like", "through", 
                    "after", "over", "between", "out", "against",
                    "during", "without", "before", "under", 
                    "around", "among", "throughout", "des", 
                    "du", "de", "la", "le", "les", "un", 
                    "une", "et", "ou", "pour", "dans", 
                    "sur", "par", "avec", "à", "en", "au",
                    "aux", "du", "des", "de", "la", "le", 
                    "les", "un", "une", "et", "ou", "pour", 
                    "dans", "sur", "par", "avec", "à", "en", 
                    "au", "aux", "du", "des", "de", "la", "le", 
                    "les", "un", "une", "et", "ou", "pour", "dans",
                    "sur", "par", "avec", "à", "en", "au", "aux", 
                    "du", "des", "de", "la", "le", "les", "un", 
                    "une", "et", "ou", "pour", "dans", "sur", 
                    "par", "avec", "à", "en", "au", "aux", "du", 
                    "des", "de", "la", "le", "les", "un", "une", 
                    "et", "ou", "pour", "dans", "sur", "par", "avec",
                    "à", "en", "au", "aux", "du", "des", "de", "la",
                    "le", "les", "un", "une", "et", "ou", "pour", 
                    "dans", "sur", "par", "avec", "à", "en", "au", "aux", "du", 
                    "des", "de", "la", "le", "les", "un", "une", "et", "ou", 
                    "pour", "dans", "sur", "par", "avec", "à", "en", "au", 
                    "aux", "du", "des", "l","1","2","3","4","5","6","7","8","9","0"]


def return_NER(sentence):
    nlp = spacy.load('fr_core_news_sm')
    doc = nlp(sentence)
    return [(X.text, X.label_) for X in doc.ents]

def remove_NER(df_use,col):
    if col == 'title':
        df_use['NER_title'] = df_use['titre'].apply(lambda x: return_NER(x))

        # Iterate through each row
        for i, row in df_use.iterrows():
            ners = row['NER_title']
    
            for ner in ners:
                entity, tag = ner
                row['titre'] = row['titre'].replace(entity, '')
    if col == 'synopsis':
        df_use['NER_synopsis'] = df_use['synopsis'].apply(lambda x: return_NER(x))

        # Iterate through each row
        for i, row in df_use.iterrows():
            ners = row['NER_synopsis']
    
            for ner in ners:
                entity, tag = ner
                row['synopsis'] = row['synopsis'].replace(entity, '')


def preprocess_text(text):
    text = text.lower()
    text = text.replace('-', ' ')
    text = text.replace("'", ' ')
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    text = text.split()
    # remove numbers
    text = [item for item in text if item.isalpha()]
    return text

def stem(text,custom_stopwords=[]):
    stemmer = FrenchStemmer()
    text = [stemmer.stem(item) for item in text]
    text = [item for item in text if item not in custom_stopwords]
    return text



def preprocess_data(df):
    df = df.loc[:, ['synopsis', 'titre', 'genre']]
    # title
    df['NER_title'] = df['titre'].apply(lambda x: return_NER(x))
    remove_NER(df,'title')
    df['tokenized_title'] = df['titre'].apply(preprocess_text)
    df['tokenized_title'] = df['tokenized_title'].apply(lambda x: stem(x, custom_stopwords))
    # synopsis
    df['NER_synopsis'] = df['synopsis'].apply(lambda x: return_NER(x))
    remove_NER(df,'synopsis')
    df['tokenized_synopsis'] = df['synopsis'].apply(preprocess_text)
    df['tokenized_synopsis'] = df['tokenized_synopsis'].apply(lambda x: stem(x, custom_stopwords))
    # combine title and synopsis
    df_new = pd.DataFrame()
    df_new['tokenized'] = df['tokenized_title'] + df['tokenized_synopsis']
    df_new['genre'] = df['genre']
    df_new['length'] = df_new['tokenized'].apply(lambda x: len(x))
    return df_new