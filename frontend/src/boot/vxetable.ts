import { boot } from 'quasar/wrappers';
import { i18n } from 'src/boot/i18n';

import 'vxe-table/lib/style.css';

import {
  // 錶格功能
  // Filter,
  // Edit,
  // Menu,
  // Export,
  // Keyboard,
  // Validator,

  // 可選組件
  Icon,
  Column,
  // Colgroup,
  Tooltip,
  Toolbar,
  // Pager,
  // Form,
  // FormItem,
  // FormGather,
  // Checkbox,
  // CheckboxGroup,
  // Radio,
  // RadioGroup,
  // RadioButton,
  // Switch,
  // Input,
  // Select,
  // Optgroup,
  // Option,
  // Textarea,
  Button,
  // Modal,
  // List,
  // Pulldown,

  // 錶格
  Table,
  Grid,
  VXETable,
} from 'vxe-table';

export default boot(({ app }) => {
  VXETable.setup({
    // size: null, // 全局尺寸
    zIndex: 2001, // 全局 zIndex 起始值，如果項目的的 z-index 樣式值過大時就需要跟隨設定更大，避免被遮擋
    version: 1, // 版本號，對於某些帶數據緩存的功能有用到，上升版本號可以用於重置數據
    loadingText: 'loading...', // 全局loading提示內容，如果為null則不顯示文本
    i18n: (key, args) => i18n.global.t(key, args), // 全局國際化方法
    translate(key, args) {
      // 自定義的翻譯方法
      // 不可使用 vxe 作為篩選自段的前綴，因為 vxe 的翻譯包已經使用此前綴
      if (key && key.indexOf('vxeTable.') > -1) {
        return i18n.global.t(key, args);
      }
      return key;
    },
    table: {
      showHeader: true,
      keepSource: true,
      showOverflow: true,
      showHeaderOverflow: true,
      showFooterOverflow: true,
      size: 'medium',
      autoResize: false,
      stripe: false,
      border: 'full',
      round: false,
      emptyText: 'vxeTable.content.emptyText',
      rowConfig: {
        keyField: '_X_ROW_KEY', // 行數據的唯一主鍵字段名
      },
      // radioConfig: {
      //   trigger: 'default'
      // },
      // checkboxConfig: {
      //   strict: false,
      //   highlight: false,
      //   range: false,
      //   trigger: 'default'
      // },
      // sortConfig: {
      // remote: false,
      // trigger: 'default',
      // orders: ['asc', 'desc', null],
      // sortMethod: null
      // },
      // filterConfig: {
      // remote: false,
      // filterMethod: null
      // },
      // expandConfig: {
      //   trigger: 'default',
      //   showIcon: true
      // },
      // treeConfig: {
      //   rowField: 'id',
      //   parentField: 'parentId',
      //   children: 'children',
      //   hasChild: 'hasChild',
      //   mapChildren: '_X_ROW_CHILD',
      //   indent: 20,
      //   showIcon: true
      // },
      tooltipConfig: {
        enterable: true,
      },
      // menuConfig: {
      //   visibleMethod () {}
      // },
      // editConfig: {
      //   mode: 'cell',
      //   showAsterisk: true
      // },
      importConfig: {
        modes: ['insert', 'covering'],
      },
      exportConfig: {
        modes: ['current', 'selected'],
      },
      // customConfig: {
      //  storage: false
      // },
      scrollX: {
        gt: 60,
      },
      scrollY: {
        gt: 100,
      },
      // loading: {
      //   icon: 'vxe-icon-spinner roll',
      //   text: '加載中...'
      // }
    },
    grid: {
      // size: 'mini',
      // zoomConfig: {
      //   escRestore: true
      // },
      // pagerConfig: {
      //   perfect: false
      // },
      // toolbarConfig: {
      //   perfect: false
      // },
      // proxyConfig: {
      //   autoLoad: true,
      //   message: true,
      //   props: {
      //     list: null, // 用於列錶，讀取回響數據
      //     result: 'result', // 用於分頁，讀取回響數據
      //     total: 'page.total' // 用於分頁，讀取總條數
      //   }
      //   beforeItem: null,
      //   beforeColumn: null,
      //   beforeQuery: null,
      //   afterQuery: null,
      //   beforeDelete: null,
      //   afterDelete: null,
      //   beforeSave: null,
      //   afterSave: null
      // }
    },
    pager: {
      size: 'medium',
      autoHidden: true,
      perfect: true,
      pageSize: 10,
      pagerCount: 1,
      pageSizes: [10, 15, 20, 50, 100],
      layouts: [
        'PrevJump',
        'PrevPage',
        'Jump',
        'PageCount',
        'NextPage',
        'NextJump',
        'Sizes',
        'Total',
      ],
    },
    // form: {
    //   preventSubmit: false
    //   size: null,
    //   colon: false,
    //   validConfig: {
    //     autoPos: true
    //   },
    //   tooltipConfig: {
    //     enterable: true
    //   },
    //   titleAsterisk: true
    // },
    // input: {
    //   size: null,
    //   transfer: false,
    //   parseFormat: 'yyyy-MM-dd HH:mm:ss',
    //   labelFormat: '',
    //   valueFormat: '',
    //   startDay: 1,
    //   digits: 2,
    //   controls: true
    // },
    // textarea: {
    //   size: null
    //   autosize: {
    //     minRows: 1,
    //     maxRows: 10
    //   }
    // },
    select: {
      size: 'medium',
      transfer: false,
      optionConfig: {
        keyField: '_X_OPTION_KEY', // 選項數據的唯一主鍵字段名
      },
      multiCharOverflow: 8,
    },
    // toolbar: {
    //   size: 'medium',
    //   import: {
    //     mode: 'covering'
    //   },
    //   export: {
    //     types: ['csv', 'html', 'xml', 'txt']
    //   },
    //   custom: {
    //     isFooter: true
    //   },
    //   buttons: [],
    //   tools: []
    // },
    button: {
      size: 'medium',
      transfer: false,
    },
    radio: {
      size: 'medium',
    },
    checkbox: {
      size: 'medium',
    },
    switch: {
      size: 'medium',
    },
    modal: {
      // size: null,
      minWidth: 340,
      minHeight: 200,
      lockView: true,
      mask: true,
      duration: 3000,
      marginSize: 0,
      dblclickZoom: true,
      showTitleOverflow: true,
      storage: false,
    },
    list: {
      scrollY: {
        gt: 100,
      },
    },
  });
  // 錶格功能
  // app.use(Filter)
  // .use(Edit)
  // .use(Menu)
  // .use(Export)
  // .use(Keyboard)
  // .use(Validator)

  // 可選組件
  app
    .use(Icon)
    .use(Column)
    // .use(Colgroup)
    .use(Tooltip)
    .use(Toolbar)
    // .use(Pager)
    // .use(Form)
    // .use(FormItem)
    // .use(FormGather)
    // .use(Checkbox)
    // .use(CheckboxGroup)
    // .use(Radio)
    // .use(RadioGroup)
    // .use(RadioButton)
    // .use(Switch)
    // .use(Input)
    // .use(Select)
    // .use(Optgroup)
    // .use(Option)
    // .use(Textarea)
    .use(Button)
    // .use(Modal)
    // .use(List)
    // .use(Pulldown)

    // 安裝錶格
    .use(Grid)
    .use(Table);
});
