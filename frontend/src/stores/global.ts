import { defineStore } from 'pinia';
import { EThemeModeIcon } from 'src/utils/Enum';


export const useGlobalStore = defineStore('global', {
  state: () => ({
    // 主題顏色 Icon
    themeModeIcon: EThemeModeIcon.LightMode
  }),

  getters: {},

  actions: {},
});
