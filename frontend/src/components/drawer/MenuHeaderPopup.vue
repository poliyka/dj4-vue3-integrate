<template>
  <q-menu transition-show="flip-right" transition-hide="flip-left">
    <div class="row no-wrap q-pa-md">
      <div class="column">
        <div class="text-h6 q-mb-md">Settings</div>
        <q-list style="min-width: 200px">
          <q-item clickable v-close-popup>
            <q-item-section>editProfile</q-item-section>
          </q-item>
          <q-item clickable v-close-popup>
            <q-item-section>resetPassword</q-item-section>
          </q-item>
          <q-item clickable v-close-popup @click="onGetUserData">
            <q-item-section>getUserData</q-item-section>
          </q-item>
        </q-list>
      </div>

      <q-separator vertical inset class="q-mx-lg" />

      <div class="column items-center">
        <q-avatar size="72px">
          <img :src="user.profile.avatar" />
        </q-avatar>

        <div class="text-subtitle1 q-mt-md q-mb-xs">
          {{ user.lastName }} {{ user.firstName }}
        </div>

        <q-btn
          color="primary"
          label="Logout"
          push
          size="sm"
          v-close-popup
          @click="onUserLogout"
        />
      </div>
    </div>
  </q-menu>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useUserStore } from 'stores/user';
import { storeToRefs } from 'pinia';
import { userLogoutApi } from 'src/api/accounts';
import { getUserDataApi } from 'src/api/v1/system';
import { useRouter } from 'vue-router';
import { Notify } from 'quasar';

export default defineComponent({
  name: 'DrawerMenuHeaderPopup',
  setup() {
    // use store
    const userStore = useUserStore();
    const { user } = storeToRefs(userStore);
    const router = useRouter();

    // function
    const onUserLogout = () => {
      userLogoutApi().then(() => {
        userStore.logout();
        router.push({ name: 'login' });
      });
    };

    const onGetUserData = () => {
      getUserDataApi(user).then((res) => {
        Notify.create({
          message: JSON.stringify(res.data),
          color: 'positive',
          position: 'top',
        });
      })
    };

    return {
      user,
      onUserLogout,
      onGetUserData,
    };
  },
});
</script>
