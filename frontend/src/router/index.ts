import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
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
  ],
})

export default router
