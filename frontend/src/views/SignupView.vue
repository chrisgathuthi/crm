<script setup>
import { ref } from 'vue'
import Timeline from '@/components/Timeline.vue'
import { useForm, useField } from 'vee-validate'
import axios from 'axios'
import * as yup from 'yup'
import { useRouter } from 'vue-router'

const show = ref(false)

const router = useRouter()
// form validation

const { errors, handleSubmit, values, resetForm, setErrors } = useForm({
    validationSchema: yup.object({
        username: yup.string().required("username is required"),
        email: yup.string().email().required(),
        password: yup.string().min(8, "password is too short").required(),
        password2: yup.string().min(8, "password is too short").oneOf([yup.ref("password"), null]).required()

    })

})
const username = useField("username")
const email = useField("email")
const password = useField("password")
const password2 = useField("password2")
const submit = handleSubmit(async () => {
    await axios.post("/accounts/registration/", values)
        .then((response) => {
            localStorage.setItem("token", response.data.token)
            resetForm()
            router.push({name: 'partner-setup'})
        })
        .catch((errors) => {
            console.log(errors.response.data);
            setErrors({
                username: errors.response.data.username,
                email: errors.response.data.email,
                password: errors.response.data.password
            })

    })

})
</script>
<template>
    <v-container>
        <v-row justify="center">
                <v-col cols="6">
                    <Timeline />
                </v-col>
                <v-col cols="6" class="gap-3">
                    <v-card class="bg-white pa-2" min-height="80vh" rounded>
                        <div>
                            <div class="text-h5 justify-center ">Welcome to Lamp connect</div>
                            <div class="text-h6 justify-center mt-2">Your trusted ISP CRM software</div>
                        </div>
                        <v-form class="bg-white mt-6" @submit.prevent="submit">
                            <v-text-field clearable color="primary" v-model="username.value.value"
                                :error-messages="errors.username" variant="outlined" label="username"
                                type="text"></v-text-field>
                            <v-text-field clearable color="primary" v-model="email.value.value"
                                :error-messages="errors.email" variant="outlined" label="email" type="email"></v-text-field>
                            <v-text-field v-model="password.value.value" :error-messages="errors.password"
                                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'" color="primary"
                                :type="show ? 'text' : 'password'" label="Password" hint="At least 8 characters" counter
                                @click="show = !show" variant="outlined"></v-text-field>
                            <v-text-field v-model="password2.value.value" :error-messages="errors.password2" color="primary"
                                :type="show ? 'text' : 'password'" label="Password" hint="At least 8 characters" counter
                                variant="outlined"></v-text-field>
                            <v-row justify="center">
                                <v-col cols="6">
                                    <v-btn block type="submit" color="purple-accent-3">Register</v-btn>
                                </v-col>
                            </v-row>
                        </v-form>
                </v-card>
            </v-col>
    </v-row>
</v-container></template>
<style scoped>
@media screen and (max-width: 600px) {
    .v-row{
        flex-direction: column-reverse;
    }
    .v-col-6{
        width: 100%;
    }
    
}
</style>