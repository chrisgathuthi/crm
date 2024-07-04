<script setup>
import axios from 'axios';
import { onBeforeMount, reactive, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import { useForm, useField } from 'vee-validate';
import * as yup from 'yup'
import { useToastStore } from '@/stores/toast';

// toast
const toast = useToastStore()
// dialog

const router = useRouter()
const route = useRoute()
const initialEmployeeInformation = reactive({ username: 'Timothy', email: '', firstName: '', lastName: '', identificationNumber: '', jobTitle: '', salary: '' })

onBeforeMount(async () => {
    await axios.get(`/accounts/staff/${route.params.id}/`, { headers: { Authorization: `Token ${localStorage.getItem("token")}` } })
        .then((response) => {
            initialEmployeeInformation.username = response.data.employee.username
            initialEmployeeInformation.email = response.data.employee.email
            initialEmployeeInformation.firstName = response.data.employee.first_name
            initialEmployeeInformation.lastName = response.data.employee.last_name
            initialEmployeeInformation.identificationNumber = response.data.identification_number
            initialEmployeeInformation.jobTitle = response.data.job_title
            initialEmployeeInformation.salary = response.data.salary
        })
        .catch(() => {
            toast.showToast(4000, "An error occurred, kindly contanct the administrator", "error")
        })


})
// watch for initial state change
watch(initialEmployeeInformation, () => {
    resetForm({
        values: {
            username: initialEmployeeInformation.username,
            email: initialEmployeeInformation.email,
            password1: initialEmployeeInformation.password1,
            firstName: initialEmployeeInformation.firstName,
            lastName: initialEmployeeInformation.lastName,
            password2: initialEmployeeInformation.password2,
            identificationNumber: initialEmployeeInformation.identificationNumber,
            jobTitle: initialEmployeeInformation.jobTitle,
            salary: initialEmployeeInformation.salary,
        }
    })
})
// updating employee information
const { errors, values, handleSubmit, resetForm, setErrors } = useForm({
    initialValues: {
        username: initialEmployeeInformation.username
    },
    validationSchema: yup.object({
        username: yup.string(),
        email: yup.string(),
        password1: yup.string().min(6),
        firstName: yup.string(),
        lastName: yup.string(),
        password2: yup.string().min(6),
        identificationNumber: yup.number(),
        jobTitle: yup.string(),
        salary: yup.string(),

    })
})
const username = useField('username')
const email = useField('email')
const firstName = useField('firstName')
const lastName = useField('lastName')
const password1 = useField('password1')
const password2 = useField('password2')
const identificationNumber = useField('identificationNumber')
const jobTitle = useField('jobTitle')
const salary = useField('salary')

const submit = handleSubmit(async () => {
    const data = {
        employee: {
            username: values.username,
            email: values.email,
            password: values.password1,
            first_name: values.firstName,
            last_name: values.lastName
        },
        identification_number: values.identificationNumber,
        job_title: values.jobTitle,
        salary: values.salary
    }
    // api call
    await axios.patch(`/accounts/staff/change/${route.params.id}/`, data, { headers: { Authorization: `Token ${localStorage.getItem("token")}` } })
        .then(() => {
            toast.showToast(3000, "staff profile information updated successfully", "success")
            router.push({ name: 'employee' })
            resetForm()
        })
        .catch((errors) => {
            toast.showToast(5000, "An error occurred fill the form correctly", "warning")
            setErrors({
                firstName: errors.data.response.firstName,
                lastName: errors.data.response.lastName,
                username: errors.data.response.username,
                email: errors.data.response.email,
                password1: errors.data.response.password,
                identificationNumber: errors.data.response.identification_number,
                jobTitle: errors.data.response.job_title,
                salary: errors.data.response.salary,
            })
        })
})

</script>
<template>
    <div>
        <v-form @submit.prevent="submit">


            <v-card prepend-icon="mdi-account" title="Employee Registration">
                <v-card-text>
                    <div>
                        <v-text-field label="First Name*" :error-messages="errors.firstName"
                            v-model="firstName.value.value" type="text" clearable required></v-text-field>
                        <v-text-field label="Last Name*" :error-messages="errors.lastName"
                            v-model="lastName.value.value" type="text" clearable required></v-text-field>
                        <v-text-field label="Username*" :error-messages="errors.username" v-model="username.value.value"
                            type="text" clearable required></v-text-field>
                        <v-text-field label="E-mail" type="email" :error-messages="errors.email"
                            v-model="email.value.value" clearable required></v-text-field>
                        <v-text-field label="Password" type="password" :error-messages="errors.password1"
                            v-model="password1.value.value" clearable required></v-text-field>
                        <v-text-field label="Confirm Password*" type="password" :error-messages="errors.password2"
                            v-model="password2.value.value" clearable required></v-text-field>
                        <v-text-field label="ID /Passport no" type="text" required
                            :error-messages="errors.identificationNumber" v-model="identificationNumber.value.value"
                            clearable></v-text-field>
                        <v-text-field label="Salary" type="text" required :error-messages="errors.salary"
                            v-model="salary.value.value" clearable></v-text-field>
                        <v-text-field label="Job Title" type="text" required :error-messages="errors.jobTitle"
                            v-model="jobTitle.value.value" clearable></v-text-field>

                    </div>

                    <small class="text-caption text-medium-emphasis">*indicates required field</small>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text="Save" variant="tonal" type="submit"></v-btn>
                </v-card-actions>
            </v-card>
        </v-form>


    </div>
</template>