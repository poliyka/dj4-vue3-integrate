<template>
  <div>
    <q-page class="row items-center">
      <div class="col-4">
        <h5>Pinia Count</h5>
        <p>爺爺今年已經 {{ states.old }} 歲了</p>
        <q-btn
          color="primary"
          label="幫爺爺慶生"
          @click="handleAfterBirthday"
        />
        <h5>Import image</h5>
        <img :src="image" alt="" />
      </div>

      <div class="col-4">
        <h5>I18n</h5>
        {{ $t('success') }} <br />
        {{ $t('failed') }} <br />
        {{ $t('option') }} <br />
      </div>

      <div class="col-4">
        <h5>Date calender</h5>
        <q-date v-model="days" multiple />
      </div>

      <div class="col-4">
        <h5>Chartjs</h5>
        <BarChart />
      </div>

      <div class="col-4">
        <h5>VxeTable</h5>
        <VxeTableExample />
      </div>

      <div class="col-4">
        <q-card>
          <q-card-section>
            <h5>Socket Result: When create log</h5>
            {{ socket.message }}
          </q-card-section>
        </q-card>
      </div>
    </q-page>

  </div>
</template>

<script lang="ts">
import { defineComponent, computed, ref } from 'vue';
import { useQuasar } from 'quasar';
import { watch, reactive } from 'vue';
import { injectStrict, statesKey, genKey } from 'src/utils/Injects';
import BarChart from 'components/chart/BarChart.vue';
import VxeTableExample  from 'components/vxetable/VxeTableExample.vue';

import image from '/icons/favicon-128x128.png';
import { useSocketStore } from 'src/stores/socket';

export default defineComponent({
  name: 'ContentExample',
  components: { BarChart, VxeTableExample},
  setup() {
    const $q = useQuasar();
    const grandpaStates = injectStrict(statesKey);
    const handleAfterBirthday = injectStrict(genKey);
    const socket = useSocketStore();
    const states = reactive({
      old: computed(() => grandpaStates?.value.old),
    });
    async function toggleMode(): Promise<void> {
      $q.dark.set(!$q.dark.isActive);
    }
    watch(
      () => $q.dark.isActive,
      (val) => {
        console.log(val ? 'On dark mode' : 'On light mode');
      }
    );
    return {
      states,
      handleAfterBirthday,
      toggleMode,
      image,
      socket,
      days: ref(['2019/02/01', '2019/02/10']),
    };
  },
});
</script>
