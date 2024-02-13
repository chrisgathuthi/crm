<script setup>
import { useRouter, RouterView } from 'vue-router'
const router = useRouter()
import Navigation from '@/components/Navigation.vue'

</script>
<template>
    <!-- navigation -->
    <v-row>
        <v-col cols="3">
            <Navigation />
        </v-col>
        <v-col cols="9">
            <v-toolbar class="bg-grey-lighten-5 border-b">
                <v-toolbar-title>Billing</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-btn @click="router.push({ name: 'payment' })">Payments</v-btn>
                <v-btn @click="router.push({ name: 'fees' })">Send sms</v-btn>
                <v-btn @click="router.push({ name: 'smsReports' })">Sms Reports</v-btn>
            </v-toolbar>
            <RouterView />

        </v-col>
    </v-row>
</template>