import { PropType } from 'vue';
import { Plugin } from 'chart.js';
import { TChartJSPlugin } from 'src/types/Types';


export const charJSProps = (type: TChartJSPlugin) => ({
  chartId: {
    type: String,
    default: `${type}-chart`,
  },
  width: {
    type: Number,
    default: 400,
  },
  height: {
    type: Number,
    default: 400,
  },
  cssClasses: {
    default: '',
    type: String,
  },
  styles: {
    type: Object as PropType<Partial<CSSStyleDeclaration>>,
    default: () => {
      return {};
    },
  },
  plugins: {
    type: Array as PropType<Plugin<TChartJSPlugin>[]>,
    default: () => [],
  },
});

