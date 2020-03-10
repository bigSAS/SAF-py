console.log('sas kodzi !!!')

var app = new Vue({
  template: '<div>{{ msg }}</div>',
  data: function () {
    return {
      msg: 'sas kodzi'
    }
  }
}).$mount('#app')

