<script setup>
import axios from 'axios';
import { useForm, useField } from 'vee-validate';
import * as yup from 'yup';
import { useToastStore } from '../stores/toast';
import { useRouter } from 'vue-router';

const pageRouter = useRouter()
const toast = useToastStore()

const { errors, values, setErrors, handleSubmit } = useForm({
    validationSchema: yup.object({
        firstname: yup.string().required('First name is required'),
        lastname: yup.string().required('Last name is required'),
        location: yup.string().required('Location is required'),
        phonenumber: yup.string().matches(/^\+(?:[0-9] ?){6,14}[0-9]$/, "Start with +254").required('Phone number is required'),
        router: yup.string().required('Router is required'),
        serviceplan: yup.string().required('Service plan is required'),
        email: yup.string().email().required('Email is required'),
        password: yup.string().min(6, 'Password should be atleast 6 characters').required('Password is required'),
    })
});

const firstname = useField('firstname');
const lastname = useField('lastname');
const phonenumber = useField('phonenumber');
const password = useField('password');
const email = useField('email');
const location = useField('location');
const router = useField('router');
const serviceplan = useField('serviceplan');

const submit = handleSubmit(async () => {
    const data = {
        first_name: values.firstname,
        last_name: values.lastname,
        phone_number: values.phonenumber,
        password: values.password,
        email: values.email,
        location: values.location,
        router: values.router,
        service_plan: values.serviceplan
    }
    await axios.post('/accounts/client/', data)
        .then((resp) => { 
            toast.showToast(3000, `${resp.data.first_name} registered successfully`, "success") 
            pageRouter.push({name: 'clients'})
        })
        .catch((errors) => {
            toast.showToast(3000, "An error occurred", "warning")
            console.log(errors.response.data)
            setErrors({
                firstname: errors.response.data.first_name,
                lastname: errors.response.data.last_name,
                phonenumber: errors.response.data.phone_number,
                email: errors.response.data.email,
                password: errors.response.data.password,
                location: errors.response.data.location,
                router: errors.response.data.router,
                serviceplan: errors.response.data.service_plan
            })
        })

    // alert(JSON.stringify(values))
})
</script>
<template>
    <v-container>
        <v-sheet>
            <v-col class="font-weight-bold">
                Client's Registration
            </v-col>
        </v-sheet>
    </v-container>
    <v-sheet width="500" class="mx-auto">
        <v-form @submit.prevent="submit" title="Client Registrtion">
            <v-responsive>
                <v-text-field clearable variant="underlined" :error-messages="errors.firstname"
                    v-model="firstname.value.value" label="First name"></v-text-field>
                <v-text-field clearable variant="underlined" :error-messages="errors.lastname"
                    v-model="lastname.value.value" label="Last name"></v-text-field>
                <v-text-field clearable variant="underlined" :error-messages="errors.phonenumber"
                    v-model="phonenumber.value.value" label="Phone number"></v-text-field>
                <v-text-field clearable variant="underlined" :error-messages="errors.email" v-model="email.value.value"
                    label=" Email"></v-text-field>
                <v-text-field clearable variant="underlined" :error-messages="errors.password"
                    v-model="password.value.value" label=" password"></v-text-field>
                <v-text-field clearable variant="underlined" :error-messages="errors.location"
                    v-model="location.value.value" label=" location"></v-text-field>
                <v-text-field clearable variant="underlined" :error-messages="errors.router" v-model="router.value.value"
                    label=" router"></v-text-field>
                <v-select label="service plan" :items="['HOTSPOT', 'PPOE', 'STATIC']" :error-messages="errors.serviceplan"
                    v-model="serviceplan.value.value" variant="underlined"></v-select>

                <v-container>
                    <v-btn type="submit" block class="mt-2">Submit</v-btn>
                </v-container>
            </v-responsive>
        </v-form>
    </v-sheet>
</template>
<style scoped>
.v-btn {
    background-color: #00E676;
}
</style>