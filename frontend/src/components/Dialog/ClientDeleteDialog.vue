<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const dialog = ref(false)
const props = defineProps(["id"])
const router = useRouter()

const deleteClient = (id) => {
    axios.delete(`/accounts/client/${parseInt(id)}`)
        .then((resp) => console.log(resp.data))
        .catch((error) => console.log(error))
}

</script>
<template>
    <v-dialog v-model="dialog" activator="parent" width="auto">
        <v-card>
            <v-card-text>
                <v-alert type="warning" icon="$warning" title="Delete client record"
                    text="Are you sure you want to delete? Please note this operation cannot be undone!"></v-alert>
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" block @click="dialog = false; deleteClient(props.id); router.push({name: 'clients'}) ">Delete</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>
