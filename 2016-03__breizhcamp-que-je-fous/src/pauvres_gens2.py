#!/usr/bin/env python

from les_pauvres_gens import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = CountVectorizer(analyzer='word')
ft = vectorizer.fit_transform(les_pauvres_gens)
cosine_distance = 1 - cosine_similarity(ft)

for i in range(cosine_distance.shape[0]):
    for j in range(cosine_distance.shape[1]):
        if i < j:
            if cosine_distance[i, j] < .43:
                print('{i:3}, {j:3}: d={d:.2}\n   {t1}\n   {t2}'.format(
                    i=i, j=j, d=cosine_distance[i, j],
                    t1=les_pauvres_gens[i], t2=les_pauvres_gens[j]))
