ifeq ($(NOENV), 1)
START_ENV :=
ENV :=
else
START_ENV := . env/bin/activate;
ENV := env/bin/activate
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
TEX := $(MARKDOWN:.md=.tex) $(MARKDOWN:.md=.handout.tex) $(WORKSHEETS:.pdf=.tex) $(ANSWERS:.pdf=.tex)
PDF := $(TEX:.tex=.pdf)

# Commands
LATEX := pdflatex -interaction=batchmode
PANDOC := pandoc -s --filter ./bin/filter
BEAMER := $(PANDOC) -t beamer --template=./pandoc/templates/beamer.tex
WORKSHEET := $(PANDOC) -t latex --template=./pandoc/templates/worksheet.tex

.PHONY: tests handouts all deploy clean www artifacts slides videos env format docker
.PRECIOUS: $(addprefix tmp/, $(TEX) $(PDF))

handouts: $(HANDOUTS) $(ANSWERS)

slides: $(SLIDES) $(WORKSHEETS)

tests: $(ENV) format
	@$(START_ENV) coverage run -m pytest tests/
	@$(START_ENV) coverage xml

all: handouts slides

frontend: node_modules
	@$(START_ENV) python3 ./bin/data.py
	@npm run-script start

backend: $(ENV)
	@$(START_ENV) python3 -m generator.server

docker:
	docker build -t teaching .
	docker tag teaching bknguyen/teaching
	docker push bknguyen/teaching

www: node_modules $(ENV)
	@$(START_ENV) python3 ./bin/data.py
	@npm run-script build

artifacts:
	@mkdir -p $@
	@rsync -am --include '*/' --include '*.pdf' --exclude '*' . $@

clean:
	@echo Removing all temporary files
	@find resources -type f | grep -v 'md$$' | xargs rm -f
	@rm -fR tmp/ node_modules/ env/ dist/

tmp/%.worksheet.tex: %.worksheet.md $(ENV) $(DEPENDENCIES)
	@mkdir -p $(@D)
	@echo Generating worksheet for $@...
	@$(WORKSHEET) -s $< -o $@

tmp/%.worksheet.answers.tex: %.worksheet.md $(ENV) $(DEPENDENCIES)
	@mkdir -p $(@D)
	@echo Generating answer sheet for $@...
	@$(WORKSHEET) -V answers=1 -s $< -o $@

tmp/%.tex: %.md $(ENV) $(DEPENDENCIES)
	@mkdir -p $(@D)
	@echo Generating $@...
	@$(BEAMER) -s $< -o $@

tmp/%.handout.tex: %.md $(ENV) $(DEPENDENCIES)
	@mkdir -p $(@D)
	@echo Generating $@...
	@$(BEAMER) -s $< -o $@ -V handout=true

resources/%.pdf: tmp/resources/%.pdf
	@cp $< $@

%.pdf: %.tex
	@echo Building $@ with LaTeX...
	@cd $(<D); $(LATEX) $(<F)

node_modules: package-lock.json package.json
	@npm install

videos: $(VIDEOS)

%: %.py $(ENV)
	@grep ^class $< | sed 's/(/ /' | awk '{ print $$2 }' \
		| xargs -I {} $(START_ENV) python3 -m videos.manim $< {}
	@touch $@

env: env/bin/activate

env/bin/activate: requirements.txt
	@test -d env || python3 -m venv env
	@$(START_ENV) pip3 install -Ur requirements.txt
	@touch env/bin/activate

format: $(ENV)
	@$(START_ENV) black .
	@$(START_ENV) python3 -m flake8
