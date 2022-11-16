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
            <img :src="computeAvatar" />
          </q-avatar>
          <div class="text-weight-bold">
            {{ userDataState.last_name }}
            {{ userDataState.first_name }}
          </div>
          <div>{{ userDataState.username }}</div>
        </div>
      </q-img>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from 'vue';
import MenuComponent from 'components/sidebar/MenuComponent.vue';
import { useMenuStore } from 'stores/menu';
import { useUserStore } from 'stores/user';
import { storeToRefs } from 'pinia';
import { getUserDataApi } from 'src/api/system';
import { useAsyncState } from '@vueuse/core';
import defaultAvatar from '/imgs/avatar.png';
import { sourcePathControl } from 'src/utils/Utils';

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
    const ASUserData = useAsyncState(
      getUserDataApi(user).then((res) => res.data),
      {
        profile: { avatar: defaultAvatar, birth: '', gender: '' },
        last_login: '',
        username: '',
        first_name: '',
        last_name: '',
        email: '',
      }
    );

    const computeAvatar = computed(() => {
      return sourcePathControl(
        ASUserData.state.value.profile.avatar,
        defaultAvatar
      );
    });

    return {
      user,
      menu,
      leftDrawerOpen,
      userDataState: ASUserData.state,
      userDataIsReady: ASUserData.isReady,
      userDataIsLoading: ASUserData.isLoading,
      computeAvatar: computeAvatar,
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
