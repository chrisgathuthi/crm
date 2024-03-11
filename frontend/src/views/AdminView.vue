<script setup>
import AdminNavigtion from '../components/Navigation/AdminNavigtion.vue';
import BaseLayout from '../components/Layout/BaseLayout.vue';
</script>
<template>
    <BaseLayout>
        <template v-slot:pageMenu>
            <AdminNavigtion/>
        </template>
    </BaseLayout>
</template>