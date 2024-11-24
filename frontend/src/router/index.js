import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import BillingView from "../views/BillingView.vue";
import FieldView from "../views/FieldView.vue";
import InventoryView from "../views/InventoryView.vue";
import InvoiceView from "../views/InvoiceView.vue";
import ServicesView from "../views/ServicesView.vue";
import SignInView from "../views/SignInView.vue";
import ClientsView from "../views/ClientsView.vue";
import ClientDetail from "../components/ClientDetail.vue";
import MonthlyBillingForm from "../components/MonthlyBillingForm.vue";
import RegistrationView from "../views/RegistrationView.vue";
import SignupView from "../views/SignupView.vue";
import PartnerSetup from "../views/PartnerSetupView.vue";
import PaymentDetail from "../components/PaymentDetail.vue";
import ServiceForm from "../components/ServiceForm.vue";
import EmployeePage from "../components/Admin/EmployeePage.vue";
import SmsReport from "../components/Billing/SmsReport.vue";
import Admin from "../views/AdminView.vue";
import Staff from "../views/StaffView.vue";
import EmployeeDetails from "../components/Admin/Employee/EmployeeDetails.vue";
import InventoryPage from "../components/Inventory/InventoryPage.vue";
import MaterialPage from "../components/Inventory/MaterialPage.vue";
import InventoryUpdate from "../components/Inventory/InventoryUpdate.vue";
import TicketForm from '../components/FieldWork/TicketForm.vue'
import ClosedTickets from "../components/FieldWork/ClosedTickets.vue";
import ActiveTickets from "../components/FieldWork/ActiveTickets.vue";
import StaffActiveTickets from "../components/Staff/ActiveTickets.vue";
import StaffTicketHistory from "../components/Staff/TicketHistory.vue";
import TicketDetails from "../components/Staff/TicketDetails.vue";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/account",
      name: "partner-setup",
      component: PartnerSetup,
    },
    {
      path: "/login",
      name: "login",
      component: SignInView,
    },
    {
      path: "/dashboard",
      name: "dashboard",
      component: HomeView,
      meta: {
        requireAuth: true,
      },
    },
    {
      path: "/billing",
      name: "billing",
      component: BillingView,
      children: [
        {
          path: "/billing-form",
          name: "fees",
          component: MonthlyBillingForm,
        },
        {
          path: "/payment",
          name: "payment",
          component: PaymentDetail,
        },
        {
          path: "/sms-reports",
          name: "smsReports",
          component: SmsReport,
        },
      ],
    },
    {
      path: "/field-work",
      name: "field-work",
      component: FieldView,
      children: [
        {
          path: "/create-ticket",
          name: "addTicket",
          component: TicketForm
        },
        {
          path: "/open-tickets",
          name: "openTickets",
          component: ActiveTickets
        },
        {
          path: "/closed-tickets",
          name: "closedTickets",
          component: ClosedTickets
        },
      ]
    },
    {
      path: "/inventory",
      name: "inventory",
      component: InventoryView,
      children: [
        {
          path: "/store",
          name: "inventoryStore",
          component: InventoryPage
        },
        {
          path: "/used-materials",
          name: "materialsUsed",
          component: MaterialPage
        },
        {
          path: "/change/:id/update",
          name: "inventoryUpdate",
          component: InventoryUpdate
        }
      ]
    },
    {
      path: "/invoice",
      name: "invoice",
      component: InvoiceView,
    },
    {
      path: "/services",
      name: "services",
      component: ServicesView,
      children: [
        {
          path: "/serviceform",
          name: "service-form",
          component: ServiceForm,
        },
      ],
    },
    {
      path: "/signin",
      name: "signin",
      component: SignInView,
    },
    {
      path: "/clients",
      name: "clients",
      component: ClientsView,
    },
    {
      path: "/client/:id",
      name: "client-detail",
      component: ClientDetail,
    },
    {
      path: "/registration",
      name: "registration",
      component: RegistrationView,
    },
    {
      path: "/",
      name: "signup",
      component: SignupView,
    },
    {
      path: "/admin",
      name: "admin",
      component: Admin,
      children: [
        {
          path: "/employee",
          name: "employee",
          component: EmployeePage,
        },
        {
          path: '/details/:id',
          name: 'employeeDetail',
          component: EmployeeDetails
        }
      ],
    },
    {
      path: "/staff",
      name: "staff",
      component: Staff,
      children: [
        {
          path: "/active-tickets",
          name: "staffActiveTicket",
          component: StaffActiveTickets
        },
        {
          path: "/ticket-details/:id",
          name: "staffTicketDetails",
          component: TicketDetails
        },
        {
          path: "/ticket-history",
          name: "staffTicketHistory",
          component: StaffTicketHistory
        },
      ]
    },
  ],
});
router.beforeEach((to, from, next) => {
  
  if (to.matched.some((record) => record.meta.requireAuth)) {
    // this route requires auth, check if logged in
    // if not, login page.
    const token = localStorage.getItem("token");
    if (!token) {
      next({ path: "/login" });
    } else {
      next();
    }
  } else {
    next(); // make sure to always call next()!
  }
});
export default router;
