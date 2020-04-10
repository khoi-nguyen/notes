<template lang="pug">
div
    header
        nav.navbar.navbar-expand-md.navbar-dark.bg-dark.fixed-top
            router-link.navbar-brand(to="/") nguyen.me.uk
            div.collapse.navbar-collapse
                ul.navbar-nav.mr-auto
                    li.nav-item
                        router-link.nav-link(to="/"). 
                            #[font-awesome-icon(icon="home")]
                            Home
                    li.nav-item
                        router-link.nav-link(to="/project").
                            #[font-awesome-icon(icon="tasks")]
                            Project
                    li.nav-item
                        router-link.nav-link(to="/teaching").
                            #[font-awesome-icon(icon="chalkboard-teacher")]
                            Resources
                    li.nav-item
                        a.nav-link(href="https://github.com/khoi-nguyen/teaching").
                            #[font-awesome-icon(:icon="['fab', 'git-alt']")]
                            Github
                    li.nav-item
                        router-link.nav-link(to="/about").
                            #[font-awesome-icon(icon="address-card")]
                            About
    div
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
