<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
import BaseLayout from '../components/Layout/BaseLayout.vue';

</script>
<template>
    <!-- navigation -->
    <BaseLayout>
        <template v-slot:pageMenu>
            <div>
                <v-app-bar class="bg-grey-lighten-5 border-b">
                    <v-toolbar-title>Billing</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-btn @click="router.push({ name: 'payment' })">Payments</v-btn>
                    <v-btn @click="router.push({ name: 'fees' })">Send sms</v-btn>
                    <v-btn @click="router.push({ name: 'smsReports' })">Sms Reports</v-btn>
                </v-app-bar>

            </div>
        </template>
    </BaseLayout>

    

</template>