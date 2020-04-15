<template lang="pug">
div
    .jumbotron
        h1 Welcome to MathsNuggets!
        p.lead.
            Hello and welcome to our website! We are two PGCE students
            at the #[a(href="https://ox.ac.uk") University of Oxford]
            about to embark on a career in teaching.
            You will find here our #[router-link(to="/teaching") teaching resources].
        p.
            We use programming to automate
            as much of the resource creating process as possible.
            For example, exercises are solved by the computer to ensure
            the answers are correct.
            More information can be found on
            #[router-link(to="/project") this page].
</template>

<script>
export default {
    name: 'Home',
}
</script>
