<template>
  <router-view />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { provide, readonly, ref } from 'vue';
import { statesKey, genKey } from './utils/Injects';

const states = ref({
  name: 'James',
  old: 75,
  //...
});

const handleAfterBirthday = () => {
  states.value.old = states.value.old + 1;
};

export default defineComponent({
  name: 'App',
  setup() {
    provide(statesKey, readonly(states));
    provide(genKey, handleAfterBirthday);
    return {};
  },
});
</script>
