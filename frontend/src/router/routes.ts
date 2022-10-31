import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  // Login Page
  {
    name: 'login',
    path: '/login',
    component: () => import('layouts/LoginLayout.vue'),
  },
  // Home Page
  {
    name: 'home',
    path: '/',
    redirect: '/search',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        name: 'search',
        path: '/search',
        component: () => import('pages/contents/search.vue'),
      },
      {
        name: 'upload',
        path: '/upload',
        component: () => import('pages/contents/upload.vue'),
      },
      {
        name: 'delete',
        path: '/delete',
        component: () => import('pages/contents/search.vue'),
      },
      {
        name: 'reverse',
        path: '/reverse',
        component: () => import('pages/contents/search.vue'),
      },
    ],
    meta: {
      requiresAuth: true,
    },
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    name: '404',
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
