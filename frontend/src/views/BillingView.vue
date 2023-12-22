<script setup>
import {useRouter, RouterView} from 'vue-router'
const router = useRouter()
import Navigation from '@/components/Navigation.vue'

</script>
<template>
    <v-toolbar>
        <v-toolbar-title>Billing</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn @click="router.push({name: 'fees'})">Payments</v-btn>
        <v-btn @click="router.push({name: 'fees'})">Send sms</v-btn>
        <v-btn to="">Failed sms</v-btn>
    </v-toolbar>
    <!-- navigation -->
    <Navigation/>
    <RouterView/>

</template>