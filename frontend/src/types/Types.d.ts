// interfaces
export interface States {
  name: string;
  old: number;
}

export interface Products {
  name: string;
  old: number;
}

export interface Menu {
  id: number;
  content: string;
}

export interface Meta {
  totalCount: number;
}

export interface TUserStore {
  firstName: string;
  lastName: string;
  avatar: string;
  username: string;
}
