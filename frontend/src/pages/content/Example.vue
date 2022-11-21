<template>
  <div>
    <q-page class="row items-center justify-evenly" height="50">
      <div>
        <h5>pinia Count</h5>
        <p>Clicks on menus: {{ clickCount }}</p>
        <p>爺爺今年已經 {{ states.old }} 歲了</p>
        <button @click="handleAfterBirthday">幫爺爺慶生結束</button>
      </div>

      <div>
        <h5>Toggle mode</h5>
        <q-btn
          color="deep-orange"
          glossy
          label="ToggleMode"
          @click="toggleMode"
          icon="recycle"
        />
      </div>

      <div>
        <h5>Import image</h5>
        <img :src="image" alt="" />
      </div>
    </q-page>

    <q-page class="row items-center justify-evenly">
      <div>
        <h5>i18n</h5>
        {{ $t('success') }} <br />
        {{ $t('failed') }} <br />
        {{ $t('option') }} <br />
      </div>

      <div>
        <h5>date calender</h5>
        <q-date v-model="days" multiple />
      </div>

      <div>
        <h5>Chartjs</h5>
        <BarChart />
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

import image from '/icons/favicon-128x128.png';

interface Student {
  firstName: string;
  lastName: string;
  year: number;
  id: number;
}

let st1: Student = {
  firstName: 'James',
  lastName: 'aa',
  year: 123,
  id: 1,
};

let st2: Student = {
  firstName: 'James',
  lastName: 'aa',
  year: 123,
  id: 2,
};

interface IStudentRecord {
  [key: string]: Student;
}

let st: IStudentRecord = { '001': st1, '002': st2 };

console.log(st);

function useClickCount() {
  const clickCount = ref(0);
  function increment() {
    clickCount.value += 1;
    return clickCount.value;
  }

  return { clickCount, increment };
}

// function useDisplayMenu(menus: Ref<Menu[]>) {
//   const menuCount = computed(() => menus.value.length);
//   return { menuCount };
// }

export default defineComponent({
  name: 'ContentExample',
  components: { BarChart },
  setup() {
    const $q = useQuasar();
    const grandpaStates = injectStrict(statesKey);
    const handleAfterBirthday = injectStrict(genKey);
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
      ...useClickCount(),
      states,
      handleAfterBirthday,
      toggleMode,
      image,
      days: ref(['2019/02/01', '2019/02/10']),
    };
  },
});
</script>
