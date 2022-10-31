import { api } from 'src/boot/axios';
import type { AxiosInstance } from 'axios';
import type { LoginFormData } from 'src/types/Api';

const API_VERSION = process.env.API_VERSION;

export const userLogin = (
  loginFormData: LoginFormData
): Promise<AxiosInstance> => {
  return api.get('api/v1/user-data/')
  // return api.post(`api/${API_VERSION}/accounts/login/`, loginFormData);
  // .then((res) => {
  //   console.log('登入成功');
  // })
  // .catch((error) => {
  //   console.error('🚀 ~ file: system.ts ~ line 15 ~ userLogin ~ error', error)
  //   // response攔截器會先執行，除非你漏接了，才會進到catch
  // });
  // Cookies.set('session', 'test', {
  //   expires: 30,
  //   secure: true,
  // });
};
