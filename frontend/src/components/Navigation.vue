
<script setup>
import { RouterLink } from 'vue-router'
</script>
<template>
    <v-navigation-drawer class="bg-purple-darken-2" theme="dark" permanent>
        <v-list color="transparent">
            <v-list-item prepend-avatar="../../public/logo.png" title="Lamp"
                subtitle="we deliver">
            </v-list-item>

            <v-divider inset></v-divider>

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

        </v-list>

        <template v-slot:append>
            <div class="pa-2">
                <v-btn block> Logout </v-btn>
            </div>
        </template>

    </v-navigation-drawer>
</template>