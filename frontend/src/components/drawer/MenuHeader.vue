<template>
  <q-img
    class="absolute-top"
    src="https://cdn.quasar.dev/img/material.png"
    style="height: 150px"
  >
    <div class="absolute-bottom bg-transparent">
      <q-btn round class="q-mb-sm">
        <q-avatar size="56px">
          <img :src="user.profile.avatar" />
        </q-avatar>

        <DrawerMenuHeaderPopup />
      </q-btn>

      <div class="text-weight-bold">
        {{ user.lastName }}
        {{ user.firstName }}
      </div>
      <div>{{ user.username }}</div>
    </div>
  </q-img>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useUserStore } from 'stores/user';
import { storeToRefs } from 'pinia';
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

    return {
      user,
    };
  },
});
</script>
