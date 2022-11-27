import { defineStore } from 'pinia';
import { EThemeModeIcon, EChartJSFontColor } from 'src/utils/Enum';
import type { QVueGlobals } from 'quasar';
import { getCssVar } from 'quasar'

export const useGlobalStore = defineStore('global', {
  state: () => ({
    // 主題顏色 Icon
    themeModeIcon: EThemeModeIcon.LightMode,
    // ChartJS Theme mode
    chartJSFontColor: EChartJSFontColor.White,
    vxeTableFontColor: getCssVar('primary'),
    vxeTableBgColor: getCssVar('dark'),
  }),

  getters: {},

  actions: {
    // 切換主題
    toggleThemeMode($q: QVueGlobals) {
      if ($q.dark.isActive) {
        this.themeModeIcon = EThemeModeIcon.LightMode;
        this.chartJSFontColor = EChartJSFontColor.White;
        this.vxeTableBgColor = getCssVar('dark');
      } else {
        this.themeModeIcon = EThemeModeIcon.DarkMode;
        this.chartJSFontColor = EChartJSFontColor.Dark;
        this.vxeTableBgColor = 'white';
      }
    },
    headerCellStyle() {
      return {
        color: this.vxeTableFontColor,
        background: this.vxeTableBgColor,
      };
    },
    rowStyle() {
      return {
        color: this.vxeTableFontColor,
        background: this.vxeTableBgColor,
      };
    },
    cellStyle() {
      return {
        color: this.vxeTableFontColor,
        background: this.vxeTableBgColor,
      };
    },
  },
});
