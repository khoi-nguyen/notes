<template lang="pug">
div
    h1 Starter Generator
    h2 Add questions
    form
        .from-group.row
            label.col-sm-2.col-form-label.col-form-label-sm How many
            .col-sm-10
                select.custom-select
                    option(v-for="n in [1, 2, 3, 4, 5]" :value="n") {{n}}
        .from-group.row
            label.col-sm-2.col-form-label.col-form-label-sm Exercise
            .col-sm-10
                select.custom-select
                    option(v-for="ex in exerciseList" :value="ex.name") {{ex.title}}
        button.btn.btn-primary(type="submit") Add question(s)
</template>

<script>
export default {
    name: 'Starter',
    data() {
        return {
            exerciseList: [
                {
                    name: 'quadratic_equation',
                    title: 'Quadratic Equation',
                }
            ],
        };
    },
}
</script>
