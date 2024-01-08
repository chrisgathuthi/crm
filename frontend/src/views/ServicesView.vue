
<script setup>
import { RouterView, useRouter} from 'vue-router';
import Navigation from '../components/Navigation.vue';

const router = useRouter()
</script>
<template>
    <v-row>
        <v-col cols="3">
            <Navigation/>
        </v-col>
        <v-col cols="9">
            <v-toolbar class="bg-grey-lighten-5 border-b">
                <v-toolbar-title>Faiba plans</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-btn @click="router.push({ name: 'service-form' })">faiba plans</v-btn>
            </v-toolbar>
            <RouterView/>
        </v-col>
    </v-row>
</template>