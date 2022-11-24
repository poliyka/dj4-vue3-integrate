<template>
  <q-card>
    <q-card-section>
      <Bar
        :chartData="chartData"
        :chartOptions="chartOptions"
        :chartId="chartId"
        :width="width"
        :height="height"
        :cssClasses="cssClasses"
        :styles="styles"
        :plugins="plugins"
      />
    </q-card-section>

    <q-card-section class="q-pt-none"> other message on here </q-card-section>
  </q-card>
</template>

<script lang="ts">
import { computed, defineComponent } from 'vue';
import { Bar } from 'vue-chartjs';
import { useGlobalStore } from 'src/stores/global';
import { storeToRefs } from 'pinia';
import { charJSProps } from 'src/utils/Props';
import { getMonthsNamesList } from 'src/utils/Utils';

export default defineComponent({
  name: 'BarChart',
  components: { Bar },
  props: {
    ...charJSProps('bar'),
  },
  setup() {
    const globalStore = useGlobalStore();
    const { chartJSFontColor } = storeToRefs(globalStore);

    const chartData = {
      labels: getMonthsNamesList({ count: 7, short: true }),
      datasets: [
        {
          data: [65, 59, 80, 81, 56, 55, 40],
          borderWidth: 1,
        },
      ],
    };

    // const chartOption = computed()
    const chartOptions = computed(() => {
      return {
        responsive: true,
        plugins: {
          legend: {
            display: false,
          },
          title: {
            display: true,
            text: 'Chart.js Bar Chart',
            color: chartJSFontColor.value,
          },
          autocolors: {
            enabled: true,
            mode: 'data',
            offset: 1,
          },
        },
        scales: {
          y: {
            beginAtZero: true,
            grid: {
              display: false,
            },
            ticks: {
              color: chartJSFontColor.value,
            },
          },
          x: {
            grid: {
              display: false,
            },
            ticks: {
              color: chartJSFontColor.value,
            },
          },
        },
      };
    });

    return {
      chartData,
      chartOptions,
    };
  },
});
</script>
