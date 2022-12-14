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

        <q-select
          v-model="lang"
          :options="langOptions"
          :label="$t('language')"
          dense
          borderless
          emit-value
          map-options
          options-dense
          style="min-width: 150px"
        />

        <q-btn flat round dense :icon="themeModeIcon" @click="onSwitchMode" />
      </q-toolbar>
    </q-header>

    <q-drawer
      behavior="mobile"
      bordered
      show-if-above
      side="left"
      v-model="leftDrawerOpen"
    >
      <!-- left drawer list -->
      <q-scroll-area class="_dva-drawer-scroll-area">
        <q-list padding>
          <DrawerMenuList
            v-for="(m, index) in menu"
            :key="index"
            :index="index"
            v-bind="m"
          />
        </q-list>
      </q-scroll-area>

      <!-- left drawer header -->
      <DrawerMenuHeader />
    </q-drawer>

    <q-page-container>
      <q-page padding>
        <router-view />
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { defineComponent, ref, watch } from 'vue';
import { useMenuStore } from 'stores/menu';
import { useGlobalStore } from 'stores/global';
import { storeToRefs } from 'pinia';

import DrawerMenuList from 'components/drawer/MenuList.vue';
import DrawerMenuHeader from 'components/drawer/MenuHeader.vue';

import { useQuasar } from 'quasar';
import languages from 'quasar/lang/index.json';
import { useI18n } from 'vue-i18n';
import { switchMode } from 'src/utils/Utils';
import { useUserStore } from 'src/stores/user';
import { getUserDataApi } from 'src/api/v1/system';

const appLanguages = languages.filter((lang) =>
  ['zh-TW', 'en-US'].includes(lang.isoName)
);

const langOptions = appLanguages.map((lang) => ({
  label: lang.nativeName,
  value: lang.isoName,
}));

export default defineComponent({
  name: 'MainLayout',

  components: {
    DrawerMenuList,
    DrawerMenuHeader,
  },

  setup() {
    const $q = useQuasar();

    // i18n for app
    const { locale } = useI18n({ useScope: 'global' });

    // i18n for quasar
    const lang = ref($q.lang.isoName);

    watch(lang, (val) => {
      // dynamic import, so loading on demand only
      switch (val) {
        case 'zh-TW':
          import('quasar/lang/zh-TW').then((lang) => {
            $q.lang.set(lang.default);
            locale.value = 'zh-TW';
          });
          break;
        case 'en-US':
          import('quasar/lang/en-US').then((lang) => {
            $q.lang.set(lang.default);
            locale.value = 'en-US';
          });
          break;
      }
    });

    // use store
    const menuStore = useMenuStore();
    const { menu } = storeToRefs(menuStore);
    const globalStore = useGlobalStore();
    const { themeModeIcon } = storeToRefs(globalStore);

    // drawer toggle
    const leftDrawerOpen = ref(false);

    // get userData begin
    const userStore = useUserStore();
    const { user } = storeToRefs(userStore);
    getUserDataApi(user).then((res) => res.data);

    return {
      // i18n
      lang,
      langOptions,

      // use
      menu,
      leftDrawerOpen,

      // theme mode
      themeModeIcon: themeModeIcon,
      onSwitchMode: () => switchMode($q),
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
