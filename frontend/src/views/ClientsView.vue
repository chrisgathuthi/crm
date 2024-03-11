<script setup>
import { useRouter } from 'vue-router'

import ClientList from '../components/ClientList.vue'
import BaseLayout from '../components/Layout/BaseLayout.vue';

const router = useRouter()
</script>
<template>
    <BaseLayout>
        <template v-slot:pageMenu>
            <div>
                <v-toolbar density="comfortable">

                    <v-toolbar-title>Clients</v-toolbar-title>

                    <v-spacer></v-spacer>

                    <v-btn color="primary" @click="router.push({ name: 'registration' })" prepend-icon="mdi-plus"
                        class="mr-3">
                        add client
                    </v-btn>
                </v-toolbar>

            </div>

        </template>
        <template v-slot:childComponent>
            <ClientList />

        </template>
    </BaseLayout>
</template>
<style scoped>
a {
    text-decoration: none;

}
</style>