<template>
  <q-card>
    <q-card-section>
      <vxe-grid v-bind="gridOptions"> </vxe-grid>
    </q-card-section>
  </q-card>
</template>

<script lang="ts">
import { defineComponent, reactive } from 'vue';
import { VxeGridProps } from 'vxe-table';
import { useGlobalStore } from 'src/stores/global';
import { VxeTablePropTypes } from 'vxe-table'

export default defineComponent({
  name: 'VxeTableExample',
  setup() {
    const globalStore = useGlobalStore();

    const gridOptions = reactive<VxeGridProps>({
      height: 300,
      align: 'center',
      headerCellStyle: globalStore.headerCellStyle as VxeTablePropTypes.HeaderCellStyle,
      toolbarConfig: {
        buttons: [
          { code: 'insert_actived', name: '新增' },
          { code: 'delete', name: '直接删除' },
          { code: 'mark_cancel', name: '删除/取消' },
          { code: 'save', name: 'vxeTable.button.save', status: 'success' },
        ],
        refresh: true,
        import: true,
        export: true,
        print: true,
        zoom: true,
        custom: true,
      },
      columnConfig: {
        resizable: true,
      },
      columns: [
        { type: 'seq', width: 50 },
        { field: 'name', title: 'name' },
        { field: 'sex', title: 'sex', showHeaderOverflow: true },
        { field: 'address', title: 'Address', showOverflow: true },
      ],
      data: [
        {
          id: 10001,
          name: 'Test1',
          nickname: 'T1',
          role: 'Develop',
          sex: 'Man',
          age: 28,
          address: 'Shenzhen',
        },
        {
          id: 10002,
          name: 'Test2',
          nickname: 'T2',
          role: 'Test',
          sex: 'Women',
          age: 22,
          address: 'Guangzhou',
        },
        {
          id: 10003,
          name: 'Test3',
          nickname: 'T3',
          role: 'PM',
          sex: 'Man',
          age: 32,
          address: 'Shanghai',
        },
        {
          id: 10004,
          name: 'Test4',
          nickname: 'T4',
          role: 'Designer',
          sex: 'Women',
          age: 23,
          address: 'Shenzhen',
        },
        {
          id: 10005,
          name: 'Test5',
          nickname: 'T5',
          role: 'Develop',
          sex: 'Women',
          age: 30,
          address: 'Shanghai',
        },
        {
          id: 10006,
          name: 'Test6',
          nickname: 'T6',
          role: 'Designer',
          sex: 'Women',
          age: 21,
          address: 'Shenzhen',
        },
        {
          id: 10007,
          name: 'Test7',
          nickname: 'T7',
          role: 'Test',
          sex: 'Man',
          age: 29,
          address: 'Shenzhen',
        },
        {
          id: 10008,
          name: 'Test8',
          nickname: 'T8',
          role: 'Develop',
          sex: 'Man',
          age: 35,
          address: 'Shenzhen',
        },
      ],
    });

    return {
      gridOptions,
    };
  },
});
</script>
