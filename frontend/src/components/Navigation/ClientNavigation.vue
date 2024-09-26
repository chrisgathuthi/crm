<script setup>
import { useRouter } from "vue-router";
const router = useRouter();
</script>

<template>
  <div>
    <v-app-bar class="bg-grey-lighten-5 border-b">
      <v-toolbar-title>Clients</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        color="primary"
        @click="router.push({ name: 'registration' })"
        prepend-icon="mdi-plus"
        class="mr-3"
        >add client</v-btn
      >
    </v-app-bar>
  </div>
</template>
