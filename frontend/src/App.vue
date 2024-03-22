<script setup>
import { RouterView } from 'vue-router'
import Toast from '@/components/Toast.vue'

</script>

<template>
  <VApp class="h-screen ">
    <v-layout>
      <v-main class="w-100">
        <RouterView />
      </v-main>
      <Toast />

    </v-layout>
  </VApp>
</template>

<style scoped>
a {
  color: #00E676;
  text-decoration: none;
}

a:hover {
  color: #06ac5b;
}

.active {
  color: #ffffff;
}

.v-app {
  height: 100vh;
}
.v-main{
  min-height: 100vh;
  overflow-y: scroll;
}
</style>