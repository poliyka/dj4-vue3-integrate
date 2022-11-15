import { api } from 'src/boot/axios';
import { LocalStorage } from 'quasar';

import type { TGetUserData } from './../types/Utils.d';
import type { TUserLogin } from 'src/types/Utils.d';
import avatar from '/imgs/avatar.png';

const API_VERSION = process.env.API_VERSION;

/**
 * It sends a POST request to the backend with the login form data
 * If the request is successful, it saves the access and refresh tokens to local storage
 * @param loginFormData - This is the data that is sent to the backend.
 * @returns The response from the API call.
 */
export const userLogin: TUserLogin = async (loginFormData) => {
  const res = await api.post('api/accounts/login/', loginFormData);
  LocalStorage.set('jwtToken', res.data.access_token);
  LocalStorage.set('jwtRefreshToken', res.data.refresh_token);
  return res;
};

export const getUserData: TGetUserData = async (user) => {
  const res = await api.get(`api/${API_VERSION}/system/user-data/`);
  user.value.firstName = res.data.first_name;
  user.value.lastName = res.data.last_name;
  user.value.username = res.data.username;
  user.value.avatar = res.data.profile.avatar ? res.data.profile.avatar : avatar;
  return res;
};
