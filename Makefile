ifeq ($(GITHUB), 1)
START_ENV :=
ENV :=
else
START_ENV := . env/bin/activate;
ENV := env
endif

# Files
MARKDOWN := $(shell find * -regex '^resources.*\.md' | grep -v 'worksheet.md$$')
WORKSHEET_MARKDOWN := $(shell find * -name '*.worksheet.md')
SLIDES := $(MARKDOWN:.md=.pdf)
HANDOUTS := $(MARKDOWN:.md=.handout.pdf)
WORKSHEETS := $(WORKSHEET_MARKDOWN:.md=.pdf)
ANSWERS := $(WORKSHEET_MARKDOWN:.md=.answers.pdf)
DEPENDENCIES := Makefile $(shell find pandoc/*)
MANIM := $(shell ls videos/*.py | grep -v 'base\|manim')
VIDEOS := $(MANIM:.py=)

# Commands
LATEX := pdflatex -interaction=batchmode
PANDOC := pandoc -s --pdf-engine=lualatex --filter ./bin/filter
BEAMER := $(PANDOC) -t beamer --template=./pandoc/templates/beamer.tex
WORKSHEET := $(PANDOC) -t latex --template=./pandoc/templates/worksheet.tex

.PHONY: tests handouts all deploy clean www artifacts slides videos env
.PRECIOUS: $(MARKDOWN:.md=.tex) $(MARKDOWN:.md=.handout.tex) $(WORKSHEETS:.pdf=.tex) $(ANSWERS:.pdf=.tex)

handouts: $(HANDOUTS) $(ANSWERS)

slides: $(SLIDES) $(WORKSHEETS)

tests: $(ENV)
	@$(START_ENV) python3 -m tests.run
	@$(START_ENV) python3 -m tests.generator
	@$(START_ENV) python3 -m flake8

all: handouts slides

frontend: node_modules
	@npm run-script start

backend: $(ENV)
	@$(START_ENV) python3 -m generator.server

www: node_modules $(ENV)
	@$(START_ENV) python3 ./bin/data.py
	@npm run-script build

artifacts:
	@mkdir -p $@
	@rsync -am --include '*/' --include '*.pdf' --exclude '*' . $@

clean:
	@echo Removing all temporary files
	@find resources -type f | grep -v 'md$$' | xargs rm -f

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
	cd $(@D); $(LATEX) $(<F)

node_modules: package-lock.json package.json
	@npm install

videos: $(VIDEOS)

%: %.py $(ENV)
	@grep ^class $< | sed 's/(/ /' | awk '{ print $$2 }' \
		| xargs -I {} $(START_ENV) python3 -m videos.manim $< {}
	@touch $@

env: env/bin/activate

env/bin/activate: requirements.txt
	test -d env || python3 -m venv env
	$(START_ENV) pip install -Ur requirements.txt
	touch env/bin/activate
