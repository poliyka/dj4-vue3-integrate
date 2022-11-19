import { defineStore } from 'pinia';

export const useMenuStore = defineStore('menu', {
  state: () => ({
    menu: [
      {
        label: 'Dashboard',
        caption: 'Show all monitor items',
        icon: 'dashboard',
        path: '/dashboard',
      },
      {
        label: 'Schedule',
        caption: 'Plan up schedule',
        icon: 'format_list_bulleted_add',
        path: '/schedule',
      },
      {
        label: 'jobs',
        caption: 'Plan up jobs',
        icon: 'work_history',
        path: '/jobs',
      },
      {
        label: 'History',
        caption: 'Show all history',
        icon: 'history',
        path: '/history',
      },
    ],
  }),

  getters: {
  },

  actions: {},
});
