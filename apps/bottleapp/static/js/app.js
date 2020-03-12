const routes = [
  { path: '', component: Home },
]

const router = new VueRouter({
  routes
});

new Vue({
  router
}).$mount('#app');

