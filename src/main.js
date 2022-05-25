import {createApp} from 'vue'
import VueChartkick from 'vue-chartkick'
import 'chartkick/chart.js'
import App from './App.vue'


import "./assets/bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import router from './router'
import store from './store'
import axios from 'axios'


createApp(App).use(VueChartkick).use(store).use(router).mount('#app')