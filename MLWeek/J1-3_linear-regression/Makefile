all: talk.pdf notes.pdf

%.pdf : %.tex ../talk-header.tex ../macros.tex
	pdflatex -halt-on-error $<
