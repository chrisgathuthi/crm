<script setup>
import { useRouter} from 'vue-router';
const router = useRouter()
</script>
<template>
    <v-toolbar density="comfortable">

        <v-toolbar-title>Admin</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn color="primary" @click="router.push({ name: 'employee' })" class="mr-3">
            Employees
        </v-btn>
    </v-toolbar>
</template>