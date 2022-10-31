import { boot } from 'quasar/wrappers';
import axios, { AxiosInstance } from 'axios';
import { Notify, Cookies } from 'quasar';

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance;
  }
}

// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)

const api = axios.create({
  baseURL: `http://${process.env.BACKEND_HOST}:${process.env.BACKEND_PORT}`,
  headers: {
    'Content-Type': 'application/json; charset=utf-8',
    'X-CSRFTOKEN': Cookies.get('csrftoken'),
  },
  timeout: 20000,
});

//CORS
api.defaults.withCredentials = true;

// On request
api.interceptors.request.use(
  function (config) {
    // Do something before request is sent
    config.headers['Authorization'] = localStorage.getItem('token');
    return config;
  },
  function (error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

// On response
api.interceptors.response.use(
  function (response) {
    // Do something with response data
    return response;
  },
  function (error) {
    Notify.create({
      type: 'positive',
      color: 'positive',
      timeout: 1000,
      position: 'center',
      message: 'Yeah. Data saved. Great Job!',
    });
    if (error.response) {
      switch (error.response.status) {
        case 401:
          console.log('請先登入');
          break;
        case 404:
          console.log('找不到頁面');
          // go to 404 page
          break;
        case 500:
          console.log('程式發生問題');
          // go to 500 page
          break;
        default:
          console.log(error.message);
      }
    }
    if (!window.navigator.onLine) {
      alert('網路出了點問題，請重新連線後重整網頁');
      return;
    }
    return Promise.reject(error);
  }
);

export default boot(({ app }) => {
  // for use inside Vue files (Options API) through this.$axios and this.$api

  app.config.globalProperties.$axios = axios;
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  app.config.globalProperties.$api = api;
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API
});

export { api };
