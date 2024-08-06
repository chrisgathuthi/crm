<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
// import { SplitText } from '@/functions/SplitText';

const openTickets = ref([])
onMounted(async ()=>{
    await axios.get("/accounts/fieldwork/?isclosed=false",{headers: {Authorization: `Token ${localStorage.getItem("token")}`}})
    .then((response)=>{
        openTickets.value = response.data
    })
    .catch((error)=>{
        console.log(error);
    })
})
// routing
const router = useRouter()

</script>
<template>
    <section>
        <v-table fixed hover>
            <thead>
                <tr>
                    <th>Task Name</th>
                    <th>Location</th>
                    <th>Date</th>
                    <th>Status</th>
                    <th>Assignee</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="data in openTickets" :key="data.id" @click="router.push({name: 'staffTicketDetails', params: { id: `${data.id}` }})">
                    <td>{{ data.task_name }}</td>
                    <td>{{ data.location }}</td>
                    <td>{{ data.date }}</td>
                    <td>{{ data.isclosed }}</td>
                    <td>{{ data.assignee }}</td>
                </tr>
            </tbody>
            
        </v-table>
    </section>
</template>