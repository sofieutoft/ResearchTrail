import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Remove punctuation and lower the text
    text = re.sub(r'[^\w\s]', '', text.lower())
    # Tokenize the text
    words = word_tokenize(text)
    # Remove stopwords
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)
