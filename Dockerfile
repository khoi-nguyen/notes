FROM archlinux/base

RUN pacman --noconfirm -Syyu
RUN pacman --noconfirm -S\
        grep \
        findutils\
        make\
        npm\
        pandoc\
        python\
        rsync\
        texlive-core\
        texlive-fontsextra\
        texlive-latexextra\
        texlive-pictures

RUN mkluatexfontdb -u
RUN npm install -g parcel-bundler

WORKDIR /teaching

ENTRYPOINT ["make", "-j", "10"]

CMD ["handouts"]
