
import { createRouter, createWebHashHistory} from 'vue-router'
import axios from 'axios'
import store from '../store'

import Accommodation from '../view/Accommodation.vue'
import Restaurant from '../view/Restaurant.vue'
import Attraction from '../view/Attraction.vue'
import AcInfo from '../view/AcInfo.vue'
import Route from '../view/Route.vue'
import User from '../view/User.vue'

const routes = [
    {
      path: "/",
      name: "/",
      redirect: "/Accommodation",
    },
    {
      path: '/Accommodation',
      name: 'Accommodation',
      component: Accommodation
    },
    {
      path: '/Restaurant',
      name: "Restaurant",
      component: Restaurant
    },
    {
      path: '/Attraction',
      name: 'Attraction',
      component: Attraction
    },
    {
      path: '/Route',
      name: 'Route',
      component: Route
    },
    {
      path: '/User',
      name: 'User',
      component: User
    },
    {
      path: '/AcInfo',
      name: 'AcInfo',
      component: AcInfo
    }
  ]
const router = createRouter({
    history: createWebHashHistory(import.meta.env.BASE_URL), // 這邊我使用 # 路徑模式
    routes, // 導入使用上方 routes 所定義的路徑
    linkActiveClass: "active",
  })

export default router;