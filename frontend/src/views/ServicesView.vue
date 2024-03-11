<script setup>
import { useRouter } from 'vue-router';
import BaseLayout from '../components/Layout/BaseLayout.vue';

const router = useRouter()
</script>
<template>
    <BaseLayout>
        <template v-slot:pageMenu>
            <div>
                <v-app-bar prominent class="bg-grey-lighten-5 static" tag="div">
                    <v-toolbar-title>Faiba plans</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-btn @click="router.push({ name: 'service-form' })">faiba plans</v-btn>
                </v-app-bar>
            </div>
        </template>
    </BaseLayout>
</template>