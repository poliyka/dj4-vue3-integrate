import type { TSwitchMode } from 'src/types/Utils';
import { EThemeMode } from 'src/utils/Enum';

export const switchMode: TSwitchMode = ($q, themeMode) => {
  // A function that is used to switch between dark and light mode.
  $q.dark.set(!$q.dark.isActive);
  if ($q.dark.isActive) {
    themeMode.value = EThemeMode.DarkMode;
  } else {
    themeMode.value = EThemeMode.LightMode;
  }
};
