<script setup>
import { ref } from 'vue';

const dialog = ref(false)
const props = defineProps(["icon", "text", "title", "message"])
</script>
<template>
    <v-dialog v-model="dialog" activator="parent" width="auto">
        <v-card>
            <v-card-text>
                <v-alert type="props.icon" icon="props.icon" title="props.title"
                    text="props.message"></v-alert>
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" block @click="dialog = false;">OK</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>