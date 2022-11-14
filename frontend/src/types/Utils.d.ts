import type { Ref } from 'vue';
import type { QVueGlobals } from 'quasar';
import type { AxiosResponse } from 'axios';
import type { LoginFormData } from 'src/types/Api';
import type { EThemeMode } from 'src/utils/Enum';

export type TSwitchMode = ($q: QVueGlobals, themeMode: Ref<EThemeMode>) => void;

export type TUserLogin = (
  loginFormData: LoginFormData
) => Promise<AxiosResponse>;

// functions
export type HandleAfterBirthday = () => void;
