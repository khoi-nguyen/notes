FROM python:3.7.1-alpine3.8

ARG PANDOC_V=2.4
ENV PATH /usr/local/texlive/2020/bin/x86_64-linuxmusl:$PATH

RUN apk add --no-cache ca-certificates && update-ca-certificates \
 && wget -O - https://github.com/jgm/pandoc/releases/download/$PANDOC_V/pandoc-$PANDOC_V-linux.tar.gz | \
    tar -xz -C /usr/local/ --strip-components=1 \
 && rm -rf /usr/local/share/man/*

RUN apk add --no-cache perl wget xz \
 && mkdir install-tl \
 && wget -O - http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz | \
    tar -xz -C install-tl --strip-components=1 \
 && printf '%s\n' \
      'selected_scheme scheme-basic' \
      'option_doc 0' \
      'option_src 0' \
    > install-tl/texlive.profile \
 && install-tl/install-tl --profile=install-tl/texlive.profile \
 && tlmgr install \
      collection-latexrecommended \
      collection-latexextra \
      collection-fontsrecommended \
 && rm -rf install-tl \
 && apk del --purge xz

RUN apk --no-cache add\
        make\
        npm\
        rsync

WORKDIR /teaching

ENTRYPOINT ["make", "-j", "10"]

CMD ["handouts"]
