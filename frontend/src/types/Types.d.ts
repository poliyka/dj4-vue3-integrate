// interfaces
export interface TUser {
  profile: Profile;
  lastLogin: string;
  username: string;
  firstName: string;
  lastName: string;
  email: string;
}

export interface Profile {
  avatar: string;
  birth: string;
  gender: string;
}

export interface TMonthsConfig {
  count?: number;
  short?: boolean;
  season?: 1 | 2 | 3 | 4;
}

// type
type TChartJSPlugin =
  | 'bar'
  | 'line'
  | 'scatter'
  | 'bubble'
  | 'pie'
  | 'doughnut'
  | 'polarArea'
  | 'radar';


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
