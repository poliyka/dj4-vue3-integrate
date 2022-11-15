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

        <div>Current User Component</div>
      </q-toolbar>
    </q-header>

    <q-drawer bordered show-if-above side="left" v-model="leftDrawerOpen">
      <!-- left drawer list -->
      <q-scroll-area class="_dva-drawer-scroll-area">
        <q-list padding>
          <MenuComponent
            v-for="(m, index) in menu"
            :key="index"
            :index="index"
            v-bind="m"
          />
        </q-list>
      </q-scroll-area>

      <!-- left drawer header -->
      <q-img
        class="absolute-top"
        src="https://cdn.quasar.dev/img/material.png"
        style="height: 150px"
      >
        <div class="absolute-bottom bg-transparent">
          <q-avatar size="56px" class="q-mb-sm">
            <img :src="user.avatar" />
          </q-avatar>
          <div class="text-weight-bold">
            {{ user.lastName }} {{ user.firstName }}
          </div>
          <div>{{ user.username }}</div>
        </div>
      </q-img>
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
import { useUserStore } from 'stores/user';
import { storeToRefs } from 'pinia';
import { getUserData } from 'src/api/system';

export default defineComponent({
  name: 'MainLayout',

  components: {
    MenuComponent,
  },

  setup() {

    // use store
    const menuStore = useMenuStore();
    const userStore = useUserStore();
    const { menu } = storeToRefs(menuStore);
    const { user } = storeToRefs(userStore);

    // drawer toggle
    const leftDrawerOpen = ref(false);

    // get userData on beginning
    getUserData(user);

    return {
      user,
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
