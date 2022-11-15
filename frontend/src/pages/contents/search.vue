<template>
  <q-page class="row items-center justify-evenly">
    <example-component
      title="Example component"
      active
      :menus="menus"
      :meta="meta"
    ></example-component>
    <div>
      <q-btn label="Get" type="button" color="accent" @click="onGet" />
    </div>
  </q-page>
</template>

<script lang="ts">
import { Menu, Meta } from 'src/types/Types';
import ExampleComponent from 'components/ExampleComponent.vue';
import { defineComponent, ref } from 'vue';
import { getUserData } from 'src/api/system';

export default defineComponent({
  name: 'IndexPage',
  components: { ExampleComponent },
  setup() {
    const menus = ref<Menu[]>([
      {
        id: 1,
        content: 'ct1',
      },
      {
        id: 2,
        content: 'ct2',
      },
      {
        id: 3,
        content: 'ct3',
      },
      {
        id: 4,
        content: 'ct4',
      },
      {
        id: 5,
        content: 'ct5',
      },
    ]);
    const meta = ref<Meta>({
      totalCount: 1200,
    });

    const onGet = async (): Promise<void> => {
      await getUserData();
    };

    return {
      menus,
      meta,
      onGet,
    };
  },
});
</script>
