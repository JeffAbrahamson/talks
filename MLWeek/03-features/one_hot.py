>>> from sklearn.feature_extraction import \
    DictVectorizer
>>> onehot_encoder = DictVectorizer()
>>> instances = [
    |{'city': 'New York'},|
    |{'city': 'San Francisco'},|
    |{'city': 'Chapel Hill'} ]|
>>> print onehot_encoder.fit_transform(instances) \
                        .toarray()
|[[ 0. 1. 0.] [ 0. 0. 1.][ 1. 0. 0.]]|
