FROM python:3.8.2-slim-buster

ENV PATH /usr/local/texlive/2020/bin/x86_64-linux:$PATH

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      npm \
      perl \
      rsync \
      wget \
 && wget -O - https://github.com/jgm/pandoc/releases/download/2.9.2.1/pandoc-2.9.2.1-linux-amd64.tar.gz| \
    tar -xz -C /usr/local/ --strip-components=1 \
 && rm -rf /usr/local/share/man/* \
 &&  mkdir install-tl \
 && wget -O - http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz | \
    tar -xz -C install-tl --strip-components=1 \
 && printf '%s\n' \
      'selected_scheme scheme-basic' \
      'option_doc 0' \
      'option_src 0' \
    > install-tl/texlive.profile \
 && install-tl/install-tl --profile=install-tl/texlive.profile \
 && tlmgr install \
      ccicons \
      collection-latexrecommended \
      collection-latexextra \
      collection-fontsrecommended \
      fira \
      fontawesome \
 && rm -rf install-tl \
 && apt-get -y remove wget perl \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

WORKDIR /teaching

ENTRYPOINT ["make", "-j", "10"]

CMD ["handouts"]
