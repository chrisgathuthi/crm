<script setup>
import { useForm, useField } from 'vee-validate';
import * as yup from 'yup'
import { useToastStore } from '@/stores/toast';
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router';

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

    await axios.post('/token/', { username: values.username, password: values.password })
        .then((response) => {
            toast.showToast(2000, 'login successful', 'success')
            userStore.setToken(response.data)
            axios.defaults.headers.common['Authorized'] = 'Bearer ' + response.data.access
            resetForm()
            router.push('/')
        })
        .catch((error) => {
            toast.showToast(3000, 'Login unsuccessful', 'warning')
            console.log(error);
            setErrors({
                username: error.reponse.data.username,
                password: error.reponse.data.password
            })

        })

})

</script>
<template>
    <v-sheet class="mx-auto" width="70%">
        <v-form @submit.prevent="submit">
            <v-responsive>
                <v-text-field label="username*" :error-messages="errors.username" v-model="username.value.value" clearable
                    required></v-text-field>
                <v-text-field label="password*" :error-messages="errors.password" v-model="password.value.value"
                    type="password" clearable></v-text-field>
                <v-container>
                    <v-btn type="submit" class="bg-purple-darken-accent-4" elevation="4" block>Login
                    </v-btn>
                </v-container>
            </v-responsive>

        </v-form>
    </v-sheet>
</template>
