import { SwitchMode } from 'src/types/Utils';
import { ThemeMode } from 'src/utils/Enum';

export const switchMode: SwitchMode = ($q, themeMode) => {
  // A function that is used to switch between dark and light mode.
  $q.dark.set(!$q.dark.isActive);
  if ($q.dark.isActive) {
    themeMode.value = ThemeMode.DarkMode;
  } else {
    themeMode.value = ThemeMode.LightMode;
  }
};
