FROM archlinux/base

RUN pacman --noconfirm -Syyu
RUN pacman --noconfirm -S\
        grep \
        findutils\
        make\
        pandoc\
        python\
        texlive-core\
        texlive-fontsextra\
        texlive-latexextra\
        texlive-pictures

RUN mkluatexfontdb -u

WORKDIR /teaching

ENTRYPOINT ["make", "-j", "10"]

CMD ["handouts"]
