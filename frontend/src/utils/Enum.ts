// global func
export const getEnumList = (
  enumObj: object,
  enumType: 'string' | 'number',
  kv: 'keys' | 'values'
) => {
  if (enumType === 'string' && kv === 'keys') return Object.keys(enumObj);
  else if (enumType === 'string' && kv === 'values')
    return Object.values(enumObj);
  else if (enumType === 'number' && kv === 'keys')
    return Object.values(enumObj).filter((v) => isNaN(Number(v)));
  else if (enumType === 'number' && kv === 'values')
    return Object.values(enumObj).filter((v) => !isNaN(Number(v)));
  return [];
};

export enum EThemeModeIcon {
  DarkMode = 'dark_mode',
  LightMode = 'light_mode',
}

export enum EChartJSFontColor {
  Dark = 'dark',
  White = 'white',
}

export enum EMonths {
  January = 1,
  February = 2,
  March = 3,
  April = 4,
  May = 5,
  June = 6,
  July = 7,
  August = 8,
  September = 9,
  October = 10,
  November = 11,
  December = 12,
}
