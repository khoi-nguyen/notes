<template lang="pug">
.container
    h1 Welcome
    p.lead.
        Hello! My name is Khoi Nguyen and
        I am doing a teacher training programme at the
        #[a(href='https://ox.ac.uk') University of Oxford].
        From August 2020 onwards, I will be teaching mathematics at the
        #[a(href='https://kingscollegeschools.org/madrid/school/') British School of Madrid].
    p.
        Before teaching, I was a web developer
        (which you probably can't tell from this website,
        since I wasn't very good at it) and before that,
        I was a research student at
        #[a(href='https://imperial.ac.uk') Imperial College].
        If you want to see what a bad thesis looks like, click
        #[a(href='https://spiral.imperial.ac.uk/handle/10044/1/44081') here].
    p.
        My greatest pride naturally lies in something I'm not very good at.
        I took part in the
        #[a(href='https://www.youtube.com/watch?v=d12Dgfd09SI') 77#[sup th] Table Tennis Varsity Game]
        as Oxford's fourth player
        (or Cambridge's fifth if you're a glass-half-full type of person).
    hr
    h3 Contact me
    dl
        dt Email
        dd khoi@nguyen.me.uk
        dt Address
        dd.
            St Stephen's House#[br]
            16, Marston St#[br]
            Oxford OX4 1JX#[br]
            United Kingdom
</template>

<script>
export default {
    name: 'Home',
}
</script>
