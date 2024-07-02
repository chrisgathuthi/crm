<script setup>
import { useForm, useField } from 'vee-validate';
import * as yup from 'yup'
import { useToastStore } from '@/stores/toast';
import axios from 'axios';
import { onMounted, ref } from 'vue';


const toast = useToastStore()

const userData = ref([])

onMounted(async ()=>{
    await axios.get("/accounts/staffs/", {headers: {Authorization: `Token ${localStorage.getItem("token")}`}})
            .then(response =>{
                userData.value = response.data
            })
            .catch(error =>{
                console.log(error);
                toast.showToast(4000, "An error occured", "warning")
            })
})

</script>
<template>
    <v-row>
        <v-col>
            <div class="table">
                <v-table fixed-header>
                    <thead>
                        <tr>
                            <th>Username</th>
                            <th>Email</th>
                            <th>ID no</th>
                            <th>Job title</th>
                            <th>Salary</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="data in userData" :key="data.id">
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
tr:hover{
    background-color: aqua;
    cursor: pointer;

}
</style>