<template lang="pug">
div
    h1 {{meta.title}}
    h2 {{meta.subtitle}}
    h3 Changelog
    ul
        li(v-for="commit in commits") {{commit.commit.message}}
    h3 Source code
    pre(v-html="contents")
</template>

<script>
import { reprism, highlight, loadLanguages } from 'reprism';
import markdown from "./markdown.js";
import "prismjs/themes/prism.css";
const axios = require('axios').default;
const resources = require('../data.json');

loadLanguages(markdown);

export default {
    name: 'File',
    data() {
        return {
            contents: '',
            commits: [],
            meta: {title: '', subtitle: ''},
            path: this.$route.params.dir + '/' + this.$route.params.filename,
        }
    },
    mounted() {
        var self = this;
        var url = 'https://api.github.com/repos/khoi-nguyen/notes/contents/';
        this.meta = resources.filter(function (res) {
            return res.path === self.path
        })[0].meta;
        axios.get(url + this.path).then(function (response) {
            let code = atob(response['data']['content']);
            let contents = highlight(code, 'markdown');
            self.contents = contents;
        });

        url = 'https://api.github.com/repos/khoi-nguyen/notes/commits'
        url += '?path=' + this.path
        // Getting commits
        axios.get(url).then(function (response) {
            self.commits = response['data'];
        });
    },
}
</script>
