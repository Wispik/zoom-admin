const mainApp = {
  delimiters: ['[[', ']]'],
  data() {
    return {
      cbSelectAll: false
    }
  }
}

Vue.createApp(mainApp).mount('#mainApp')