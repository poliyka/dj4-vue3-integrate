import { defineStore } from 'pinia';

export const useMenuStore = defineStore('menu', {
  state: () => ({
    menu: [
      {
        label: 'Search',
        caption: 'Inquire journal details',
        icon: 'fa fa-magnifying-glass',
        path: '/search',
      },
      {
        label: 'Upload',
        caption: 'Upload journal',
        icon: 'fa fa-upload',
        path: '/upload',
      },
      {
        label: 'Delete',
        caption: 'Delete journal (not approve)',
        icon: 'fa fa-trash',
        path: '/delete',
      },
      {
        label: 'Reverse',
        caption: 'Reverse journal (approved)',
        icon: 'fa fa-arrow-rotate-left',
        path: '/reverse',
      },
    ],
  }),

  getters: {
    // doubleCount (state) {
    //   return state.counter * 2;
    // }
  },

  actions: {},
});
