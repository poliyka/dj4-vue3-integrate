import { defineStore } from 'pinia';
import { TSocketStore } from 'src/types/Types';
import { store } from 'src/boot/store';
import { Notify, QNotifyCreateOptions } from 'quasar';

const NotifyKw = {
  type: 'info',
  color: 'info',
  timeout: 3000,
  position: 'bottom',
  message: '',
} as QNotifyCreateOptions;

export const useSocketStore = defineStore('socket', {
  state: (): TSocketStore => ({
    // 儲存 socket
    socket: null,
    // 連接狀態
    isConnected: false,
    // 消息內容
    message: {},
    // 重新連接錯誤
    reconnectError: false,
    // 心跳消息發送時間
    heartBeatInterval: 50000,
    // 心跳定時器
    heartBeatTimer: 0,
  }),

  actions: {
    // 連接打開
    SOCKET_ONOPEN(event: { currentTarget: WebSocket }) {
      this.socket = event.currentTarget;
      this.isConnected = true;
      // 連接成功時啓動定時發送心跳消息，避免被服務器斷開連接
      this.heartBeatTimer = window.setInterval(() => {
        const message = '心跳消息';
        this.isConnected &&
          this.socket.sendObj({
            code: 200,
            msg: message,
          });
      }, this.heartBeatInterval);
    },
    // 連接關閉
    SOCKET_ONCLOSE(event: object) {
      this.isConnected = false;
      // 連接關閉時停掉心跳消息
      window.clearInterval(this.heartBeatTimer);
      this.heartBeatTimer = 0;
      console.log('連接已斷開: ' + new Date());
      console.log(event);
    },
    // 發生錯誤
    SOCKET_ONERROR(event: object) {
      console.error(event);
    },
    // 收到服務端發送的消息
    SOCKET_ONMESSAGE(message: object) {
      this.message = message;
      Notify.create({ ...NotifyKw, message: JSON.stringify(message) });
    },
    // 自動重連
    SOCKET_RECONNECT(count: number) {
      console.info('消息係統重連中...', count);
    },
    // 重連錯誤
    SOCKET_RECONNECT_ERROR() {
      console.error('重連錯誤');
      this.reconnectError = true;
    },
  },
});

export function useSocketStoreWithOut() {
  return useSocketStore(store);
}
