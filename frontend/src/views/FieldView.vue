<script setup>
import BaseLayout from '../components/Layout/BaseLayout.vue';
import FieldWorkNavigation from '@/components/Navigation/FieldWorkNavigation.vue';
</script>

<template>
    <BaseLayout>
        <template v-slot:pageMenu>
            <FieldWorkNavigation/>
        </template>
        <template v-slot:childComponent>
        </template>
    </BaseLayout>
</template>