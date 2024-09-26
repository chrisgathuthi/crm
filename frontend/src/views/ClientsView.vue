<script setup>
import BaseLayout from '../components/Layout/BaseLayout.vue';
import ClientList from '../components/client/ClientList.vue';
import ClientNavigation from '../components/Navigation/ClientNavigation.vue';
</script>
<template>
    <BaseLayout>
        <template v-slot:pageMenu>
            <ClientNavigation/>

        </template>
        <template v-slot:childComponent>
            <ClientList />

        </template>
    </BaseLayout>
</template>
<style scoped>
a {
    text-decoration: none;

}
</style>