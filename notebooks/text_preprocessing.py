import re
import nltk 

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords 

class Preporcessing():
    def __init__(self,l_text):
        self.text = " ".join(l_text)
        self.text = self.text.lower()
    def character_remove(self):
        text = re.sub(r'\d+','',self.text)
        text = re.sub(r'[^\w\s]','',text)
        return text
    def tokenize(self,text):
        return nltk.word_tokenize(text)
    def remove_stopwords(self,tokens):
        stop_words = set(stopwords.words('english'))
        return [word for word in tokens if word not in stop_words]
    def perform_lemmatization(self,tokens):
        lemmatizer = nltk.WordNetLemmatizer()
        return [lemmatizer.lemmatize(token) for token in tokens]