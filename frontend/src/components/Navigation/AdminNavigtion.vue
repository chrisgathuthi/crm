<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()
</script>
<template>
    <div>
        <v-app-bar prominent class="bg-grey-lighten-5 static" tag="div">
            <v-toolbar-title>Admin</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn @click="router.push({ name: 'employee' })">Employees</v-btn>
        </v-app-bar>
    </div>

</template>