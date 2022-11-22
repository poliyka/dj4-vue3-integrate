<template>
  <div
    class="fit row justify-center items-center content-center _dva-login-container"
  >
    <q-layout
      view="lHh lpr lFf"
      container
      class="shadow-2 rounded-borders _dva-login-layout"
    >
      <q-header elevated>
        <q-toolbar>
          <q-avatar>
            <q-icon name="login"></q-icon>
          </q-avatar>

          <q-toolbar-title> DVA System Login </q-toolbar-title>

          <q-btn flat round dense :icon="themeModeIcon" @click="onSwitchMode" />
        </q-toolbar>
      </q-header>

      <q-page-container>
        <q-page padding>
          <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
            <q-input
              filled
              autocomplete
              v-model.trim="formData.username"
              label="Account"
              hint="Email or Phone number"
              lazy-rules
              :rules="[
                (val) => !v$.username.$invalid || `Please insert account`,
              ]"
            />
            <!-- (val) => (val && val.length > 0) || 'Please type something', -->
            <q-input
              filled
              type="password"
              autocomplete
              v-model.trim="formData.password"
              label="Password"
              lazy-rules
              :rules="[
                (val) => !v$.password.$invalid || `Please insert password`,
              ]"
            />

            <!-- <q-toggle v-model="accept" label="I accept the license and terms" /> -->

            <!-- <pre class="language-json">
              {{ v$.username.$invalid }}
            </pre> -->
            <div>
              <q-btn label="Submit" type="submit" color="primary" />
              <q-btn
                label="Reset"
                type="reset"
                color="primary"
                flat
                class="q-ml-sm"
              />
            </div>
          </q-form>
        </q-page>
      </q-page-container>
    </q-layout>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from 'vue';
import { useVuelidate } from '@vuelidate/core';
import { required } from '@vuelidate/validators';
import { useQuasar } from 'quasar';
import { useRouter } from 'vue-router';
import { userLoginApi } from 'src/api/accounts';
import { switchMode } from 'src/utils/Utils';
import { useGlobalStore } from 'src/stores/global';
import { storeToRefs } from 'pinia';

export default defineComponent({
  name: 'LoginLayout',

  setup() {
    // Third party attr
    const $q = useQuasar();
    const router = useRouter();

    // Define attr
    const globalStore = useGlobalStore();
    const { themeModeIcon } = storeToRefs(globalStore);

    const formData = reactive({
      username: '',
      password: '',
    });

    // Validation
    const rules = {
      username: { required },
      password: { required },
    };

    const v$ = useVuelidate(rules, formData);

    // Function
    const onSubmit = async (): Promise<void> => {
      await userLoginApi(formData);

      // 登入成功
      $q.notify({
        color: 'positive',
        textColor: 'white',
        icon: 'check_circle',
        position: 'top',
        message: 'Login success!',
        timeout: 1000,
      });
      // 重新導向到首頁
      router.push({ name: 'example' });
    };

    const onReset = (): void => {
      // Resetting the form.
      formData.username = '';
      formData.password = '';
    };

    return {
      // attr
      formData,
      themeModeIcon,

      // validation
      v$,
      // function
      onSwitchMode: () => switchMode($q, themeModeIcon),
      onSubmit,
      onReset,
    };
  },
});
</script>

<style lang="scss" scoped>
._dva-login-container {
  min-height: 100vh;
}
._dva-login-layout {
  overflow: auto;
  min-height: 25em;
  max-height: 30em;
  min-width: 30em;
  max-width: 30em;
}
</style>
