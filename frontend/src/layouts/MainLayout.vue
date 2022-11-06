<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>DVA Web UI</q-toolbar-title>

        <div>Current User Component</div>
      </q-toolbar>
    </q-header>

    <q-drawer bordered show-if-above side="left" v-model="leftDrawerOpen">
      <q-list>
        <q-item-label header> Menu </q-item-label>

        <MenuComponent
          v-for="(m, index) in menu"
          :key="index"
          :index="index"
          v-bind="m"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import MenuComponent from 'components/sidebar/MenuComponent.vue';
import { useMenuStore } from 'stores/menu';
import { storeToRefs } from 'pinia';

export default defineComponent({
  name: 'MainLayout',

  components: {
    MenuComponent,
  },

  setup() {
    const menuStore = useMenuStore();
    const { menu } = storeToRefs(menuStore);
    const leftDrawerOpen = ref(false);

    return {
      menu: menu,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },
});
</script>
