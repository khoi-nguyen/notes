<template lang="pug">
div
    h1 Starter Generator
    ul.list-group
        li.list-group-item.d-flex.justify-content-between.align-items-center(v-for="(q, index) in questions")
            span(v-html="q[0]")
            span
                span.badge.badge-success.answer.d-none(v-html="q[1]")
                span.badge.badge-danger.answer(v-on:click="remove_question(index)") x
    p(v-if="questions.length > 0")
        button.btn.btn-success(v-on:click="show_answers()") Show answers
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
const host = 'http://localhost:5000/';
import 'katex/dist/katex.min.css';

export default {
    name: 'Starter',
    data() {
        return {
            exerciseList: [],
            question: 'quadratic_equation',
            questions: [],
            n: 1,
        };
    },
    mounted() {
        var self = this;
        axios.get(host).then(function (response) {
            self.exerciseList = response.data;
        });
    },
    methods: {
        add_question: function(event) {
            var self = this;
            var url = host + 'add_question/' + self.question + '/' + self.n;
            axios.get(url).then(function (response) {
                var data = response.data;
                data.forEach(function (element, index) {
                    this[index][0] = katex.renderToString(element[0])
                    this[index][1] = katex.renderToString(element[1])
                }, data);
                self.questions = self.questions.concat(data);
            });
        },
        remove_question: function(index) {
            this.questions.splice(index, 1);
        },
        show_answers: function() {
            var answers = document.getElementsByClassName('answer');
            for(var i = 0; i < answers.length; i++) {
                answers[i].classList.toggle('d-none');
            }
        },
        reset_questions: function() {
            this.questions = [];
        }
    },
}
</script>
