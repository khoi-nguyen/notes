FROM alpine:latest

RUN apk update
RUN apk add -U --repository http://dl-3.alpinelinux.org/alpine/edge/testing \
        pandoc
RUN apk --no-cache add\
        grep\
        make\
        texlive\
        texlive-luatex\
        python3
RUN apk add -U --repository http://dl-3.alpinelinux.org/alpine/edge/community \
        texmf-dist-fontsextra\
        texmf-dist-latexextra\
        texmf-dist-pictures

RUN luaotfload-tool -u

WORKDIR /teaching

ENTRYPOINT ["make", "-j", "10"]

CMD ["handouts"]
