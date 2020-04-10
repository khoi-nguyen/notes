import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App';

import About from './About';
import Home from './Home';
import Project from './Project';
import Teaching from './Teaching';
import File from './File';

import { library } from '@fortawesome/fontawesome-svg-core'
import { faFilePdf, faFileAlt, faHome, faChalkboardTeacher, faTasks, faAddressCard } from '@fortawesome/free-solid-svg-icons'
import { faGitAlt } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faFilePdf, faFileAlt, faHome, faChalkboardTeacher, faTasks, faAddressCard, faGitAlt)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(VueRouter);

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.css';

const routes = [
    { path: '/', component: Home },
    { path: '/about', component: About },
    { path: '/project', component: Project },
    { path: '/teaching', component: Teaching },
    { path: '/file', component: File },
    { path: '/file/:dir/:filename', component: File },
]

const router = new VueRouter({
    routes
})

const app = new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
