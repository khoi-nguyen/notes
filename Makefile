MARKDOWN := $(shell find * -name '*.md' | grep -v '^\(env\|node\|www\|README\)' | grep -v 'worksheet.md$$')
WORKSHEET_MARKDOWN := $(shell find * -name '*.worksheet.md')
DEPENDENCIES := env/bin/activate Makefile $(shell find pandoc/*)
ENV := . env/bin/activate;
LATEX := latexmk -silent -lualatex -cd -f
SLIDES := $(MARKDOWN:.md=.pdf)
HANDOUTS := $(MARKDOWN:.md=.handout.pdf)
WORKSHEETS := $(WORKSHEET_MARKDOWN:.md=.pdf)
ANSWERS := $(WORKSHEET_MARKDOWN:.md=.answers.pdf)
PANDOC := $(ENV) pandoc -s\
	--filter ./pandoc/pythontex.py\
	--filter ./pandoc/environments.py\
	--filter ./pandoc/multicols.py
BEAMER := $(PANDOC) -t beamer --template=./pandoc/beamer.tex
WORKSHEET := $(PANDOC) -t latex --template=./pandoc/worksheet.tex

.PHONY: tests handouts all deploy clean init
.PRECIOUS: $(MARKDOWN:.md=.tex) $(MARKDOWN:.md=.handout.tex) $(WORKSHEETS:.pdf=.tex) $(ANSWERS:.pdf=.tex)

handouts: env/bin/activate tests $(HANDOUTS) $(ANSWERS)

tests:
	@$(ENV) python3 ./pandoc/run_test.py

all: $(SLIDES) $(WORKSHEETS) handouts

deploy: all
	. env/bin/activate; python3 ./data.py
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

%.worksheet.answers.tex: %.worksheet.md $(DEPENDENCIES)
	@echo Generating answer sheet for $@...
	@$(WORKSHEET) -V answers=1 -s $< -o $@

%.tex: %.md $(DEPENDENCIES)
	@echo Generating $@...
	@$(BEAMER) -s $< -o $@

%.handout.tex: %.md $(DEPENDENCIES)
	@echo Building $@...
	@$(BEAMER) -s $< -o $@ -V handout=true

%.pdf: %.tex
	@echo Building $@ with LaTeX...
	@$(LATEX) $<

env/bin/activate: requirements.txt
	@echo Setting up virtual environment
	@test -d env || python3 -m venv env
	@$(ENV) pip3 install -Ur requirements.txt
	@touch env/bin/activate
