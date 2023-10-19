import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BillingView from '../views/BillingView.vue'
import DashboardView from '../views/DashboardView.vue'
import FieldView from '../views/FieldView.vue'
import InventoryView from '../views/InventoryView.vue'
import InvoiceView from '../views/InvoiceView.vue'
import ServicesView from '../views/ServicesView.vue'
import SignInView from '../views/SignInView.vue'
import ClientsView from '../views/ClientsView.vue'
import ClientDetail from '../components/ClientDetail.vue'
import RegistrationView from '../views/RegistrationView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView
    },
    {
      path: '/billing',
      name: 'billing',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/BillingView.vue')
    },
    {
      path: '/field-work',
      name: 'field-work',
      component: FieldView
    },
    {
      path: '/inventory',
      name: 'inventory',
      component: InventoryView
    },
    {
      path: '/invoice',
      name: 'invoice',
      component: InvoiceView
    },
    {
      path: '/services',
      name: 'services',
      component: ServicesView
    },
    {
      path: '/signin',
      name: 'signin',
      component: SignInView
    },
    {
      path: '/clients',
      name: 'clients',
      component: ClientsView
    },
    {
      path: '/client/:id',
      name: 'client-detail',
      component: ClientDetail
    },
    {
      path: '/registration',
      name: 'registration',
      component: RegistrationView
    }

  ]
})

export default router
