<script setup>
import { ref } from 'vue';
import { useToastStore } from '../stores/toast';
const store = useToastStore()
</script>
<template>
    <v-snackbar :timeout="store.time" :color="store.classes" v-model="store.isvisible">
        {{ store.message }}

        <template v-slot:actions>
            <v-btn color="blue" variant="text" @click="store.isvisible = false">
                <v-icon icon="mdi-close"></v-icon>
            </v-btn>
        </template>
    </v-snackbar>
</template>