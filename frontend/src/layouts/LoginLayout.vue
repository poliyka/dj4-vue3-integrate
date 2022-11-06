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

          <q-btn flat round dense :icon="themeMode" @click="onSwitchMode" />
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
              <q-btn label="Get" type="button" color="accent" @click="onGet" />
              <q-btn
                label="Post"
                type="button"
                color="accent"
                flat
                class="q-ml-sm"
                @click="onPost"
              />
            </div>
          </q-form>
        </q-page>
      </q-page-container>
    </q-layout>
  </div>

</template>

<script lang="ts">
import { defineComponent, ref, reactive } from 'vue';
import { useVuelidate } from '@vuelidate/core';
import { required } from '@vuelidate/validators';
import { useQuasar } from 'quasar';
import { ThemeMode } from 'src/utils/Enum';
// import { Cookies } from 'quasar';
import { useRouter } from 'vue-router';
import { userLogin, userGet, userPost } from 'src/api/system';
import { switchMode } from 'src/utils/Utils';

export default defineComponent({
  name: 'LoginLayout',

  setup() {
    // Third party attr
    const $q = useQuasar();
    const router = useRouter();

    // Define attr
    const themeMode = ref<string>(ThemeMode.DarkMode);
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
      await userLogin(formData);
      const jcsToken = $q.localStorage.getItem('jcsToken');

      // TODO: ajax 後端確認登入狀態
      if (jcsToken) {
        $q.notify({
          color: 'red-5',
          textColor: 'white',
          icon: 'warning',
          message:
            'Access error! Please confirm that your account or password is correct.',
        });
      } else {
        // Cookies.set('session', 'test', {
        //   expires: 30,
        //   secure: true,
        // });
        $q.notify({
          color: 'green-4',
          textColor: 'white',
          icon: 'success',
          position: 'top',
          message: 'Submitted',
        });
        router.push({ name: 'search' });
      }
    };

    const onGet = async (): Promise<void> => {
      await userGet();
    };

    const onPost = async (): Promise<void> => {
      await userPost();
    };

    const onReset = (): void => {
      // Resetting the form.
      formData.username = '';
      formData.password = '';
    };

    const onSwitchMode = (): void => {
      switchMode($q, themeMode);
    };

    return {
      // attr
      formData,
      themeMode,
      // validation
      v$,
      // function
      onSwitchMode,
      onSubmit,
      onReset,
      onGet,
      onPost,
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
  min-height: 30em;
  max-height: 30em;
  min-width: 30em;
  max-width: 30em;
}
</style>



