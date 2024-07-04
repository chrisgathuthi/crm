<script setup>

import { useToastStore } from '@/stores/toast';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import RegisterEmployee from './Employee/RegisterEmployee.vue';
import { useRouter } from 'vue-router';


const router = useRouter()
// toast
const toast = useToastStore()

const userData = ref([])

onMounted(async () => {
    await axios.get("/accounts/staffs/", { headers: { Authorization: `Token ${localStorage.getItem("token")}` } })
        .then(response => {
            userData.value = response.data
        })
        .catch(error => {
            console.log(error);
            toast.showToast(4000, "An error occured", "warning")
        })
})

</script>
<template>
    <v-row class="mt-10">
        <v-col>
            <RegisterEmployee />
        </v-col>
    </v-row>

    <v-row>
        <v-col>
            <div class="table">
                <v-table fixed-header>
                    <thead>
                        <tr>
                            <th scope="col">Username</th>
                            <th scope="col">Email</th>
                            <th scope="col">ID no</th>
                            <th scope="col">Job title</th>
                            <th scope="col">Salary</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="data in userData" :key="data.id"
                            @click="router.push({ name: 'employeeDetail', params: { id: `${data.id}` } })">
                            <td>{{ data.employee.username }}</td>
                            <td>{{ data.employee.email }}</td>
                            <td>{{ data.identification_number }}</td>
                            <td>{{ data.job_title }}</td>
                            <td>{{ data.salary }}</td>
                        </tr>
                    </tbody>
                </v-table>
            </div>
        </v-col>
    </v-row>
</template>
<style scoped>
tr:hover {
    background-color: aqua;
    cursor: pointer;

}
</style>