import type { TSwitchMode, TStatusHandler } from 'src/types/Utils';
import { EThemeModeIcon, EChartJSFontColor } from 'src/utils/Enum';
import { LocalStorage, Notify } from 'quasar';
import _ from 'lodash';
import { useGlobalStore } from 'src/stores/global';
import { storeToRefs } from 'pinia';

export const switchMode: TSwitchMode = ($q) => {
  // A function that is used to switch between dark and light mode.
  $q.dark.set(!$q.dark.isActive);
  // global store
  const globalStore = useGlobalStore()
  const { themeModeIcon, chartJSFontColor } = storeToRefs(globalStore);

  if ($q.dark.isActive) {
    themeModeIcon.value = EThemeModeIcon.LightMode;
    chartJSFontColor.value = EChartJSFontColor.White;
  } else {
    themeModeIcon.value = EThemeModeIcon.DarkMode;
    chartJSFontColor.value = EChartJSFontColor.Dark;
  }
};

/**
 * If the environment is development, prepend the base URL to the source path.
 * Because on develop on nodejs server, the source path is not correct
 * We need to prepend the base URL to django server path
 * @param {string} source - The source path.
 * @returns A string
 */
export const sourcePathControl = (
  source: string,
  defaultSource = ''
): string => {
  let path = source;

  if (_.isEmpty(source)) {
    path = defaultSource;
  }

  if (process.env.DEV) {
    const baseURL = `http://${process.env.BACKEND_HOST}:${process.env.BACKEND_PORT}`;
    path = baseURL + path;
  }

  return path;
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
  const refreshTokenUrl = 'api/accounts/token/refresh/';
  const jwtRefreshToken = LocalStorage.getItem('jwtRefreshToken');
  const originalRequest = error.config;
  const excludeUrls = ['api/accounts/logout/'];
  if (
    error.config.url !== refreshTokenUrl &&
    _.indexOf(excludeUrls, error.config.url) === -1
  ) {
    return api
      .post(refreshTokenUrl, { refresh: jwtRefreshToken })
      .then((res) => {
        // [更新 access_token 成功]

        // 刷新 storage (其他呼叫 api 的地方都會從此處取得新 access_token)
        LocalStorage.set('jwtToken', res.data.access);
        LocalStorage.set('jwtRefreshToken', res.data.refresh);

        // 刷新原始 request 的 access_token
        originalRequest.headers.Authorization = 'Bearer ' + res.data.access

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
  } else if (_.indexOf(excludeUrls, error.config.url) > 0) {
    Notify.create({
      ...errNotifyKw,
      message: '網站發生錯誤，請稍後再做嘗試',
    });
  }
};
