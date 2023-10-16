<script setup>
import axios from 'axios';
import { ref, onBeforeMount, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const client = ref()
const route = useRoute()
const router = useRouter()
console.log("The route",route)
console.log("The router",router)

const { id } = route.params

onBeforeMount(() => {
    axios.get(`/accounts/client/${id}`)
        .then((resp) => client.value = resp.data)
        .catch((error) => console.log(error))
})
</script>
<template>
    <v-card width="500">
        <v-card-item>
            <v-card-tile style="font-weight: bold;">{{ client.first_name }} {{ client.last_name }}</v-card-tile>
            <v-card-text>
                <v-container>
                    <v-row>
                        <v-col title="location">Location {{ client.location }}</v-col>
                    </v-row>
                    <v-row>
                        <v-col title="Phone number">Phone number {{ client.phone_number }}</v-col>
                    </v-row>
                    <v-row>
                        <v-col title="Password">Password {{ client.password }}</v-col>
                    </v-row>
                    <v-row>
                        <v-col title="email">E-mail {{ client.email }}</v-col>
                    </v-row>
                    <v-row>
                        <v-col title="router">Router {{ client.router }}</v-col>
                    </v-row>
                    <v-row>
                        <v-col title="service plan">Service plan {{ client.service_plan }}</v-col>
                    </v-row>
                    <v-row>
                        <v-col title="registration">Registration date {{ client.registration_date }}</v-col>
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