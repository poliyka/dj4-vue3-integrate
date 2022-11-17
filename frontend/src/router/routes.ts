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
    redirect: '/dashboard',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        name: 'dashboard',
        path: '/dashboard',
        component: () => import('pages/content/dashboard.vue'),
      },
      {
        name: 'schedule',
        path: '/schedule',
        component: () => import('pages/content/schedule.vue'),
      },
      {
        name: 'jobs',
        path: '/jobs',
        component: () => import('pages/content/jobs.vue'),
      },
      {
        name: 'history',
        path: '/history',
        component: () => import('pages/content/history.vue'),
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
