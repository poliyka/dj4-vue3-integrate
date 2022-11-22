// interfaces
export interface TUserStore {
  firstName: string;
  lastName: string;
  avatar: string;
  username: string;
}


interface TSocketStore {
  // 儲存 socket
  socket: any;
  // 連接狀態
  isConnected: boolean;
  // 消息內容
  message: object;
  // 重新連接錯誤
  reconnectError: boolean;
  // 心跳消息發送時間
  heartBeatInterval: number;
  // 心跳定時器
  heartBeatTimer: number;
}
