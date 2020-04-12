<template lang="pug">
div
    h1 Starter Generator
    ul.list-group
        li.list-group-item.d-flex.justify-content-between.align-items-center(v-for="(q, index) in questions")
            span
                span(v-html="q[0]")
                span(v-html="q[1]")
            span
                span.text-success(v-html="q[2]" v-if="show_answers")
                span.badge.badge-danger(v-on:click="remove_question(index)" v-if="!show_answers") x
    p(v-if="questions.length > 0")
        button.btn.btn-success(v-on:click="toggle_show_answers()" v-if="!show_answers") Show answers
        button.btn.btn-primary(v-on:click="toggle_show_answers()" v-if="show_answers") Hide answers
        button.btn.btn-secondary(v-on:click="reset_questions()") Reset
    hr
    h2 Add questions
    form(v-on:submit="add_question")
        .from-group.row
            label.col-sm-2.col-form-label.col-form-label-sm How many
            .col-sm-10
                select.custom-select(v-model="n")
                    option(v-for="i in [1, 2, 3, 4, 5]" :value="i") {{i}}
        .from-group.row
            label.col-sm-2.col-form-label.col-form-label-sm Exercise
            .col-sm-10
                select.custom-select(v-model="question")
                    option(v-for="ex in exerciseList" :value="ex.name") {{ex.title}}
        button.btn.btn-primary(type="submit") Add question(s)
</template>

<script>
const axios = require('axios').default;
const katex = require('katex');
import 'katex/dist/katex.min.css';

export default {
    name: 'Starter',
    data() {
        if(window.location.hostname == 'localhost') {
            var backend = 'http://localhost:5000/';
        } else {
            var backend = 'https://mathsnuggets.co.uk/_starters/';
        }
        return {
            backend: backend,
            exerciseList: [],
            question: '',
            questions: [],
            n: 1,
            show_answers: false,
        };
    },
    mounted() {
        var self = this;
        axios.get(self.backend).then(function (response) {
            self.exerciseList = response.data;
            self.question = self.exerciseList[0].name;
        });
    },
    methods: {
        add_question: function(event) {
            event.preventDefault();
            var self = this;
            var url = self.backend + 'add_question/' + self.question + '/' + self.n;
            axios.get(url).then(function (response) {
                var data = response.data;
                data.forEach(function (element, index) {
                    var options = {displayMode: true};
                    this[index][0] = element[0];
                    this[index][1] = katex.renderToString(element[1], options)
                    this[index][2] = katex.renderToString(element[2], options)
                }, data);
                self.questions = self.questions.concat(data);
            });
        },
        remove_question: function(index) {
            this.questions.splice(index, 1);
        },
        toggle_show_answers: function() {
            this.show_answers = !this.show_answers;
        },
        reset_questions: function() {
            this.questions = [];
        }
    },
}
</script>
