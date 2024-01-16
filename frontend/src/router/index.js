import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BillingView from '../views/BillingView.vue'
import FieldView from '../views/FieldView.vue'
import InventoryView from '../views/InventoryView.vue'
import InvoiceView from '../views/InvoiceView.vue'
import ServicesView from '../views/ServicesView.vue'
import SignInView from '../views/SignInView.vue'
import ClientsView from '../views/ClientsView.vue'
import ClientDetail from '../components/ClientDetail.vue'
import MonthlyBillingForm from '../components/MonthlyBillingForm.vue'
import RegistrationView from '../views/RegistrationView.vue'
import SignupView from '../views/SignupView.vue'
import PartnerSetup from '../views/PartnerSetupView.vue'
import PaymentDetail from '../components/PaymentDetail.vue'
import ServiceForm from '../components/ServiceForm.vue'
import EmployeePage from '../components/Admin/Employee.vue'
import Admin from '../views/AdminView.vue'
import Staff from '../views/StaffView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/account',
      name: 'partner-setup',
      component: PartnerSetup
    },
    {
      path: '/login',
      name: 'login',
      component: SignInView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: HomeView
    },
    {
      path: '/billing',
      name: 'billing',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/BillingView.vue'),
      children: [
        {
          path: '/billing-form',
          name: 'fees',
          component: MonthlyBillingForm
        },
        {
          path: "payment",
          name: "payment",
          component: PaymentDetail
        }
      ]
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
      component: ServicesView,
      children: [
        {
          path:'/serviceform',
          name: 'service-form',
          component: ServiceForm
        }
      ]
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
    },
    {
      path: '/',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin,
      children:[
        {
          path: "/employee",
          name: 'employee',
          component: EmployeePage
        },{
          path: "/staff",
          name: "staff",
          component: Staff
        }

      ]
    }

  ]
})

export default router
