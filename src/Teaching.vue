<template lang="pug">
div
    h1 Teaching resources
    p.lead.
        You will find my teaching resources on this page.
        Feel free to use them.
    table.table.table-striped.table-hover.table-bordered
        thead.thead-dark
            tr
                th Level
                th Title
        tbody
            tr(v-for="file in data")
                td {{file.year}}
                td
                    h5 {{file.meta.title}}
                    h6 {{file.meta.subtitle}}
                    h6.text-muted Last modified on {{file.modified}}
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
                        li.list-group-item(v-if="file.worksheet").
                            #[font-awesome-icon(icon="file-pdf")]
                            #[a(v-bind:href="'./' + file.worksheet") Worksheet]
                        li.list-group-item(v-if="file.answers").
                            #[font-awesome-icon(icon="file-pdf")]
                            #[a(v-bind:href="'./' + file.answers") Answers]
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
