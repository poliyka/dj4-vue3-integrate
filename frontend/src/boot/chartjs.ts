import { boot } from 'quasar/wrappers';

// import all the things on the chart.js library not registerables
import {
  Chart as ChartJS,
  registerables
} from 'chart.js';

import autocolors from 'chartjs-plugin-autocolors';

ChartJS.register(
  ...registerables,
  autocolors
);

export default boot(({ app }) => {
  // for use inside Vue files (Options API) through this.$axios and this.$api

  app.config.globalProperties.$ChartJS = ChartJS;
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API
});

export { ChartJS };
