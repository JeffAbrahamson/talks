HAM = 0
SPAM = 1

SOURCES = [
    ('data/spam',         SPAM),
    ('data/easy_ham',     HAM),
    ('data/hard_ham',     HAM),
    ('data/beck-s',       HAM),
    ('data/farmer-d',     HAM),
    ('data/kaminski-v',   HAM),
    ('data/kitchen-l',    HAM),
    ('data/lokay-m',      HAM),
    ('data/williams-w3',  HAM),
    ('data/BG',           SPAM),
    ('data/GP',           SPAM),
    ('data/SH',           SPAM)
    ]

data = DataFrame({'text': [], 'class': []})
for path, classification in SOURCES:
    data = data.append(build_data_frame(path, classification))
  
data = data.reindex(numpy.random.permutation(data.index))
