<template>
  <div>
    <p>{{ title }}</p>
    <ul>
      <li v-for="menu in menus" :key="menu.id" @click="increment">
        {{ menu.id }} - {{ menu.content }}
      </li>
    </ul>
    <p>Count: {{ menuCount }} / {{ meta.totalCount }}</p>
    <p>Active: {{ active ? 'yes' : 'no' }}</p>
    <p>Clicks on menus: {{ clickCount }}</p>
    <q-btn
      color="deep-orange"
      glossy
      label="ChangeMode"
      @click="toggleMode"
      icon="recycle"
    />
    爺爺今年已經 {{ states.old }} 歲了
    <button @click="handleAfterBirthday">幫爺爺慶生結束</button>
    <img :src="image" alt="" />
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, computed, ref, Ref, toRefs } from 'vue';
import { Menu, Meta } from 'src/types/Types';
import { useQuasar } from 'quasar';
import { watch, reactive } from 'vue';
import { injectStrict, statesKey, genKey } from 'src/utils/Injects';

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

function useDisplayMenu(menus: Ref<Menu[]>) {
  const menuCount = computed(() => menus.value.length);
  return { menuCount };
}

export default defineComponent({
  name: 'ExampleComponent',
  props: {
    title: {
      type: String,
      required: true,
    },
    menus: {
      type: Array as PropType<Menu[]>,
      default: () => [],
    },
    meta: {
      type: Object as PropType<Meta>,
      required: true,
    },
    active: {
      type: Boolean,
    },
  },
  setup(props) {
    const { menus } = toRefs(props);
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
      ...useDisplayMenu(menus),
      states,
      handleAfterBirthday,
      toggleMode,
      image,
    };
  },
});
</script>
