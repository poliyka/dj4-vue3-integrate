import { defineStore } from 'pinia';
import { EThemeModeIcon, EChartJSFontColor } from 'src/utils/Enum';


export const useGlobalStore = defineStore('global', {
  state: () => ({
    // 主題顏色 Icon
    themeModeIcon: EThemeModeIcon.LightMode,
    // ChartJS Theme mode
    chartJSFontColor: EChartJSFontColor.White,
  }),

  getters: {},

  actions: {},
});
