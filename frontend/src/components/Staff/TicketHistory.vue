<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
// import { SplitText } from '@/functions/SplitText';

const openTickets = ref([])
onMounted(async ()=>{
    await axios.get("/accounts/fieldwork/?isclosed=true",{headers: {Authorization: `Token ${localStorage.getItem("token")}`}})
    .then((response)=>{
        openTickets.value = response.data
    })
    .catch((error)=>{
        console.log(error);
    })
})
</script>
<template>
    <section>
        <v-table fixed hover>
            <thead>
                <tr>
                    <th>Task Name</th>
                    <th>Location</th>
                    <th>Nor Date</th>
                    <th>Status</th>
                    <th>Activites</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="data in openTickets" :key="data.id">
                    <td>{{ data.task_name }}</td>
                    <td>{{ data.location }}</td>
                    <td>{{ data.date }}</td>
                    <td>{{ data.isclosed }}</td>
                    <td> <p>{{ data.activities }}</p> </td>
                </tr>
            </tbody>
            
        </v-table>
    </section>
</template>