MARKDOWN := $(shell find * -name '*.md' | grep -v '^\(env\|node\|www\|README\)')
DEPENDENCIES := Makefile $(shell find pandoc/*)
TARGETS := $(MARKDOWN:.md=.tex) $(MARKDOWN:.md=.pdf)
HANDOUTS := $(MARKDOWN:.md=.handout.tex) $(MARKDOWN:.md=.handout.pdf)
BEAMER := @. env/bin/activate; pandoc -t beamer --pdf-engine=lualatex\
	--template=./pandoc/beamer.tex\
	--filter ./pandoc/pythontex.py\
	--filter ./pandoc/environments.py\
	--filter ./pandoc/multicols.py

all: $(TARGETS)

deploy: all $(HANDOUTS)
	. env/bin/activate; python ./data.py
	parcel build index.html --out-dir www --public-url ./ --no-cache
	ls -d */ | grep '^[0-9]' | xargs -I {} cp -R {} www
	rsync -avu --delete www/ khoi@nguyen.me.uk:~/www
	rm -fR www/*

clean:
	@echo Removing all temporary files
	@find [0-9]* -type f | grep -v '\(md\)$$' | xargs rm

%.tex: %.md $(DEPENDENCIES)
	@echo Generating $@...
	$(BEAMER) -s $< -o $@

%.handout.tex: %.md $(DEPENDENCIES)
	@echo Building $@...
	$(BEAMER) -s $< -o $@ -V handout=true

%.pdf: %.tex
	@echo Building $@ with LaTeX...
	@latexmk -silent -lualatex -cd $<

env: env/bin/activate

env/bin/activate: requirements.txt
	test -d env || virtualenv env
	. env/bin/activate; pip install -Ur requirements.txt
	touch env/bin/activate
