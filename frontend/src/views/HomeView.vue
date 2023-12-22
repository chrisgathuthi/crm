<script setup>
import Navigation from '@/components/Navigation.vue';
import {  RouterView } from 'vue-router'
</script>

<template>
     <Navigation/>
      <v-main>
        <RouterView />
      </v-main>
</template>
<style >
.v-layout{
  background: red;
  min-height: 100vh;
}
.v-main{
  overflow: scroll;
}
</style>