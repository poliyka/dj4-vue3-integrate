<template>
  <q-layout view="lHh Lpr lff">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>DVA Web UI</q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer bordered show-if-above side="left" v-model="leftDrawerOpen">
      <!-- left drawer list -->
      <q-scroll-area class="_dva-drawer-scroll-area">
        <q-list padding>
          <MenuListComponent
            v-for="(m, index) in menu"
            :key="index"
            :index="index"
            v-bind="m"
          />
        </q-list>
      </q-scroll-area>

      <!-- left drawer header -->
      <MenuHeaderComponent />
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useMenuStore } from 'stores/menu';
import { storeToRefs } from 'pinia';

import MenuListComponent from 'src/components/sidebar/MenuListComponent.vue';
import MenuHeaderComponent from 'src/components/sidebar/MenuHeaderComponent.vue';

export default defineComponent({
  name: 'MainLayout',

  components: {
    MenuListComponent,
    MenuHeaderComponent,
  },

  setup() {
    // use store
    const menuStore = useMenuStore();
    const { menu } = storeToRefs(menuStore);

    // drawer toggle
    const leftDrawerOpen = ref(false);

    return {
      menu,
      leftDrawerOpen,
    };
  },
});
</script>

<style lang="scss" scoped>
._dva-drawer-scroll-area {
  height: calc(100% - 150px);
  margin-top: 150px;
}
</style>
