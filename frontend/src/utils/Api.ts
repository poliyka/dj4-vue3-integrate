import { TGetCsrfToken } from 'src/types/Utils';
import { Cookies } from 'quasar';

export const getCsrfToken: TGetCsrfToken = () => {
  return { 'X-CSRFTOKEN': Cookies.get('csrftoken') };
};
