<script setup>
import {  computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useClientStore } from "../stores/client";
import ClientDeleteDialog from './Dialog/ClientDeleteDialog.vue';

const route = useRoute()
const router = useRouter()
const store = useClientStore()

const selectedClient = computed(() =>{
    return store.clients.find((item) => item.id === Number(route.params.id))
})
</script>
<template>
    <v-card width="500">
        <v-card-item>
            <v-card-tile style="font-weight: bold;">{{ selectedClient.first_name }} {{ selectedClient.last_name }}</v-card-tile>
            <v-card-text>
                <v-container>
                    <v-row>
                        <v-col title="location">Location {{ selectedClient.location }}</v-col>
                    </v-row>
                    <v-row>
                        <v-col title="Phone number">Phone number {{ selectedClient.phone_number }}</v-col>
                    </v-row>
                    <v-row>
                        <v-col title="Password">Password {{ selectedClient.password }}</v-col>
                    </v-row>
                    <v-row>
                        <v-col title="email">E-mail {{ selectedClient.email }}</v-col>
                    </v-row>
                    <v-row>
                        <v-col title="router">Router {{ selectedClient.router }}</v-col>
                    </v-row>
                    <v-row>
                        <v-col title="service plan">Service plan {{ selectedClient.service_plan }}</v-col>
                    </v-row>
                    <v-row>
                        <v-col title="registration">Registration date {{ selectedClient.registration_date }}</v-col>
                    </v-row>
                </v-container>
            </v-card-text>
        </v-card-item>
        <v-card-action>
            <div class="links">
            <v-btn>
                <v-icon icon="mdi-delete" style="color: #D50000;">
                </v-icon>
                Delete
             <ClientDeleteDialog :id="selectedClient.id"/>
            </v-btn>
            <v-btn>
                <v-icon icon="mdi-square-edit-outline" style="color: #00E676;">
                </v-icon>
                Edit
            </v-btn>
            <v-btn @click="router.back()">
                <v-icon icon="mdi-arrow-left" style="color: #212121;">
                </v-icon>
                Back
            </v-btn>
            </div>
 

        </v-card-action>
    </v-card>
</template>