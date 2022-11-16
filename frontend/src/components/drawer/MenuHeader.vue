<template>
  <q-img
    class="absolute-top"
    src="https://cdn.quasar.dev/img/material.png"
    style="height: 150px"
  >
    <div class="absolute-bottom bg-transparent">
      <q-btn round class="q-mb-sm">
        <q-avatar size="56px">
          <img :src="computeAvatar" />
        </q-avatar>

        <DrawerMenuHeaderPopup />
      </q-btn>

      <div class="text-weight-bold">
        {{ userDataState.last_name }}
        {{ userDataState.first_name }}
      </div>
      <div>{{ userDataState.username }}</div>
    </div>
  </q-img>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue';
import { sourcePathControl } from 'src/utils/Utils';
import { getUserDataApi } from 'src/api/system';
import { useAsyncState } from '@vueuse/core';
import { useUserStore } from 'stores/user';
import { storeToRefs } from 'pinia';
import defaultAvatar from '/imgs/avatar.png';
import DrawerMenuHeaderPopup from './MenuHeaderPopup.vue';

export default defineComponent({
  name: 'DrawerMenuHeader',

  components: {
    DrawerMenuHeaderPopup,
  },

  setup() {
    // use store
    const userStore = useUserStore();
    const { user } = storeToRefs(userStore);

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
      userDataState: ASUserData.state,
      userDataIsReady: ASUserData.isReady,
      userDataIsLoading: ASUserData.isLoading,
      computeAvatar,
    };
  },
});
</script>
