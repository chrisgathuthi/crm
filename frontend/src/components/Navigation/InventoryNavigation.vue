<script setup>
import {  useRouter } from 'vue-router';

const router = useRouter()
</script>
<template>
    <div>
        <v-app-bar class="bg-grey-lighten-5 border-b">
            <v-toolbar-title>Inventory</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn @click="router.push({name: 'materialsUsed'})"  prepend-icon="mdi mdi-tools">Materials Used</v-btn>
            <v-btn @click="router.push({name: 'inventoryStore'})"  prepend-icon="mdi mdi-warehouse">warehouse</v-btn>
        </v-app-bar>

    </div>
</template>