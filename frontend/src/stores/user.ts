import { defineStore } from 'pinia';
import { reactive } from 'vue';
import avatar from '/imgs/avatar.png';
import type { TUserStore } from 'src/types/Types';

export const useUserStore = defineStore('user', {
  state: () => ({
    // default user
    user: reactive<TUserStore>({
      firstName: 'firstName',
      lastName: 'lastName',
      avatar: avatar,
      username: 'username',
    }),
  }),

  getters: {},

  actions: {},
});
