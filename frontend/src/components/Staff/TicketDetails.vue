<script setup>
import axios from 'axios';
import { onBeforeMount, ref } from 'vue';
import { useRoute } from 'vue-router';


// route
const route = useRoute()

// fieldwork data
const fieldworkData = ref([])
onBeforeMount(async () => {
    await axios.get(`/accounts/fieldwork/${route.params.id}`, {
        headers: { Authorization: `Token ${localStorage.getItem("token")}` }
    })
        .then((response) => {            
            fieldworkData.value = response.data
        })
        .catch()
})

// searching material values
const inventories = ref([])

function searching(value) {
    
    axios.get(`/accounts/search-inventories/?search=${value}`, { headers: { Authorization: `Token ${localStorage.getItem("token")}` } })
        .then((response) => {          
            console.log(`response ${response.data[0].name}`);
              
            inventories.value = [response.data[0].name]
        })
        .catch((error) => {
            console.log(error);
        })
}
</script>
<template>
    <v-row class="pt-10">
        <v-col>
            <v-card min-height="350" class="pt-4">
                <v-card-item>
                    <v-form>
                        <v-row class="pt-4">
                            <v-col cols="8">
                                <v-autocomplete label="Material used" clearable hint="material used" variant="outlined" v-model="inventories"
                                    :items="inventories" @update:search="(value) => searching(value)">
                                </v-autocomplete>
                            </v-col>
                            <v-col cols="4">
                                <v-text-field label="size" hint="length" variant="outlined" type="number"></v-text-field>
                            </v-col>
                        </v-row>
                        <v-btn type="submit" prepend-icon="mdi mdi-plus" color="primary">materials</v-btn>
                    </v-form>
                </v-card-item>
            </v-card>
        </v-col>
        <v-col>
            <v-card min-height="350">
                <v-card-item>
                    <v-card-title>
                        {{ fieldworkData.task_name }}
                    </v-card-title>
                    <v-card-subtitle>
                        {{ fieldworkData.location }} | {{ fieldworkData.date }}
                    </v-card-subtitle>
                    <v-card-subtitle>{{ fieldworkData.isclosed }}</v-card-subtitle>
                </v-card-item>
                <v-card-text>
                    {{ fieldworkData.activities }}
                </v-card-text>
                <v-card-title>
                    Materials used
                    <ul class="pl-4">
                        <li></li>
                    </ul>
                </v-card-title>
                <div class="text-center">
                    <v-btn color="primary">close Ticket</v-btn>
                </div>
            </v-card>
        </v-col>
    </v-row>
</template>