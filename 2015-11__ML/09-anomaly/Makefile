dummy:
	echo; echo "    ====  Nothing to make here. ===="; echo

all: talk.pdf notes.pdf

%.pdf : %.tex
	pdflatex -halt-on-error $<
