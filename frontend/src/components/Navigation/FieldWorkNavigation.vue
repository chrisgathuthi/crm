<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()
</script>
<template>
    <div>
        <v-app-bar prominent class="bg-grey-lighten-5 static" tag="div">

            <v-toolbar-title>Field Tickets</v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn @click="router.push({ name: 'addTicket' })" prepend-icon="mdi-plus" class="mr-3">Tickets</v-btn>
            <v-btn @click="router.push({ name: 'openTickets' })" prepend-icon="mdi mdi-hard-hat">open Tickets</v-btn>
            <v-btn @click="router.push({ name: 'closedTickets' })" prepend-icon="mdi mdi-hard-hat">Closed Tickets</v-btn>
        </v-app-bar>
    </div>
</template>