<script setup>
import { RouterView, useRouter } from 'vue-router';
import Navigation from '../components/Navigation.vue';

const router = useRouter()
</script>
<template>
    <main class="">
        <aside class="bg-red">
            <Navigation />
        </aside>
        <section>
            <div>
                <v-app-bar prominent class="bg-grey-lighten-5" tag="div">
                    <v-toolbar-title>Faiba plans</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-btn @click="router.push({ name: 'service-form' })">faiba plans</v-btn>
                </v-app-bar>

            </div>


            <RouterView />
        </section>
    </main>
</template>