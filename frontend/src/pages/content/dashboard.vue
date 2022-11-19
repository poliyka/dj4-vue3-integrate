<template>
  <q-page class="row items-center justify-evenly">
    {{ $t('success') }} <br />
    {{ $t('failed') }} <br />
    <q-date v-model="days" multiple />
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'ContentDashboard',
  // components: { ExampleComponent },
  setup() {
    return {
      days: ref([ '2019/02/01', '2019/02/10' ])
    };
  },
});
</script>
