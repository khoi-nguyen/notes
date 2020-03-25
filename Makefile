MARKDOWN := $(shell find * -name '*.md' | grep -v '^\(env\|node\|www\)')
DEPENDENCIES := Makefile $(shell find pandoc/*)
TARGETS := $(MARKDOWN:.md=.pdf) $(MARKDOWN:.md=.handout.pdf)
BEAMER := @pandoc -t beamer --pdf-engine=lualatex\
	--template=./pandoc/beamer.tex\
	--filter ./pandoc/pythontex.py\
	--filter ./pandoc/environments.py\
	--filter ./pandoc/multicols.py

all: $(TARGETS)

deploy: all Makefile
	python ./data.py
	rm -fR www/*
	parcel build index.html --out-dir www --public-url ./ --no-cache
	ls -d */ | grep '^[0-9]' | xargs -I {} cp -R {} www
	rsync -avu --delete www/ khoi@nguyen.me.uk:~/www

clean:
	rm $(TARGETS)

%.handout.pdf: %.md $(DEPENDENCIES)
	@echo Building $@...
	$(BEAMER) -s $< -o $@ -V handout=true

%.tex: %.md $(DEPENDENCIES)
	@echo Building $@...
	$(BEAMER) -s $< -o $@

%.pdf: %.md $(DEPENDENCIES)
	@echo Building $@...
	$(BEAMER) -s $< -o $@
