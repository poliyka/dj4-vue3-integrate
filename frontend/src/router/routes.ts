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
    redirect: '/example',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        name: 'example',
        path: '/example',
        component: () => import('src/pages/content/Example.vue'),
      },
      {
        name: 'dashboard',
        path: '/dashboard',
        component: () => import('src/pages/content/Dashboard.vue'),
      },
      {
        name: 'schedule',
        path: '/schedule',
        component: () => import('src/pages/content/Schedule.vue'),
      },
      {
        name: 'jobs',
        path: '/jobs',
        component: () => import('src/pages/content/Jobs.vue'),
      },
      {
        name: 'history',
        path: '/history',
        component: () => import('src/pages/content/History.vue'),
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
