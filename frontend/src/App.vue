<script setup>
import { RouterView} from 'vue-router'
import Toast from '@/components/Toast.vue'
</script>

<template>
  <VApp style="width: 100%; height: 100vh;" >
    <v-container>
      <RouterView/>
      <Toast/>
    </v-container>
  </VApp>
</template>

<style scoped>

a{
  color: #00E676;
  text-decoration: none;
}
a:hover{
  color: #06ac5b;
}
.active{
  color: #ffffff;
}

</style>