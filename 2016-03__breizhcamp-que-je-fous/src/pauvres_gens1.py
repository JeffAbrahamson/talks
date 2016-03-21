    vectorizer = CountVectorizer(analyzer='word')
    ft = vectorizer.fit_transform(pauvres_gens)
    ft.todense()

    [1, 1, 0, 1, 2, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0]
    [0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1]
