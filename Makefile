MARKDOWN := $(shell find * -name '*.md' | grep -v '^\(env\|node\)')
DEPENDENCIES := Makefile $(shell find pandoc/*)
TARGETS := $(MARKDOWN:.md=.pdf) $(MARKDOWN:.md=.handout.pdf)
BEAMER := @pandoc -t beamer --pdf-engine=lualatex\
	--template=./pandoc/beamer.tex\
	--filter ./pandoc/pythontex.py\
	--filter ./pandoc/beamer.py\
	--filter ./pandoc/beamer2.py\

all: $(TARGETS)

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
