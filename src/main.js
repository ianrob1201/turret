// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueFire from 'vuefire'
import firebase from 'firebase'
import store from './store'
import VueResource from 'vue-resource'

Vue.config.productionTip = false

// explicit installation required in module environments
Vue.use(VueFire)
Vue.use(VueResource)

const config = {
  apiKey: 'AIzaSyCKH7DVvs-Rpx9pto7X2jVG8c9f05_K21E',
  authDomain: 'turret-a2f8e.firebaseapp.com',
  databaseURL: 'https://turret-a2f8e.firebaseio.com',
  projectId: 'turret-a2f8e',
  storageBucket: '',
  messagingSenderId: '327517409294'
}
const firebaseApp = firebase.initializeApp(config)
export const db = firebase.database()
export const peopleRef = firebaseApp.database().ref().child('people')
console.log("REF")
console.log(peopleRef)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>',
  firebase: {
    people: db.ref('/people')
  }
})
