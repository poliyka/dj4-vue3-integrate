import { boot } from 'quasar/wrappers';
import axios, { AxiosInstance } from 'axios';
import { Notify, QNotifyCreateOptions, LocalStorage, Cookies } from 'quasar';

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
  },
  timeout: 20000,
});

// 在開發環境下才啟用 CORS
// 並直接模擬登入首頁取得 csrf token
if (process.env.DEV) {
  api.defaults.withCredentials = true;
  api.get('', { withCredentials: true });
}

export default boot(({ app, router }) => {

  // On request
  api.interceptors.request.use(
    function (config) {
      // Do something before request is sent
      config.headers['x-csrftoken'] = Cookies.get('csrftoken');
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
      // Show up notify
      const notifyKwargs = {
        type: 'negative',
        color: 'negative',
        timeout: 3000,
        position: 'top',
        message: error.message,
      } as QNotifyCreateOptions;

      if (error.response) {
        switch (error.response.status) {
          case 400:
            Notify.create({ ...notifyKwargs, message: '參數錯誤' });
            break;
          case 401:
            // 當不是 refresh token 作業發生 401 才需要更新 access token 並重發
            // 如果是就略過此刷新 access token 作業，直接不處理(因為 catch 已經攔截處理更新失敗的情況了)
            const refreshTokenUrl = '/api/accounts/token/refresh/';
            const jwtRefreshToken = LocalStorage.getItem('jwtRefreshToken');
            const originalRequest = error.config;

            if (error.config.url !== refreshTokenUrl) {
              return api
                .post(refreshTokenUrl, { refresh: jwtRefreshToken })
                .then((res) => {
                  // [更新 access_token 成功]

                  // 刷新 storage (其他呼叫 api 的地方都會從此處取得新 access_token)
                  LocalStorage.set('jwtToken', res.data.access);
                  LocalStorage.set('jwtRefreshToken', res.data.refresh);

                  // 刷新原始 request 的 access_token
                  originalRequest.cookies =
                    'Bearer ' + res.data.access;

                  // 重送 request (with new access_token)
                  return axios(originalRequest);
                })
                .catch((err) => {
                  // [更新 access_token 失敗] ( e.g. refresh_token 過期無效)
                  LocalStorage.set('jwtToken', null);
                  LocalStorage.set('jwtRefreshToken', null);

                  Notify.create({ ...notifyKwargs, message: '作業逾時或無相關使用授權，請重新登入' });
                  router.push({ name: 'login' });
                  return Promise.reject(err);
                });
            }

            break;
          case 403:
            Notify.create({ ...notifyKwargs, message: '權限不足' });
            break;
          case 404:
            Notify.create({ ...notifyKwargs, message: '找不到相關頁面' });
            // go to 404 page
            break;
          case 500:
            Notify.create({
              ...notifyKwargs,
              message: '網站發生錯誤，請稍後再做嘗試',
            });
            // go to 500 page
            break;
          default:
            Notify.create(notifyKwargs);
        }
      }
      if (!window.navigator.onLine) {
        Notify.create({
          ...notifyKwargs,
          message: '網路出了點問題，請重新連線後重整網頁',
        });
        return;
      }
      return Promise.reject(error);
    }
  );

  // for use inside Vue files (Options API) through this.$axios and this.$api

  app.config.globalProperties.$axios = axios;
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  app.config.globalProperties.$api = api;
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API
});

export { api };
