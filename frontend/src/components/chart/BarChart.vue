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
import { computed, defineComponent, PropType } from 'vue';
import { Bar } from 'vue-chartjs';
import { Plugin } from 'chart.js';
import { useGlobalStore } from 'src/stores/global';
import { storeToRefs } from 'pinia';

export default defineComponent({
  name: 'BarChart',
  components: { Bar },
  props: {
    chartId: {
      type: String,
      default: 'bar-chart',
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
      type: Array as PropType<Plugin<'bar'>[]>,
      default: () => [],
    },
  },
  setup() {
    const globalStore = useGlobalStore();
    const { chartJSFontColor } = storeToRefs(globalStore);

    const MONTHS = [
      'January',
      'February',
      'March',
      'April',
      'May',
      'June',
      'July',
      'August',
      'September',
      'October',
      'November',
      'December',
    ];
    function months(config: any) {
      var cfg = config || {};
      var count = cfg.count || 12;
      var section = cfg.section;
      var values = [];
      var i, value;

      for (i = 0; i < count; ++i) {
        value = MONTHS[Math.ceil(i) % 12];
        values.push(value.substring(0, section));
      }

      return values;
    }

    const chartData = {
      labels: months({ count: 7 }),
      datasets: [
        {
          data: [65, 59, 80, 81, 56, 55, 40],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(255, 205, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(201, 203, 207, 0.2)',
          ],
          borderColor: [
            'rgb(255, 99, 132)',
            'rgb(255, 159, 64)',
            'rgb(255, 205, 86)',
            'rgb(75, 192, 192)',
            'rgb(54, 162, 235)',
            'rgb(153, 102, 255)',
            'rgb(201, 203, 207)',
          ],
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
        },
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              color: chartJSFontColor.value,
            },
          },
          x: {
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
