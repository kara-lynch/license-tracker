import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView,
    },{
      path: '/home',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/view-licenses',
      name: 'view-licenses',
      component: () => import('../views/ViewLicensesView.vue'),
    },
     {
      path: '/assigned-to-me',
      name: 'assigned-to-me',
      component: () => import('../views/AssignedToMeView.vue'),
    },
    {
      path: '/assign-license',
      name: 'assign-license',
      component: () => import('../views/AssignLicenseView.vue')
    },
  ],
})

export default router
