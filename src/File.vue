<template lang="pug">
div
    .container
        h1 {{meta.title}}
        h2 {{meta.subtitle}}
        hr
        h3 Changelog
        dl
            div(v-for="commit in commits")
                dt.
                    #[span.text-muted {{commit.commit.author.date.substr(0, 10)}}]
                    #[small by {{commit.commit.author.name}}]
                dd.
                    #[a(:href="commit.html_url") {{commit.commit.message}}]
        hr
    h3 Source code
    .row
        .col-md-6
            pre(v-html="contents")
        .col-md-6
            object(:data="handout" type="application/pdf" width="100%" height="100%")
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
        var path = 'resources/' + this.$route.params.dir + '/' + this.$route.params.filename
        var data = resources.filter(function (res) {
            return res.path === path
        });
        var handout = data[0].handout;
        var meta = data[0].meta;
        return {
            contents: '',
            commits: [],
            handout: './' + handout,
            meta: meta,
            path: path,
        }
    },
    mounted() {
        var self = this;
        var url = 'https://api.github.com/repos/khoi-nguyen/teaching/contents/';
        axios.get(url + this.path).then(function (response) {
            let code = atob(response['data']['content']);
            let contents = highlight(code, 'markdown');
            self.contents = contents;
        });

        url = 'https://api.github.com/repos/khoi-nguyen/teaching/commits'
        url += '?path=' + this.path
        // Getting commits
        axios.get(url).then(function (response) {
            self.commits = response['data'].slice(0, 5);
        });
    },
}
</script>
