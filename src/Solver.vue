<template lang="pug">
div
    h1 Solver
    ul.list-group
        li.list-group-item.d-flex.justify-content-between.align-items-center(v-for="(element, index) in history")
            span
                code &gt;&gt;&gt; {{element[0]}}
                dl
                    dt Exercise
                    dd(v-html="element[1]")
                    dt Solution
                    dd(v-html="element[2]")
            span.badge.badge-danger(v-on:click="remove_command(index)" v-if="!show_answers") x
    form(v-on:submit="execute_command")
        .form-group.row
            label.col-3.col-form-label Command
            .col-9
                input.form-control.text-monospace(v-model='command')
</template>

<script>
const axios = require('axios').default;
const katex = require('katex');
import 'katex/dist/katex.min.css';

export default {
    name: 'Solver',
    data() {
        if(window.location.hostname == 'localhost') {
            var backend = 'http://localhost:5000/';
        } else {
            var backend = 'https://mathsnuggets.co.uk/_starters/';
        }
        return {
            backend: backend,
            history: [],
            command: 'equation("x^2 - 5*x + 6")',
        };
    },
    methods: {
        remove_command: function(index) {
            this.history.splice(index, 1);
        },
        execute_command: function(event) {
            event.preventDefault();
            var self = this;
            var url = self.backend + 'solver';
            var formData = new FormData();
            formData.set('command', self.command);
            axios.post(url, formData).then(function (response) {
                var data = response.data;
                var options = {displayMode: true, macros: {'\\br': '\\left(#1\\right)'}};
                var exercise = katex.renderToString(data[0], options)
                var solution = katex.renderToString(data[1], options)
                self.history.push([self.command, exercise, solution]);
                self.command = '';
            });
        },
    },
}
</script>
