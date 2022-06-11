import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import * as VueGoogleMaps from "vue2-google-maps" // Import package

Vue.config.productionTip = false

Vue.use(VueGoogleMaps, {
  load: {
    key: "AIzaSyACs2jbBXhOIlRnugdswVY--7aiBx_D7Ss",
    libraries: "places",
    region: "KR"
  }
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
