<script setup>
import { useForm } from 'vee-validate';
import * as yup from 'yup';

const { errors,  defineInputBinds } = useForm({
    validationSchema: yup.object({
            firstname: yup.string().required('First name is required'),
            lastname: yup.string().required('Last name is required'),
            location: yup.string().required('Location is required'),
            phonenumber: yup.number().required('Phone number is required'),
            router: yup.string().required('Router is required'),
            serviceplan: yup.string().required('Service plan is required'),
            email: yup.string().email().required('Email is required'),
            password: yup.string().min(6, 'Password should be atleast 6 characters').required('Password is required'),
        })
});

const firstname = defineInputBinds('firstname');
const lastname = defineInputBinds('lastname');
const phonenumber = defineInputBinds('phonenumber');
const password = defineInputBinds('password');
const email = defineInputBinds('email');
const location = defineInputBinds('location');
const router = defineInputBinds('router');
const serviceplan = defineInputBinds('serviceplan');

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
        <v-form @submit.prevent title="Client Registrtion">
            <v-responsive>
                <v-text-field clearable variant="underlined" :error-messages="errors.firstname" v-bind="firstname"
                    label="First name"></v-text-field>
                <v-text-field clearable variant="underlined" :error-messages="errors.lastname" v-bind="lastname"
                    label="Last name"></v-text-field>
                <v-text-field clearable variant="underlined" :error-messages="errors.phonenumber" v-bind="phonenumber"
                    label="Phone number"></v-text-field>
                <v-text-field clearable variant="underlined" :error-messages="errors.email" v-bind="email"
                    label=" Email"></v-text-field>
                <v-text-field clearable variant="underlined" :error-messages="errors.password" v-bind="password"
                    label=" password"></v-text-field>
                <v-text-field clearable variant="underlined" :error-messages="errors.location" v-bind="location"
                    label=" location"></v-text-field>
                <v-text-field clearable variant="underlined" :error-messages="errors.router" v-bind="router"
                    label=" router"></v-text-field>
                <v-select label="Select" :items="['HOTSPOT', 'PPOE', 'STATIC']" :error-messages="errors.serviceplan"
                    v-bind="serviceplan" variant="underlined"></v-select>

                <v-container>
                    <v-btn type="submit" block class="mt-2">Submit</v-btn>
                </v-container>
            </v-responsive>
        </v-form>
</v-sheet></template>
<style scoped>.v-btn {
    background-color: #00E676;
}</style>