everything: slides articles

all :
	for d in [0-9]*; do (if [ -d $$d ]; then cd $$d && make; fi); done

slides:
	cat make-slides.tex setup-base.tex > setup.tex
	$(MAKE) all
	mv *pdf pdf-slides/

articles:
	cat make-article.tex setup-base.tex > setup.tex
	$(MAKE) all
	mv *pdf pdf-articles/

package :
	mkdir /tmp/stats-intro/
	cp -r pdf-slides/*pdf codelab-0[236]/ /tmp/stats-intro/
	(cd /tmp/ && zip -r stats-intro.zip stats-intro/)
	rm -rf /tmp/stats-intro/
