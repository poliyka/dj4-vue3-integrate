import type { Ref } from 'vue';
import type { QVueGlobals } from 'quasar';
import type { ICsrfTokenHeader } from 'src/types/Types';
import type { AxiosResponse } from 'axios';
import type { LoginFormData } from 'src/types/Api';

export type TSwitchMode = ($q: QVueGlobals, themeMode: Ref<string>) => void;

export type TGetCsrfToken = () => ICsrfTokenHeader;

export type TUserLogin = (
  loginFormData: LoginFormData
) => Promise<AxiosResponse>;
