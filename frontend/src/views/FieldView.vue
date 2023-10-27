<script setup>
import { ref } from 'vue';
import FieldWorkForm from '@/components/Dialog/FieldWorkForm.vue';

const dialog = ref(false)

</script>

<template>
    <v-card color="grey-lighten-4" flat height="auto" rounded="0">
        <v-toolbar density="comfortable">

            <v-toolbar-title>Field Tickets</v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn color="primary" @click="dialog = !dialog">
                    <v-icon icon="mdi-plus"></v-icon> <span>Tickets</span>
                    <FieldWorkForm :dialog="dialog"/>
                </v-btn>

            <v-btn class="text-none" stacked>
                <v-badge content="2" color="error">
                    <v-icon>mdi-bell-outline</v-icon>
                </v-badge>
            </v-btn>
        </v-toolbar>
    </v-card>
    

</template>