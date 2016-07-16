#all: talk.pdf notes.pdf
all: notes.pdf

%.pdf : %.tex ../talk-header.tex
	pdflatex -halt-on-error $<
