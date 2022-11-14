import { api } from 'src/boot/axios';
import { LocalStorage } from 'quasar';

import type { TUserLogin } from 'src/types/Utils.d';

const API_VERSION = process.env.API_VERSION;

export const userLogin: TUserLogin = async (loginFormData) => {
  const res = await api.post(
    'api/accounts/login/',
    loginFormData
  );
  LocalStorage.set('jwtToken', res.data.access_token);
  LocalStorage.set('jwtRefreshToken', res.data.refresh_token);
  return res;
};

export const userGet = async () => {
  const res = await api.get(`api/${API_VERSION}/system/user-data/`);
  console.log('userGet');
  console.log(res.data);
  return res;
};

export const userPost = async () => {
  const res = await api.post(`api/${API_VERSION}/system/user-data/`, {
    email: 'test',
    username: 'aaa',
  });
  console.log('userPost');
  return res;
};
