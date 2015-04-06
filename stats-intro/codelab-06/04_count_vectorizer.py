import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

count_vectorizer = CountVectorizer()
# Fit learns the vocabulary.
# Transform does the count.
counts = count_vectorizer.fit_transform(np.asarray(data['text']))
