DST = /srv/oscarbenedito.com

.PHONY: site server blogroll deploy loc clean

site:
	python3 gensite.py

server: site
	git ls-files | entr make &
	python3 -m http.server --bind localhost --directory _site

blogroll:
	python3 misc/update-blogroll.py

deploy:
	git fetch origin master
	git reset --hard origin/master
	git verify-commit master
	git submodule foreach 'git fetch origin master; git reset --hard $$sha1'
	python3 gensite.py
	rsync --perms --recursive --checksum --delete _site/ $(DST)

loc:
	grep -vE '^[[:space:]]*#|^[[:space:]]*$$|^[[:space:]]*"""' gensite.py | wc -l

clean:
	rm -rf _site
