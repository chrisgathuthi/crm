<script setup>
import { useField, useForm } from 'vee-validate';
import * as yup from 'yup';
import { useToastStore } from '@/stores/toast';
import axios from 'axios';
import { onMounted, ref } from 'vue';

// toaster
const toast = useToastStore()

// load staff from api
const staff = ref([])
function unpackObjectToArray(object) {
    let array = []
    for (let element of object) {
        array.push(`${element.employee.first_name} ${element.employee.last_name}`)
    }
    return array
}

onMounted(() => {
    axios.get("/accounts/staffs/", { headers: { Authorization: `Token ${localStorage.getItem('token')}` } })
        .then((response) => {
            //   staff.value = response.data  
            staff.value = unpackObjectToArray(response.data)
        })
        .catch(() => {
            toast.showToast(2000, "An error occured", 'warning')
        })
})



const { errors, values, resetForm, setErrors, handleSubmit } = useForm({
    validationSchema: yup.object({
        taskname: yup.string().required("Task title required"),
        location: yup.string().required("Task location required e.g. Juja"),
        activities: yup.string().required("Outline activities e.g. line mintenance"),
        assignee: yup.string().required("Assignee required"),
        date: yup.date().required("Task execution date required")


    })

})
const taskname = useField('taskname');
const location = useField('location');
const activities = useField('activities');
const assignee = useField('assignee');
const date = useField('date');

const submit = handleSubmit(async () => {
    const data = {
        task_name: values.taskname,
        location: values.location,
        activities: values.activities,
        assignee: values.assignee,
        date: values.date,
    }
    await axios.post('/accounts/fieldwork/', data, { headers: { Authorization: `Token ${localStorage.getItem("token")}` } })
        .then((resp) => {
            toast.showToast(3000, `${resp.data.task_name} created successfully`, 'success')
            resetForm()
        })
        .catch((errors) => {
            toast.showToast(3000, "An error occurred", "warning")
            setErrors({
                taskname: errors.response.data.task_name,
                location: errors.response.data.location,
                activities: errors.response.data.activities,
                assignee: errors.response.data.assignee,
                date: errors.response.data.date,
            })
        })
})
</script>
<template>
    <v-sheet class="mx-auto overflow-auto elevation-1 pa-5 mt-4" tag="div" width="600" >
            <v-form @submit.prevent="submit" title="create field ticket">
                <v-text-field label="Task Name*" variant="underlined" clearable :error-messages="errors.taskname"
                    v-model="taskname.value.value" required></v-text-field>

                <v-text-field label="Location*" variant="underlined" required clearable :error-messages="errors.location"
                    v-model="location.value.value"></v-text-field>
                <v-textarea clearable variant="underlined" clear-icon="mdi-close-circle" label="Activites*" model-value="1. "
                    :error-messages="errors.activities" v-model="activities.value.value"></v-textarea>
                <v-select variant="underlined" :items="staff" label="Assignee*" required :error-messages="errors.assignee"
                    v-model="assignee.value.value"></v-select>
                <v-text-field label="Date*" variant="underlined" :error-messages="errors.date" v-model="date.value.value" type="date"
                    required></v-text-field>

                <small>*indicates required field </small>

                <v-spacer></v-spacer>
                <div class="text-center">
                    <v-btn color="blue-darken-1" type="submit">
                    submit
                </v-btn>

                </div>
            </v-form>
    </v-sheet>
</template>