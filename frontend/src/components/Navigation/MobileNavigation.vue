<script setup>
import { ref } from 'vue'

const expand = ref(false)
</script>

<template>
        <section class="d-none">
                <v-app-bar color="primary" prominent class="block d-none d-md-none">
                        <v-app-bar-nav-icon variant="text" @click="expand = !expand"></v-app-bar-nav-icon>
                        <v-toolbar-title>Lamp</v-toolbar-title>
                </v-app-bar>

                <v-sheet class="bg-pink elevation-3 d-md-none" position="absolute" tag="div" width="100%">
                        <v-row>
                                <v-col class="bg-pink">
                                        <v-expand-transition>

                                                <v-list color="transparent" v-show="expand">
                                                        <v-list-item prepend-avatar="logo.svg" title="Lamp"
                                                                subtitle="......">
                                                        </v-list-item>

                                                        <v-divider class="mt-2"></v-divider>

                                                        <RouterLink active-class="active" color="#27248C"
                                                                :to="{ name: 'admin' }"><v-list-item
                                                                        prepend-icon="mdi-security"
                                                                        title="Admin"></v-list-item></RouterLink>
                                                        <RouterLink active-class="active" :to="{ name: 'clients' }">
                                                                <v-list-item prepend-icon="mdi-account-multiple"
                                                                        title="Clients"></v-list-item></RouterLink>
                                                        <RouterLink active-class="active" :to="{ name: 'billing' }">
                                                                <v-list-item
                                                                        prepend-icon="mdi-account-credit-card-outline"
                                                                        title="Billing"></v-list-item>
                                                        </RouterLink>
                                                        <RouterLink active-class="active" :to="{ name: 'field-work' }">
                                                                <v-list-item prepend-icon="mdi-account-hard-hat-outline"
                                                                        title="Field work"></v-list-item>
                                                        </RouterLink>
                                                        <RouterLink active-class="active" :to="{ name: 'inventory' }">
                                                                <v-list-item prepend-icon="mdi-note-outline"
                                                                        title="Inventory"></v-list-item></RouterLink>
                                                        <RouterLink active-class="active" :to="{ name: 'invoice' }">
                                                                <v-list-item prepend-icon="mdi mdi-bank"
                                                                        title="Invoices"></v-list-item></RouterLink>
                                                        <RouterLink active-class="active" :to="{ name: 'services' }">
                                                                <v-list-item prepend-icon="mdi-face-agent"
                                                                        title="Services"></v-list-item></RouterLink>
                                                        <RouterLink active-class="active" :to="{ name: 'staff' }">
                                                                <v-list-item prepend-icon="mdi-account-circle"
                                                                        title="Staff"></v-list-item></RouterLink>

                                                </v-list>

                                        </v-expand-transition>


                                </v-col>
                        </v-row>

                </v-sheet>

        </section>


</template>