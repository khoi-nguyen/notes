<template lang="pug">
div
    nav.navbar.navbar-dark.sticky-top.bg-dark.flex-md-nowrap.p-0.navbar-expand-md
        router-link.navbar-brand.col-sm-3.col-md-2.mr-0(to="/") mathsnuggets
        .collapse.navbar-collapse
            ul.navbar-nav.mr-auto.px-3
                li.nav-item.text-nowrap(v-for="link in links")
                    router-link.nav-link(:to="link.to").
                        #[font-awesome-icon(:icon="link.icon")]
                        {{link.text}}
    .container-fluid
        .row
            .col-md-2.d-none.d-md-block.bg-light.sidebar
                .sidebar-sticky
                    h5.sidebar-heading.text-muted Contribute
                    ul.nav.flex-column
                        li.nav-item
                            a.nav-link(href="https://github.com/khoi-nguyen/teaching").
                                #[font-awesome-icon.text-muted(icon="file-pdf")]
                                Github
                            a.nav-link(href="https://github.com/khoi-nguyen/teaching").
                                #[font-awesome-icon.text-muted(icon="file-pdf")]
                                Issues
                    h5.sidebar-heading.text-muted Build status
                    p
                        img(src="https://github.com/khoi-nguyen/teaching/workflows/Build/badge.svg")
            main.col-md-10.ml-sm-auto.col-lg-10.pt-3.px-4
                router-view
</template>

<script>
const axios = require('axios').default;

export default {
    name: 'App',
    data() {
        return {
            links: [
                {text: 'Home', icon: 'home', to: '/'},
                {text: 'Project', icon: 'tasks', to: '/project'},
                {text: 'Resources', icon: 'chalkboard-teacher', to: '/teaching'},
                {text: 'About', icon: 'address-card', to: '/about'},
                {text: 'Starter Generator', icon: 'tv', to: '/starter'},
            ],
        }
    },
}
</script>

<style>
.sidebar {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    z-index: 100; /* Behind the navbar */
    padding: 0;
    box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
}
.navbar-brand {
    padding-top: .75rem;
    padding-bottom: .75rem;
    font-size: 1rem;
    background-color: rgba(0, 0, 0, .25);
    box-shadow: inset -1px 0 0 rgba(0, 0, 0, .25);
}
body {
}

.feather {
  width: 16px;
  height: 16px;
  vertical-align: text-bottom;
}

/*
 * Sidebar
 */

.sidebar {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100; /* Behind the navbar */
  padding: 0;
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
}

.sidebar-sticky {
  position: -webkit-sticky;
  position: sticky;
  top: 48px; /* Height of navbar */
  height: calc(100vh - 48px);
  padding-top: .5rem;
  overflow-x: hidden;
  overflow-y: auto; /* Scrollable contents if viewport is shorter than content. */
}

.sidebar .nav-link {
  font-weight: 500;
  color: #333;
}

.sidebar .nav-link.active {
  color: #007bff;
}

.sidebar .nav-link:hover .feather,
.sidebar .nav-link.active .feather {
  color: inherit;
}

.sidebar-heading {
  font-size: .85rem;
  text-transform: uppercase;
}

/*
 * Navbar
 */

.navbar-brand {
  padding-top: .75rem;
  padding-bottom: .75rem;
  font-size: 1rem;
  background-color: rgba(0, 0, 0, .25);
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, .25);
}

.navbar .form-control {
  padding: .75rem 1rem;
  border-width: 0;
  border-radius: 0;
}

.form-control-dark {
  color: #fff;
  background-color: rgba(255, 255, 255, .1);
  border-color: rgba(255, 255, 255, .1);
}

.form-control-dark:focus {
  border-color: transparent;
  box-shadow: 0 0 0 3px rgba(255, 255, 255, .25);
}

/*
 * Utilities
 */

.border-top { border-top: 1px solid #e5e5e5; }
.border-bottom { border-bottom: 1px solid #e5e5e5; }
</style>
