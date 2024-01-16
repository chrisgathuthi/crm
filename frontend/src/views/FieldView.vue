<script setup>
import { ref, onMounted } from 'vue';
import FieldWorkForm from '@/components/Dialog/FieldWorkForm.vue';
import { useFieldWorkStore } from '@/stores/fieldwork.js'
import { useToastStore } from '../stores/toast'
import { Converter } from '@/functions/DateConverter'
import Navigation from '../components/Navigation.vue';
import axios from 'axios';

const dialog = ref(false)

const toast = useToastStore()


// api call
const store = useFieldWorkStore()

// load before create phase
onMounted(async () => {
    await store.getFieldWorkList()

})
// show summary
const expand = ref(false)

// show search

// update the status
async function closeTicket(id) {
    await axios.patch(`/accounts/fieldwork/${id}/`, { isclosed: true }, { headers: { Authorization: `Token ${localStorage.getItem("token")}` } })
        .then((response) => {
            console.log(response);
            toast.showToast(3000, "ticket closed", "success")
        })
        .catch((error) => {
            console.log(error);
            toast.showToast(3000, "an error occurred", "warning")
        })

}
</script>

<template>
    <!-- navigation -->
    <v-row>
        <v-col cols="3">
            <Navigation />
        </v-col>
        <v-col cols="9">
            <v-toolbar density="comfortable">

                <v-toolbar-title>Field Tickets</v-toolbar-title>

                <v-spacer></v-spacer>

                <v-divider vertical></v-divider>


                <v-divider vertical></v-divider>
                <v-btn color="primary" @click="dialog = !dialog" prepend-icon="mdi-plus" class="mr-3">
                    Tickets
                    <FieldWorkForm :dialog="dialog" />
                </v-btn>
                <v-divider vertical></v-divider>

                <v-btn class="text-none" stacked>
                    <v-badge content="2" color="error">
                        <v-icon>mdi-bell-outline</v-icon>
                    </v-badge>
                </v-btn>
            </v-toolbar>
            <!-- fieldwork data grid -->
            <v-row class="mt-8">
                <v-col>
                    <div class="subtitle">
                        Open Tickets
                    </div>
                </v-col>
            </v-row>

            <v-container v-for="(item, index) in store.fieldworks" :key="index" v-if="store.fieldworks.length > 0">
                <v-card max-width="350" elevation="4">
                    <v-card-item>
                        <v-card-title>
                            {{ item.task_name }}
                        </v-card-title>
                        <v-card-subtitle>
                            <v-row>
                                <v-col cols="auto">
                                    {{ item.assignee }}
                                </v-col>
                                <v-divider vertical></v-divider>
                                <v-col cols="auto">
                                    {{ Converter(item.date) }}
                                </v-col>
                                <v-col cols="auto">
                                    status
                                    <v-icon icon="mdi-circle-small" size="x-large" color="green-darken-2"></v-icon>
                                </v-col>
                            </v-row>
                        </v-card-subtitle>

                        <v-card-actions>
                            <v-btn @click="expand = !expand" class="bg-purple-accent-3"
                                :append-icon="expand ? 'mdi-chevron-up' : 'mdi-chevron-down'">
                                {{ !expand ? 'Read more' : 'Read less' }}
                            </v-btn>
                        </v-card-actions>

                        <v-expand-transition>
                            <div class="summary" v-show="expand">
                                <v-card-text>
                                    {{ item.activities }}

                                </v-card-text>
                                <v-card-action class="w-25">
                                    <button @click="closeTicket(item.id)" type="button" block size="large" variant="outlined" elevation-1 class="border">close</button>
                                </v-card-action>
                            </div>
                        </v-expand-transition>
                    </v-card-item>
                </v-card>
            </v-container>
            <v-container v-else>
                <h3>Hoorah! no Fieldwork Tickets</h3>

            </v-container>
        </v-col>
    </v-row>
</template>