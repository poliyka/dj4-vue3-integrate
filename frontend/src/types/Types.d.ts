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
