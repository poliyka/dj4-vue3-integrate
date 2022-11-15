import type { TStatusHandler } from './../types/Utils.d';
import type { TSwitchMode } from 'src/types/Utils';
import { EThemeMode } from 'src/utils/Enum';
import { LocalStorage, Notify } from 'quasar';
import _ from 'lodash';

export const switchMode: TSwitchMode = ($q, themeMode) => {
  // A function that is used to switch between dark and light mode.
  $q.dark.set(!$q.dark.isActive);
  if ($q.dark.isActive) {
    themeMode.value = EThemeMode.DarkMode;
  } else {
    themeMode.value = EThemeMode.LightMode;
  }
};

export const status400Handler: TStatusHandler = (
  api,
  error,
  router,
  errNotifyKw
) => {
  // A function that is used to handle 400 errors.
  // 排除不是 typeof dictionary 的錯誤
  if (!_.isPlainObject(error.response?.data)) {
    Notify.create({ ...errNotifyKw, message: '參數錯誤' });
  }

  // 確認是否為帳號密碼錯誤
  if (_.has(error.response.data, 'non_field_errors')) {
    Notify.create({ ...errNotifyKw, message: '帳號或密碼錯誤' });
  }
};

/**
 * It will try to refresh the access token if the request is not the refresh token request
 * @param api - the axios instance
 * @param error - The error object that was thrown
 * @param router - Vue Router instance
 * @param errNotifyKw - An object that contains the keyword arguments for the Notify.create() function.
 * @returns axios response or void
 */
export const status401Handler: TStatusHandler = (
  api,
  error,
  router,
  errNotifyKw
) => {
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
        originalRequest.cookies = 'Bearer ' + res.data.access;

        // 重送 request (with new access_token)
        return api(originalRequest);
      })
      .catch((err) => {
        // [更新 access_token 失敗] ( e.g. refresh_token 過期無效)
        LocalStorage.remove('jwtToken');
        LocalStorage.remove('jwtRefreshToken');

        Notify.create({
          ...errNotifyKw,
          message: '作業逾時或無相關使用授權，請重新登入',
        });
        router.push({ name: 'login' });
        return Promise.reject(err);
      });
  }
};
