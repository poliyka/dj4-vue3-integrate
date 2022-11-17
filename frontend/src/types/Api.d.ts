export interface LoginFormData {
  username: string;
  password: string;
}

export interface RUserData {
  profile: Profile;
  last_login: string;
  username: string;
  first_name: string;
  last_name: string;
  email: string;
}

export interface Profile {
  avatar: string;
  birth: string;
  gender: string;
}
