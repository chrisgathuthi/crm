<script setup>
import { useForm, useField } from 'vee-validate';
import * as yup from 'yup'
import { useToastStore } from '@/stores/toast';
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router';
import {ref} from 'vue'

const toast = useToastStore()
const userStore = useUserStore()

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

    await axios.post('/accounts/employee/', { username: values.username, password: values.password })
        .then((response) => {
            toast.showToast(2000, 'login successful', 'success')
            resetForm()
        })
        .catch((error) => {
            toast.showToast(3000, 'Login unsuccessful', 'warning')
            setErrors({
                username: error.response.data.username,
                password: error.response.data.password
        })

    })

})
ref
</script>
<template>
    <v-row justify="center" class="align-center" >
        <v-col cols="6" class="elevation-1">
            <v-form @submit.prevent="submit" class="py-4">
                <v-text-field label="username*" :error-messages="errors.username" v-model="username.value.value" clearable prepend-icon="mdi-account" variant="underlined"
                    required></v-text-field>
                <v-text-field label="password*" :error-messages="errors.password" v-model="password.value.value" prepend-icon="mdi-lock" variant="underlined"
                    type="password" clearable></v-text-field>
                    <v-btn type="submit" color="purple-accent-3" class="w-25" elevation-1  block>save
                    </v-btn>
            </v-form>

        </v-col>
    </v-row>
</template>
