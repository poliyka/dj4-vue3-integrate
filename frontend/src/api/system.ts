import { api } from 'src/boot/axios';
import { LocalStorage } from 'quasar';

import type { TUserLogin } from 'src/types/Utils.d';

const API_VERSION = process.env.API_VERSION;

export const userLogin: TUserLogin = async (loginFormData) => {
  // TODO: 先刪除掉原有的 sessionid
  const res = await api.post(
    `api/${API_VERSION}/accounts/login/`,
    loginFormData
  );
  LocalStorage.set('jcsToken', res.data.key);
  return res;
};

export const userGet = async () => {
  const res = await api.get('api/v1/user-data/');
  console.log('userGet');
  return res;
};

export const userPost = async () => {
  const res = await api.post('api/v1/user-data/', {
    email: 'test',
    username: 'aaa',
  });
  console.log('userPost');
  return res;
};
