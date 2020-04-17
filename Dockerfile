FROM python:3.8.2-alpine3.11

ENV PATH /usr/local/texlive/2020/bin/x86_64-linuxmusl:$PATH

RUN wget -O - https://github.com/jgm/pandoc/releases/download/2.9.2.1/pandoc-2.9.2.1-linux-amd64.tar.gz| \
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
      cc-icons \
      collection-latexrecommended \
      collection-latexextra \
      collection-fontsrecommended \
      fontawesome \
      latexmk \
 && rm -rf install-tl

RUN apk --no-cache add make npm rsync
RUN apk del --purge wget xz

WORKDIR /teaching

ENTRYPOINT ["make", "-j", "10"]

CMD ["handouts"]
