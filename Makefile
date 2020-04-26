# Files
MARKDOWN := $(shell find * -regex '^resources.*\.md' | grep -v 'worksheet.md$$')
WORKSHEET_MARKDOWN := $(shell find * -name '*.worksheet.md')
SLIDES := $(MARKDOWN:.md=.pdf)
HANDOUTS := $(MARKDOWN:.md=.handout.pdf)
WORKSHEETS := $(WORKSHEET_MARKDOWN:.md=.pdf)
ANSWERS := $(WORKSHEET_MARKDOWN:.md=.answers.pdf)
DEPENDENCIES := Makefile $(shell find pandoc/*)

# Commands
LATEX := pdflatex -interaction=batchmode
PANDOC := pandoc -s --pdf-engine=lualatex --filter ./bin/filter
BEAMER := $(PANDOC) -t beamer --template=./pandoc/beamer.tex
WORKSHEET := $(PANDOC) -t latex --template=./pandoc/worksheet.tex

.PHONY: tests handouts all deploy clean www artifacts slides
.PRECIOUS: $(MARKDOWN:.md=.tex) $(MARKDOWN:.md=.handout.tex) $(WORKSHEETS:.pdf=.tex) $(ANSWERS:.pdf=.tex)

handouts: $(HANDOUTS) $(ANSWERS)

slides: $(SLIDES) $(WORKSHEETS)

tests:
	@python3 -m tests.run

all: handouts slides

frontend: node_modules
	@npm run-script start

backend:
	@python3 -m generator.server

www: node_modules
	@python3 ./bin/data.py
	@npm run-script build

artifacts:
	@mkdir -p $@
	@rsync -am --include '*/' --include '*.pdf' --exclude '*' . $@

clean:
	@echo Removing all temporary files
	@find resources -type f | grep -v 'md$$' | xargs rm

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
