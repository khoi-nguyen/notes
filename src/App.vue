<template lang="pug">
div
    header
        nav.navbar.navbar-expand-md.navbar-dark.bg-dark.fixed-top
            router-link.navbar-brand(to="/") nguyen.me.uk
            div.collapse.navbar-collapse
                ul.navbar-nav.mr-auto
                    li.nav-item
                        router-link.nav-link(to="/") Home
                    li.nav-item
                        router-link.nav-link(to="/teaching") Teaching resources
    .container
        router-view
</template>

<script>
export default {
    name: 'App',
}
</script>

<style>
body {
    padding-top: 5rem;
}
</style>
