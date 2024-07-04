<script setup>
import { useForm, useField } from 'vee-validate';
import * as yup from 'yup'
import { ref } from 'vue';
import axios from 'axios';
import { useToastStore } from '@/stores/toast';

// toast
const toast = useToastStore()
// dialog
const dialog = ref(false)

const { errors, values, handleSubmit, resetForm, setErrors } = useForm({
    validationSchema: yup.object({
        username: yup.string().required(),
        email: yup.string().required(),
        password1: yup.string().min(6).required(),
        firstName: yup.string().required(),
        lastName: yup.string().required(),
        password2: yup.string().min(6).required(),
        identificationNumber: yup.number().required(),
        jobTitle: yup.string().required(),
        salary: yup.string().required(),

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
    await axios.post("/accounts/staff/", data, { headers: { Authorization: `Token ${localStorage.getItem("token")}` } })
        .then(() => {
            toast.showToast(3000, "staff profile created successfully", "success")
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
    <div class="pa-4 text-center">
        <v-dialog v-model="dialog" max-width="800">
            <template v-slot:activator="{ props: activatorProps }">
                <v-btn class="text-none font-weight-regular" prepend-icon="mdi-account" text="Add Employee"
                    variant="tonal" v-bind="activatorProps"></v-btn>
            </template>

            <v-form @submit.prevent="submit">


                <v-card prepend-icon="mdi-account" title="Employee Registration">
                    <v-card-text>
                        <div class="text-right">
                            <v-btn prepend-icon="mdi mdi-window-close" text="close" color="red lighten-3" variant="plain" @click="dialog = false"></v-btn>
                        </div>
                        <div>
                            <v-text-field label="First Name*" :error-messages="errors.firstName"
                                v-model="firstName.value.value" type="text" clearable required></v-text-field>
                            <v-text-field label="Last Name*" :error-messages="errors.lastName"
                                v-model="lastName.value.value" type="text" clearable required></v-text-field>
                            <v-text-field label="Username*" :error-messages="errors.username"
                                v-model="username.value.value" type="text" clearable required></v-text-field>
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

                        <v-btn text="Close" variant="plain" @click="dialog = false"></v-btn>

                        <v-btn color="primary" text="Save" variant="tonal" type="submit"></v-btn>
                    </v-card-actions>
                </v-card>
            </v-form>

        </v-dialog>
    </div>
</template>
