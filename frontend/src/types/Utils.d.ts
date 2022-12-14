import type { Ref } from 'vue';
import type { QVueGlobals, QNotifyCreateOptions } from 'quasar';
import type { AxiosResponse, AxiosInstance } from 'axios';
import type { LoginFormData, RUserData } from 'src/types/Api';
import type { Router } from 'vue-router';
import type { TMonthsConfig, TUser } from 'src/types/Types';

export type TSwitchMode = ($q: QVueGlobals) => void;

export type TGetUserData = (
  user: Ref<TUser>
) => Promise<AxiosResponse<RUserData>>;

export type TUserLogin = (
  loginFormData: LoginFormData
) => Promise<AxiosResponse>;

export type TUserLogout = () => Promise<AxiosResponse>;

export type HandleAfterBirthday = () => void;

export type TStatusHandler = (
  api: AxiosInstance,
  error: any,
  router: Router,
  errNotifyKw: QNotifyCreateOptions
) => Promise<AxiosResponse> | void;

export type TMonthsList<T> = (months: T[], config?: TMonthsConfig) => T[];

export type TGetMonthsList<T> = (config?: TMonthsConfig) => T[];
