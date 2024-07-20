<script setup>
import BaseLayout from '../components/Layout/BaseLayout.vue';
import StaffNavigation from '@/components/Navigation/StaffNavigation.vue';
</script>
<template>
    <BaseLayout>
        <template v-slot:pageMenu>

            <StaffNavigation />

        </template>
        <template v-slot:childComponent>
        </template>
    </BaseLayout>
</template>