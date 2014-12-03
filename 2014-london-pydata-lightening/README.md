## Display the talk:

1. Open the latest version with your favorite app, thus:
```
xdg-open https://rawgit.com/JeffAbrahamson/talks/master/2014-london-pydata-lightening/talk.pdf
```

2. If you already pulled the git repository,
```
xdg-open talk.pdf
```

## Code

The code is in code/ .
The race data is in code/2014_ResultatsJourneeHuit.pdf .
The script code/get-data extracts the data to a suitable format to be read by pandas.
The script code/munge_data.py manipulates the data and makes the plots.

The talk itself builds by typing make.


## Feedback

Pull requests are always welcome.

My own self-feedback is that I need to find a better way of presenting
code so I can easily highlight things (and maybe get better syntax
highlighting).
