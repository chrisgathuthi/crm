<script setup>
import { useRouter } from 'vue-router'

import ClientList from '../components/ClientList.vue'
import Navigation from '../components/Navigation.vue';

const router = useRouter()
</script>
<template>
    <!-- navigation -->
    <v-row>
        <v-col cols="3">
            <Navigation />
        </v-col>
        <v-col cols="9">
            <v-toolbar density="comfortable">

                <v-toolbar-title>Clients</v-toolbar-title>

                <v-spacer></v-spacer>

                <v-btn color="primary" @click="router.push({ name: 'registration' })" prepend-icon="mdi-plus" class="mr-3">
                    add client
                </v-btn>
            </v-toolbar>

            <!-- view -->

            <ClientList />


        </v-col>
    </v-row>
</template>
<style scoped>
a {
    text-decoration: none;

}
</style>