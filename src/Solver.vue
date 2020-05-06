<template lang="pug">
div#solver
    h1 Solver
    ul.list-group
        li.list-group-item(v-for="(element, index) in history")
            div
                div.input-group.mb-2
                    input.form-control.text-monospace(:value="element[0]" v-on:keyup.enter="execute_command(index, $event)")
                    .input-group-append
                        button.btn.btn-danger(v-on:click="remove_command(index)") x
                dl
                    dt Exercise
                    dd(v-html="element[1]")
                    dt Solution
                    dd(v-html="element[2]")
    form.form-group
        input.form-control.text-monospace(v-model='command' placeholder="Command" v-on:keyup.enter="execute_command(false, $event)")
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
            command: '',
        };
    },
    methods: {
        remove_command: function(index) {
            this.history.splice(index, 1);
        },
        execute_command: function(index, event) {
            event.preventDefault();
            var self = this;
            var url = self.backend + 'solver';
            var formData = new FormData();
            var command = event.currentTarget.value;
            formData.set('command', command);
            axios.post(url, formData).then(function (response) {
                var data = response.data;
                var options = {displayMode: true, macros: {'\\br': '\\left(#1\\right)'}};
                var exercise = katex.renderToString(data[0], options)
                var solution = katex.renderToString(data[1], options)
                if(index === false) {
                    self.history.push([command, exercise, solution]);
                    self.command = '';
                } else {
                    self.history.splice(index, 1, [command, exercise, solution]);
                }
            });
        },
    },
}
</script>

<style>
#solver .list-group input {
    border: 0 !important;
}
#solver input {
    color: #e83e8c !important;
}
</style>
