import type { Ref } from 'vue';
import type { QVueGlobals } from 'quasar';
import type { ICsrfTokenHeader } from 'src/types/Types';

export type TSwitchMode = ($q: QVueGlobals, themeMode: Ref<string>) => void;

export type TGetCsrfToken = () => ICsrfTokenHeader;
