
import { createRouter, createWebHashHistory } from 'vue-router'
import axios from 'axios'
import store from '../store'

import Accommodation from '../view/Accommodation.vue'
import Restaurant from '../view/Restaurant.vue'
import Attraction from '../view/Attraction.vue'
import AcInfo from '../view/AcInfo.vue'
import AtInfo from '../view/AtInfo.vue'
import ReInfo from '../view/ReInfo.vue'
import Route from '../view/Route.vue'
import User from '../view/User.vue'
import AddRoute from '../view/AddRoute.vue'
import RtInfo from '../view/RtInfo.vue'

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
    component: Route,
    beforeEnter:(to,from,next) => {
      axios.get("http://127.0.0.1:5000/api/LoadRoute")
      .then((res)=>{
          console.log('資料 : ',res.data)
          store.dispatch("LoadRtdata", res.data);
          console.log('Samuel')
          next();
      })
    }
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
  },
  {
    path: '/ReInfo',
    name: 'ReInfo',
    component: ReInfo
  },
  {
    path: '/AtInfo',
    name: 'AtInfo',
    component: AtInfo
  },
  {
    path: '/RtInfo',
    name: 'RtInfo',
    component: RtInfo
  },
  {
    path: '/AddRoute',
    name: 'AddRoute',
    component: AddRoute
  }
]
const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL), // 這邊我使用 # 路徑模式
  routes, // 導入使用上方 routes 所定義的路徑
  linkActiveClass: "active",
})

export default router;