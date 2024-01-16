<script setup>
import { RouterView } from 'vue-router';
import Navigation from '../components/Navigation.vue';
import AdminNavigtion from '../components/Navigation/AdminNavigtion.vue';

</script>
<template>
    <v-row>
        <v-col cols="3">
            <Navigation />
        </v-col>
        <v-col cols="9">
            <AdminNavigtion/>
            <RouterView/>
        </v-col>
    </v-row>
</template>