<template>
  <q-item clickable v-ripple :active="active" :to="path">
    <q-item-section avatar>
      <q-icon :name="icon" />
    </q-item-section>

    <q-item-section>
      <q-item-label>{{ label }}</q-item-label>
      <q-item-label caption>{{ caption }}</q-item-label>
    </q-item-section>
  </q-item>
</template>

<script lang="ts">
import { defineComponent, computed, toRefs } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'MenuComponent',
  props: {
    index: {
      type: Number,
      required: true,
    },

    label: {
      type: String,
      required: true,
    },

    caption: {
      type: String,
      default: '',
    },

    path: {
      type: String,
      default: '#',
    },

    icon: {
      type: String,
      default: '',
    },
  },
  setup(props) {
    const { path } = toRefs(props);
    const router = useRouter();
    const active = computed(() => {
      return router.currentRoute.value.path == path.value
    });

    return { active, props };
  },
});
</script>
