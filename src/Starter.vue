<template lang="pug">
div
    #starter
        div
            .row
                .col-md-8.col-lg-10
                    h1
                        input(type='text' placeholder='Lesson Objective')
                    h3 {{date.toDateString()}}
                    .form-group.row#timer
                        label.col-4.col-form-label.col-form-label-sm Timer (seconds)
                        .col-8
                            input.form-control(v-model='time')
                .col-md-4.col-lg-2.text-right
                    BaseTimer(:timeLimit="time")
            .row
                ul.list-group.col
                    li.list-group-item.d-flex.justify-content-between.align-items-center(v-for="(q, index) in questions" v-if="index % 2 == 0")
                        span
                            span {{index + 1}})&nbsp;
                            span(v-html="q[0]")
                            span(v-html="q[1]")
                        span
                            span.badge.badge-success(v-on:click="toggle_show_answer(index)" v-if="!show_answers && !answers.includes(index)") Solution
                            span.text-success(v-html="q[2]" v-on:click="toggle_show_answer(index)" v-if="show_answers || answers.includes(index)")
                            span.badge.badge-danger(v-on:click="remove_question(index)" v-if="!show_answers") x
                ul.list-group.col
                    li.list-group-item.d-flex.justify-content-between.align-items-center(v-for="(q, index) in questions" v-if="index % 2 == 1")
                        span
                            span {{index + 1}})&nbsp;
                            span(v-html="q[0]")
                            span(v-html="q[1]")
                        span
                            span.badge.badge-success(v-on:click="toggle_show_answer(index)" v-if="!show_answers && !answers.includes(index)") Solution
                            span.text-success(v-html="q[2]" v-on:click="toggle_show_answer(index)" v-if="show_answers || answers.includes(index)")
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
                    option(v-for="i in [1, 2, 3, 4, 5, 6, 7, 8, 9]" :value="i") {{i}}
        .from-group.row
            label.col-sm-2.col-form-label.col-form-label-sm Exercise
            .col-sm-10
                select.custom-select(v-model="question")
                    option(v-for="ex in exerciseList" :value="ex.name") {{ex.title}}
        .from-group.row
            label.col-sm-2.col-form-label.col-form-label-sm Level
            .col-sm-10
                select.custom-select(v-model="level")
                    option(v-for="i in [1, 2, 3, 4, 5, 6, 7, 8, 9]" :value="i") {{i}}
        button.btn.btn-primary(type="submit") Add question(s)
    button.btn.btn-success(v-on:click="toggle_fullscreen")#btn-fullscreen Fullscreen
</template>

<script>
const axios = require('axios').default;
const katex = require('katex');
import 'katex/dist/katex.min.css';

import BaseTimer from "./BaseTimer";

export default {
    name: 'Starter',
	components: {
        BaseTimer
	},
    data() {
        if(window.location.hostname == 'localhost') {
            var backend = 'http://localhost:5000/';
        } else {
            var backend = 'https://mathsnuggets.co.uk/_starters/';
        }
        return {
            backend: backend,
            date: new Date(),
            exerciseList: [],
            level: 5,
            question: '',
            questions: [],
            n: 1,
            show_answers: false,
            answers: [],
            time: 300,
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
            var url = self.backend + 'add_question/' + self.question + '/' + self.n + '/' + self.level;
            axios.get(url).then(function (response) {
                var data = response.data;
                data.forEach(function (element, index) {
                    var options = {displayMode: true, macros: {'\\br': '\\left(#1\\right)'}};
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
        toggle_fullscreen: function() {
            var elem = document.getElementById('starter');
            if (elem.requestFullScreen) {
                  elem.requestFullScreen();
            } else if (elem.mozRequestFullScreen) {
                  elem.mozRequestFullScreen();
            } else if (elem.webkitRequestFullScreen) {
                  elem.webkitRequestFullScreen();
            }
        },
        toggle_show_answer: function(index) {
            if(!this.answers.includes(index)) {
                this.answers.push(index);
            } else {
                this.answers.splice(this.answers.indexOf(index), 1);
            }
        },
        toggle_show_answers: function() {
            this.show_answers = !this.show_answers;
            this.answers = [];
        },
        reset_questions: function() {
            this.questions = [];
        }
    },
}
</script>

<style>
h1 input {
    border: 0;
}
#starter:fullscreen {
    background-color: white;
    height: 100vw;
}
#starter:fullscreen > div {
    font-size: 1.5vw;
    margin: auto;
    height: 100vw;
    width: 90vw;
}
#starter:fullscreen h1 {
    font-size: 5vw;
}
#starter:fullscreen h3 {
    font-size: 2.5vw;
}
#starter:fullscreen .badge-danger, #starter:fullscreen .btn-secondary, #starter:fullscreen #timer {
    display: none;
}
</style>
