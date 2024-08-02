<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()
</script>
<template>
    <v-app-bar>
        <v-toolbar prominent class="bg-grey-lighten-5 static" tag="div">
            <v-toolbar-title>Staff</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn @click="router.push({name: 'staffActiveTicket'})">
                Active Tickets
                <v-badge color="error" dot>
                    <v-icon>mdi mdi-hard-hat</v-icon>
                </v-badge>
            </v-btn>
            <v-btn @click="router.push({name: 'staffTicketHistory'})" prepend-icon="mdi mdi-timeline-text-outline">Ticket History</v-btn>
        </v-toolbar>
    </v-app-bar>
</template>