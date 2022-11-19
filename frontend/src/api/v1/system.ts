import { api } from 'src/boot/axios';
import { sourcePathControl } from 'src/utils/Utils';
import type { TGetUserData } from 'src/types/Utils';
import defaultAvatar from '/imgs/avatar.png';

export const getUserDataApi: TGetUserData = async (user) => {
  const res = await api.get('api/v1/system/user-data/');
  user.value.firstName = res.data.first_name;
  user.value.lastName = res.data.last_name;
  user.value.username = res.data.username;
  user.value.avatar = sourcePathControl(res.data.profile.avatar, defaultAvatar);

  return res;
};
