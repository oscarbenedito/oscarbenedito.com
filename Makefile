DEST = /srv/oscarbenedito.com

.PHONY: default deploy blogroll clean

default:
	@echo "No default target, please choose one: deploy, blogroll, clean"
	@exit 2

deploy: clean
	git fetch origin master
	git reset --hard origin/master
	git verify-commit master
	hugo
	rm -f public/index.xml
	rsync --perms --recursive --checksum --delete public/ $(DEST)

blogroll: data/blogroll.json

data/blogroll.json: blogroll.ompl
	./create-blogroll.py blogroll.ompl > data/blogroll.json

clean:
	rm -rf public resources
