import { createApp } from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import router from './router'; 
import App from "./App";

// set default Django cookies and headers
// Set the Cross Site Request Forgery token to be sent w/ every axios req:
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

// Unmount any previously mounted Vue instance before mounting the new one
const previousApp = document.getElementById("app");
if (previousApp && previousApp.__vue__) {
  previousApp.__vue__.unmount();
}

if (!window.__VUE_INSTANCE__) {
  const app = createApp(App);
  app.use(router);
  app.use(VueAxios, axios);
  app.mount("#app");

  // Flag to prevent duplicate mounting
  window.__VUE_INSTANCE__ = true;
}