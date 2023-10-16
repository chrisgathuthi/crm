<script setup>
import {RouterLink, RouterView} from 'vue-router'

import ClientList from '../components/ClientList.vue'
</script>
<template>
    <v-app-bar>
        <v-card variant="flat">
            <v-card-item>
                <RouterLink to="/">
                    <v-icon size="large" color="green-darken-2" icon="mdi-plus"></v-icon> Clients
                </RouterLink>
            </v-card-item>
        </v-card>
    </v-app-bar>

    <v-divider></v-divider>
    <ClientList/>
    
</template>
<style scoped>
a{
    text-decoration: none;

}
</style>