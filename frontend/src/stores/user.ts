import { defineStore } from 'pinia';
import type { TUser } from 'src/types/Types';
import _ from 'lodash';

const user: TUser = {
  profile: { avatar: '', birth: '', gender: '' },
  lastLogin: '',
  username: '',
  firstName: '',
  lastName: '',
  email: '',
};

export const useUserStore = defineStore('user', {
  state: () => ({
    // default user
    user: _.cloneDeep(user),
  }),

  getters: {},

  actions: {
    logout() {
      this.user = _.cloneDeep(user);
    },
  },
});
