import { boot } from 'quasar/wrappers';
import VueNativeSock from 'vue-native-websocket-vue3';
import { useSocketStoreWithOut } from 'src/stores/socket';

const store = useSocketStoreWithOut();

export default boot(({ app }) => {
  app.use(VueNativeSock, 'ws://localhost:3002/ws/log', {
    // 啓用pinia集成 | enable pinia integration
    store: store,
    // 數據發送/接收使用使用json
    format: 'json',
    // 開啓手動調用 connect() 連接服務器
    connectManually: false,
    // 開啓自動重連
    reconnection: true,
    // 嘗試重連的次數
    reconnectionAttempts: 5,
    // 重連間隔時間
    reconnectionDelay: 3000,
  });
});


