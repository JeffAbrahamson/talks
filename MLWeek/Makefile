old:
	for d in J*-*; do if [ -d $$d ]; then (echo; echo; echo Making $$d && cd $$d && make); fi; done

%.pdf : %.tex talk-header.tex macros.tex
	pdflatex -halt-on-error $<

all: $(wildcard J*-*/talk.pdf)
	echo $(wildcard J*-*/talk.pdf)

