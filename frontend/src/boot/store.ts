import { createPinia } from 'pinia';
import { boot } from 'quasar/wrappers';

const store = createPinia();

export default boot(({ app }) => {
  app.use(store);
});

export { store };

