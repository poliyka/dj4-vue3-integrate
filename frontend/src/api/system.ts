import { api } from 'src/boot/axios';
// import { Cookies } from 'quasar';
import type { AxiosInstance } from 'axios';
import type { LoginFormData } from 'src/types/Api';
// import { getCsrfToken } from 'src/utils/Api';

const API_VERSION = process.env.API_VERSION;

export const userLogin = (
  loginFormData: LoginFormData
): Promise<AxiosInstance> => {
  // return api.post(
  //   'api/v1/user-data/',
  //   { email: 'test@test.te', username: '1234' },
  //   {
  //     headers: { ...getCsrfToken() },
  //     auth: loginFormData,
  //   }
  // );
  return api.post(`api/${API_VERSION}/accounts/login/`, loginFormData) ;
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
