import { defineStore } from 'pinia';
import { reactive } from 'vue';
import type { TUserStore } from 'src/types/Types';

export const useUserStore = defineStore('user', {
  state: () => ({
    // default user
    user: reactive<TUserStore>({
      firstName: '',
      lastName: '',
      avatar: '',
      username: '',
    }),
  }),

  getters: {},

  actions: {
    logout() {
      this.user.firstName = '';
      this.user.lastName = '';
      this.user.avatar = '';
      this.user.username = '';
    },
  },
});
