ifeq ($(OS),Windows_NT)
	MARKDOWN := $(shell dir /b /S *.md | findstr /v /i "\.worksheet\.md$" )
	WORKSHEET_MARKDOWN := $(shell dir /b /S *.worksheet.md)
	DEPENDENCIES := Makefile $(shell dir /b pandoc\\*.md)
	ENV :=
else
	MARKDOWN := $(shell find * -name '*.md' | grep -v '^\(env\|node\|www\|README\)' | grep -v 'worksheet.md$$')
	WORKSHEET_MARKDOWN := $(shell find * -name '*.worksheet.md')
	DEPENDENCIES := Makefile $(shell find pandoc/*)
	ENV := source env/bin/activate;
endif
LATEX := latexmk -silent -lualatex -cd -f
SLIDES := $(MARKDOWN:.md=.pdf)
HANDOUTS := $(MARKDOWN:.md=.handout.pdf)
WORKSHEETS := $(WORKSHEET_MARKDOWN:.md=.pdf)
PANDOC := $(ENV) pandoc -s --pdf-engine=lualatex\
	--filter ./pandoc/pythontex.py\
	--filter ./pandoc/environments.py\
	--filter ./pandoc/multicols.py
BEAMER := $(PANDOC) -t beamer --template=./pandoc/beamer.tex
WORKSHEET := $(PANDOC) -t latex --template=./pandoc/worksheet.tex

.PHONY: tests handouts all deploy clean
.PRECIOUS: $(MARKDOWN:.md=.tex) $(MARKDOWN:.md=.handout.tex) $(WORKSHEETS:.pdf=.tex)

handouts: tests $(HANDOUTS) $(WORKSHEETS)

tests:
	@$(ENV) python ./pandoc/run_test.py

all: tests $(SLIDES) $(HANDOUTS)

deploy: all
	. env/bin/activate; python ./data.py
	parcel build index.html --out-dir www --public-url ./ --no-cache
	ls -d */ | grep '^[0-9]' | xargs -I {} cp -R {} www
	rsync -avu --delete www/ khoi@nguyen.me.uk:~/www
	rm -fR www/*

clean:
	@echo Removing all temporary files
	@find [0-9]* -type f | grep -v '\(md\)$$' | xargs rm

%.worksheet.tex: %.worksheet.md $(DEPENDENCIES)
	@echo Generating worksheet for $@...
	@$(WORKSHEET) -s $< -o $@

%.tex: %.md $(DEPENDENCIES)
	@echo Generating $@...
	@$(BEAMER) -s $< -o $@

%.handout.tex: %.md $(DEPENDENCIES)
	@echo Building $@...
	@$(BEAMER) -s $< -o $@ -V handout=true

%.pdf: %.tex
	@echo Building $@ with LaTeX...
	@$(LATEX) $<

env: env/bin/activate

env/bin/activate: requirements.txt
	test -d env || virtualenv env
	. env/bin/activate; pip install -Ur requirements.txt
	touch env/bin/activate
