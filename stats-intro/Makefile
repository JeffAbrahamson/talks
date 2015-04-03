all :
	for d in [0-9]*; do (if [ -d $$d ]; then cd $$d && make; fi); done

package :
	mkdir /tmp/stats-intro/
	cp -r *pdf codelab* /tmp/stats-intro/
	(cd /tmp/ && tar czf stats-intro.tgz stats-intro/)
	rm -rf /tmp/stats-intro/
