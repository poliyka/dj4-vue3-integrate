// interfaces
export interface TUserStore {
  firstName: string;
  lastName: string;
  avatar: string;
  username: string;
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
