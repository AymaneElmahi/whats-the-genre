from nltk.stem import SnowballStemmer
import spacy
import nlp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import tensorflow as tf
import plotly.graph_objs as go
import string
import nltk
nltk.download('stopwords')

# Initialisation de l'objet SnowballStemmer pour le français
stemmer = SnowballStemmer('french')

# Fonction pour lemmatiser une chaîne de caractères


def lemmatize_text(text):
    """
    Cette fonction prend en entrée une chaîne de caractères 'text'
    et renvoie une version lemmatisée de cette chaîne, avec tous les
    mots au singulier et au masculin.
    """
    words = nltk.word_tokenize(text)  # Tokenisation en mots
    lemmatized_words = [stemmer.stem(word) for word in words]  # Lemmatisation
    # Reconstitution de la chaîne lemmatisée
    return ' '.join(lemmatized_words)


stopwords = nltk.corpus.stopwords.words('french')

nlp = spacy.load('fr_core_news_sm')


def return_NER(sentence):
    doc = nlp(sentence)
    return [(X.text, X.label_) for X in doc.ents]


def remove_NER(df_use, col):
    if col == 'title':
        df_use['NER_title'] = df_use['titre'].apply(lambda x: return_NER(x))

        # Iterate through each row
        for i, row in df_use.iterrows():
            ners = row['NER_title']

            for ner in ners:
                entity, tag = ner
                row['titre'] = row['titre'].replace(entity, '')
    if col == 'synopsis':
        df_use['NER_synopsis'] = df_use['synopsis'].apply(
            lambda x: return_NER(x))

        # Iterate through each row
        for i, row in df_use.iterrows():
            ners = row['NER_synopsis']

            for ner in ners:
                entity, tag = ner
                row['synopsis'] = row['synopsis'].replace(entity, '')


def process_title(df):
    df['titre'] = df['titre'].str.lower()
    df['titre'] = df['titre'].str.normalize('NFKD').str.encode(
        'ascii', errors='ignore').str.decode('utf-8')
    df['titre'] = df['titre'].str.translate(
        str.maketrans('', '', string.punctuation))
    df['titre'] = df['titre'].apply(lambda x: ' '.join(
        [word for word in x.split() if word not in (stopwords)]))
    df['titre_use'] = df['titre'].apply(lemmatize_text)
    return df


def process_synopsis(df):
    remove_NER(df, 'synopsis')
    df['synopsis'] = df['synopsis'].str.lower()
    df['synopsis'] = df['synopsis'].str.normalize('NFKD').str.encode(
        'ascii', errors='ignore').str.decode('utf-8')
    df['synopsis'] = df['synopsis'].str.translate(
        str.maketrans('', '', string.punctuation))
    df['synopsis'] = df['synopsis'].apply(lambda x: ' '.join(
        [word for word in x.split() if word not in (stopwords)]))
    df['synopsis_use'] = df['synopsis'].apply(lemmatize_text)
    return df


def process_df(df,train = True):
    if train:
        df = df.loc[:, ['synopsis', 'titre', 'genre']]
    else:
        df = df.loc[:, ['synopsis', 'titre']]
    df = process_title(df)
    df = process_synopsis(df)
    if train:
        df = df.loc[:, ['synopsis_use', 'titre_use', 'genre']]
    else:
        df = df.loc[:, ['synopsis_use', 'titre_use']]
    # mix the synopsis and the title
    df['synopsis_title'] = df['synopsis_use'] + ' ' + df['titre_use']
    if train:
        df = df.loc[:, ['synopsis_title', 'genre']]
    else:
        df = df.loc[:, ['synopsis_title']]
    return df
