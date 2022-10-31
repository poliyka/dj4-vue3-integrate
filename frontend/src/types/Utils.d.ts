import type { Ref } from 'vue';
import type { QVueGlobals } from 'quasar';

export type SwitchMode = ($q: QVueGlobals, themeMode: Ref<string>) => void;
