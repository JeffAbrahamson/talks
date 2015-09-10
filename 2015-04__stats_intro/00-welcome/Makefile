../00-welcome.pdf : talk.tex ../setup.tex ../make-slides.tex ../make-article.tex
	pdflatex -halt-on-error talk.tex && mv talk.pdf $@

talk.pdf : ../00-welcome.pdf
