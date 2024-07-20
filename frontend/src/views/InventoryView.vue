
<script setup>
import BaseLayout from '@/components/Layout/BaseLayout.vue';
import InventoryNavigation from '@/components/Navigation/InventoryNavigation.vue';

</script>
<template>
    <Navigation/>
    <BaseLayout>
        <template v-slot:pageMenu>
            <InventoryNavigation/>
        </template>
        <template v-slot:childComponent>
        </template>
    </BaseLayout>
    
</template>