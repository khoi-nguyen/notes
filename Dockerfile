FROM alpine:latest

RUN apk --no-cache add --repository http://dl-3.alpinelinux.org/alpine/edge/testing \
        pandoc
RUN apk --no-cache add\
        grep\
        make\
        npm\
        python3\
        rsync\
        texlive
RUN apk --no-cache add --repository http://dl-3.alpinelinux.org/alpine/edge/community \
        texmf-dist-fontsextra\
        texmf-dist-latexextra\
        texmf-dist-pictures

WORKDIR /teaching

ENTRYPOINT ["make", "-j", "10"]

CMD ["handouts"]
