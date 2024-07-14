
<script setup>
import { RouterView } from 'vue-router';
import BaseLayout from '../components/Layout/BaseLayout.vue';
import InventoryNavigation from '../components/Navigation/InventoryNavigation.vue';

</script>
<template>
    <Navigation/>
    <BaseLayout>
        <template v-slot:pageMenu>
            <InventoryNavigation/>
        </template>
        <template>
            <RouterView/>
        </template>
    </BaseLayout>
    
</template>