all: talk.pdf notes.pdf

%.pdf : %.tex ../talk-header.tex
	pdflatex -halt-on-error $<
