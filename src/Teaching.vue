<template lang="pug">
.container
    h1 Teaching resources
    p.lead.
        You will find my teaching resources on this page.
        Feel free to use them.
    table.table.table-striped.table-hover.table-bordered
        thead.thead-dark
            tr
                th Level
                th Title
                th Last modification
        tbody
            tr(v-for="file in data")
                td {{file.year}}
                td
                    h5 {{file.meta.title}}
                    h6 {{file.meta.subtitle}}
                    ul.list-group.list-group-horizontal
                        li.list-group-item.
                            #[font-awesome-icon(icon="file-alt")]
                            #[router-link(v-bind:to="'/file/' + file.path") Source]
                        li.list-group-item.
                            #[font-awesome-icon(icon="file-pdf")]
                            #[a(v-bind:href="'./' + file.pdf") Slides]
                        li.list-group-item.
                            #[font-awesome-icon(icon="file-pdf")]
                            #[a(v-bind:href="'./' + file.handout") Handout]
                td {{file.modified}}
</template>

<script>
const resources = require('../data.json');

export default {
    name: 'Teaching',
    data() {
        return {data: resources}
    },
}
</script>
