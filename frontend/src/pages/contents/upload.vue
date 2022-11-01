<template>
  <div
    v-for="(input, index) in state.collection"
    :key="index"
    :class="{
      error: v$.collection.$each.$response.$errors[index].name.length,
    }"
  >
    <input v-model="input.name" type="text" />
    <div
      v-for="error in v$.collection.$each.$response.$errors[index].name"
      :key="error"
    >
      {{ error.$message }}
    </div>
  </div>
</template>

<script lang="ts">
import { helpers, required } from '@vuelidate/validators';
import { useVuelidate } from '@vuelidate/core';
import { reactive } from 'vue';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'uploadPage',
  setup() {
    const rules = {
      collection: {
        $each: helpers.forEach({
          name: {
            required,
          },
        }),
      },
    };
    const state = reactive({
      collection: [{ name: '' }, { name: 'bar' }],
    });
    const v$ = useVuelidate(rules, state);
    return { v$, state };
  },
});
</script>
