<script setup>
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()

const deleteToken = () =>{
        localStorage.removeItem("token")
        router.push({name:"login"})
}
</script>
<template>
    <v-navigation-drawer class="navigation d-xs-none" theme="dark">
        <v-list color="transparent">
            <v-list-item prepend-avatar="logo.svg" title="Lamp"
                subtitle="......">
            </v-list-item>

            <v-divider class="mt-2"></v-divider>

            <RouterLink active-class="active" color="#27248C" :to="{ name: 'admin' }"><v-list-item prepend-icon="mdi-security"
                    title="Admin"></v-list-item></RouterLink>
            <RouterLink active-class="active" :to="{ name: 'clients' }"><v-list-item prepend-icon="mdi-account-multiple"
                    title="Clients"></v-list-item></RouterLink>
            <RouterLink active-class="active" :to="{ name: 'billing' }"><v-list-item
                    prepend-icon="mdi-account-credit-card-outline" title="Billing"></v-list-item></RouterLink>
            <RouterLink active-class="active" :to="{ name: 'field-work' }"><v-list-item
                    prepend-icon="mdi-account-hard-hat-outline" title="Field work"></v-list-item></RouterLink>
            <RouterLink active-class="active" :to="{ name: 'inventory' }"><v-list-item prepend-icon="mdi-note-outline"
                    title="Inventory"></v-list-item></RouterLink>
            <RouterLink active-class="active" :to="{ name: 'invoice' }"><v-list-item prepend-icon="mdi mdi-bank"
                    title="Invoices"></v-list-item></RouterLink>
            <RouterLink active-class="active" :to="{ name: 'services' }"><v-list-item prepend-icon="mdi-face-agent"
                    title="Services"></v-list-item></RouterLink>
        <RouterLink active-class="active" :to="{ name: 'staff' }"><v-list-item prepend-icon="mdi-account-circle"
                    title="Staff"></v-list-item></RouterLink>

        </v-list>

        <template v-slot:append>
            <div class="pa-2">
                <v-btn block color="primary" @click="deleteToken"> Logout </v-btn>
            </div>
        </template>

    </v-navigation-drawer>
</template>
<style scoped>
.navigation{
        background-color: #27248C;
}
.v-list-item{
        color: white;
}
</style>