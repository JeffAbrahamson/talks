#!/usr/bin/env python

from les_pauvres_gens import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

bigram_vectorizer = CountVectorizer(ngram_range=(1,2))
bigram_ft = bigram_vectorizer.fit_transform(les_pauvres_gens)
bigram_analyze = bigram_vectorizer.build_analyzer()
bigram_analyze(phrase_1)
bigram_cosine_distance = 1 - cosine_similarity(bigram_ft)

for i in range(bigram_cosine_distance.shape[0]):
    for j in range(bigram_cosine_distance.shape[1]):
        if i < j:
            if bigram_cosine_distance[i, j] < .43:
                print('{i:3}, {j:3}: d={d:.2}\n   {t1}\n   {t2}'.format(
                    i=i, j=j, d=bigram_cosine_distance[i, j],
                    t1=les_pauvres_gens[i], t2=les_pauvres_gens[j]))
