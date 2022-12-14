import { InjectionKey, inject } from 'vue';
import type { Ref } from 'vue';
import type { HandleAfterBirthday } from 'src/types/Utils';

interface States {
  name: string;
  old: number;
}

// Prevent inject not define
export function injectStrict<T>(key: InjectionKey<T>, fallback?: T) {
  const resolved = inject(key, fallback);
  if (!resolved) {
    throw new Error(`Could not resolve ${key.description}`);
  }
  return resolved;
}

// Inject keys
export const statesKey: InjectionKey<Ref<States>> = Symbol('Status');

export const genKey: InjectionKey<HandleAfterBirthday> = Symbol('Gen');
