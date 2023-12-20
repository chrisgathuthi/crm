<script setup>
import { ref } from 'vue'
import { useForm, useField } from 'vee-validate'
import axios from 'axios'
import * as yup from 'yup'
import { useRouter } from 'vue-router'
import { useToastStore } from '../stores/toast.js'
import { storeToRefs } from 'pinia'

const show = ref(false)

const router = useRouter()
// toast store
const toast = useToastStore()

// form validation

const { errors, handleSubmit, values, resetForm, setErrors } = useForm({
    validationSchema: yup.object({
        name: yup.string().max(100).required("co. name is required"),
        location: yup.string().max(100).required("location phone number is required"),
        phonenumber: yup.string().matches(/^\+(?:[0-9] ?){6,14}[0-9]$/, "Start with +254").required('co. phone number is required'),
        orgEmail: yup.string().email().required("org. email is required"),
        shortCode: yup.string().min(7).max(7).required("your organisation short code is required"),

    })

})
const name = useField("name")
const location = useField("location")
const phonenumber = useField("phonenumber")
const orgEmail = useField("orgEmail")
const shortCode = useField("shortCode")

const submit = handleSubmit(async () => {
    const data = {
        name: values.name,
        location: values.location,
        phone_number: values.phonenumber,
        org_email: values.orgEmail,
        short_code: values.shortCode
    }
    const headers = {
        "Authorization": `Token ${localStorage.getItem('token')}`,
        // "Token": `Token ${localStorage.getItem('token')}`
    }
    await axios.post("/accounts/provider/", data, {headers:headers})
        .then((response) => {
            toast.showToast(3000,"ISP profile created successfully","success")
            router.push({name: "dashboard"})
            resetForm()
        })
        .catch((err) => {
            console.log(err);
        })
})
</script>

<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="6">
                <v-card class=" pa-4">
                    <div>
                        <p class="text-body-2">
                            Fill the form to create your ISP profile
                        </p>
                    </div>
                    <v-form class="mt-3" @submit.prevent="submit">
                        <v-text-field clearable color="primary" v-model="name.value.value" :error-messages="errors.name"
                            variant="outlined" label="company name" type="text"></v-text-field>
                        <v-text-field clearable color="primary" v-model="location.value.value"
                            :error-messages="errors.location" variant="outlined" label="company location"
                            type="text"></v-text-field>
                        <v-text-field clearable color="primary" v-model="phonenumber.value.value"
                            :error-messages="errors.phonenumber" variant="outlined" label="company phone number"
                            type="tel"></v-text-field>
                        <v-text-field clearable color="primary" v-model="orgEmail.value.value"
                            :error-messages="errors.orgEmail" variant="outlined" label="company email"
                            type="email"></v-text-field>
                        <v-text-field clearable color="primary" v-model="shortCode.value.value" counter
                            :error-messages="errors.shortCode" variant="outlined" label="company short code"
                            hint="mpesa/paybill number" type="text"></v-text-field>

                        <v-row justify="center">
                            <v-col cols="6">
                                <v-btn block type="submit" color="purple-accent-3">proceed</v-btn>
                            </v-col>
                        </v-row>

                    </v-form>
                </v-card>
            </v-col>
        </v-row>

    </v-container>
</template>