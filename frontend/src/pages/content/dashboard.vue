<template>
  <q-page class="row items-center justify-evenly">
    {{ $t('success') }} <br />
    {{ $t('failed') }} <br />
    {{ $t('option') }} <br />
    <q-date v-model="days" multiple />
    <q-card>
      <q-card-section>
        <h5>Socket Result: When create log</h5>
        {{ socket.message }}
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useSocketStore } from 'src/stores/socket';

export default defineComponent({
  name: 'ContentDashboard',
  // components: { ExampleComponent },
  setup() {
    // socket
    const socket = useSocketStore();

    return {
      days: ref(['2019/02/01', '2019/02/10']),
      socket
    };
  },
});
</script>
