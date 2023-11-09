<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Toast from '@/components/Toast.vue'
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { onBeforeMount } from 'vue';
const userStore = useUserStore()

onBeforeMount(() => {
  const token = userStore.user.access

  if(token){
    axios.defaults.headers.common['Authorization'] = "Bearer "+token
  }else{
    axios.defaults.headers.common['Authorization'] = ""
  }
})
</script>

<template>
  <VApp style="width: 100%; height: 100vh;" >
    <v-layout>
      <v-navigation-drawer class="bg-purple-darken-2" theme="dark" permanent>
        <v-list color="transparent">
          <v-list-item prepend-avatar="https://randomuser.me/api/portraits/women/85.jpg" title="Fastech"
            subtitle="fast secure internet">
          </v-list-item>

          <v-divider></v-divider>

          <RouterLink active-class="active" :to="{name: 'dashboard'}"><v-list-item prepend-icon="mdi-view-dashboard" title="Dashboard"></v-list-item></RouterLink>
          <RouterLink active-class="active" :to="{name: 'clients'}"><v-list-item prepend-icon="mdi-account-multiple" title="Clients"></v-list-item></RouterLink>
          <RouterLink active-class="active" :to="{name: 'billing'}"><v-list-item prepend-icon="mdi-account-credit-card-outline" title="Billing"></v-list-item></RouterLink>
          <RouterLink active-class="active" :to="{name: 'field-work'}"><v-list-item prepend-icon="mdi-account-hard-hat-outline" title="Field work"></v-list-item></RouterLink>
          <RouterLink active-class="active" :to="{name: 'inventory'}"><v-list-item prepend-icon="mdi-note-outline" title="Inventory"></v-list-item></RouterLink>
          <RouterLink active-class="active" :to="{name: 'invoice'}"><v-list-item prepend-icon="mdi mdi-bank" title="Invoices"></v-list-item></RouterLink>
          <RouterLink active-class="active" :to="{name: 'services'}"><v-list-item prepend-icon="mdi-face-agent" title="Services"></v-list-item></RouterLink>
          <RouterLink active-class="active" :to="{name: 'signin'}"><v-list-item prepend-icon="mdi-login" title="Signin"></v-list-item></RouterLink>

        </v-list>

        <template v-slot:append>
          <div class="pa-2">
            <v-btn block> Logout </v-btn>
          </div>
        </template>

      </v-navigation-drawer>
      <v-main>
        <RouterView />
        <Toast/>
      </v-main>
    </v-layout>
  </VApp>
</template>

<style scoped>

a{
  color: #00E676;
  text-decoration: none;
}
a:hover{
  color: #06ac5b;
}
.active{
  color: #ffffff;
}
.v-main{
  overflow: scroll;
}
</style>