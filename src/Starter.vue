<template lang="pug">
div
    h1 Starter Generator
    ul.list-group
        li.list-group-item.d-flex.justify-content-between.align-items-center(v-for="q in questions")
            span {{q[0]}}
            span.badge.badge-success {{q[1]}}
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
const host = 'http://localhost:5000/';
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
                self.questions.push(response.data)
            });
        }
    },
}
</script>
