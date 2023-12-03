import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the questions dataset
df = pd.read_csv("Q and A.csv")

# Create a TfidfVectorizer object with specified parameters
tfidf_vectorizer = TfidfVectorizer(max_df=0.5, max_features=10000)

# Fit and transform the questions text into a tf-idf weighted document-term matrix
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Question'].values.astype('U'))

# Get the feature names (terms) from the tfidf_vectorizer object
terms = tfidf_vectorizer.get_feature_names()

# Print the tf-idf matrix and feature names
print(tfidf_matrix)
print(terms)
