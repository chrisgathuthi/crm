<script setup>
import { RouterView, useRouter } from 'vue-router';
import Navigation from '../components/Navigation.vue';

const router = useRouter()
</script>
<template>
    <aside class="bg-pink">
        <Navigation />
    </aside>
    <main class="h-screen">
        <v-toolbar class="bg-grey-lighten-5 border-b">
            <v-toolbar-title>Faiba plans</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn @click="router.push({ name: 'service-form' })">faiba plans</v-btn>
        </v-toolbar>

        <RouterView />
    </main>
</template>