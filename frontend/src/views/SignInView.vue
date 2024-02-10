<script setup>
import { useForm, useField } from 'vee-validate';
import * as yup from 'yup'
import { useToastStore } from '@/stores/toast';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { ref } from 'vue'

// toggle password view
const hideInputField = ref(true)

const toast = useToastStore()

const router = useRouter()

const { errors, values, handleSubmit, resetForm, setErrors } = useForm({
    validationSchema: yup.object({
        username: yup.string().required('username required'),
        password: yup.string().min(6, 'your password should be atleast 6 characters').required('password required'),
    })
})
const username = useField('username')
const password = useField('password')

const submit = handleSubmit(async () => {

    await axios.post('/accounts/login/', { username: values.username, password: values.password })
        .then((response) => {
            localStorage.setItem("token", response.data.token)
            toast.showToast(2000, 'login successful', 'success')
            resetForm()
            router.push({name:"dashboard"})
        })
        .catch((error) => {
            toast.showToast(3000, 'Login unsuccessful', 'warning')
            setErrors({
                username: error.response.data.username,
                password: error.response.data.password
            })

        })

})
</script>
<template>
    <v-row justify="center" class="align-center">
        <v-col cols="6" class="elevation-1">
            <div class="text-h5">
                <div class="d-inline-flex justify-center align-center"><v-img src="logo.svg" height="64" width="64"></v-img><h3>Lamp</h3></div>
            </div>
            <v-form @submit.prevent="submit" class="py-4">
                <v-text-field label="username*" :error-messages="errors.username" v-model="username.value.value" clearable
                    prepend-icon="mdi-account" variant="underlined" required></v-text-field>
                <v-text-field label="password*" :error-messages="errors.password" v-model="password.value.value"
                    prepend-icon="mdi-lock" variant="underlined" :type="hideInputField ? 'password' : 'text'"
                    append-inner="mdi-eye-off" @click="isHidden = !isHidden" clearable></v-text-field>
                <v-row justify="center">
                    <v-col cols="4">
                        <v-btn type="submit" color="purple-accent-3" elevation-1 block>Login</v-btn>
                    </v-col>
                </v-row>
                <div class="forgot mt-2">
                    <span role="link" class="text-gray">forgot password?</span>
                </div>
            </v-form>

        </v-col>
    </v-row>
</template>
