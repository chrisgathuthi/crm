<script setup>
import axios from 'axios';
import { useForm, useField } from 'vee-validate';
import * as yup from 'yup';
import { useToastStore } from '../stores/toast';
import { useRouter } from 'vue-router';
import { useBandwidth } from '../stores/bandwidth';
import { onMounted } from 'vue';
import BaseLayout from '../components/Layout/BaseLayout.vue';

const pageRouter = useRouter()
const toast = useToastStore()
const bandwidthStore = useBandwidth()

// load bandwidth
onMounted(() => {
    bandwidthStore.getBandwith()
})

function itemProps(item) {
    return {
        title: item,
    }
}
console.log(bandwidthStore.package)
const { errors, values, setErrors, handleSubmit } = useForm({
    validationSchema: yup.object({
        firstname: yup.string().required('First name is required'),
        lastname: yup.string().required('Last name is required'),
        location: yup.string().required('Location is required'),
        phonenumber: yup.string().matches(/^\+(?:[0-9] ?){6,14}[0-9]$/, "Start with +254").required('Phone number is required'),
        router: yup.string().required('Router is required'),
        serviceplan: yup.string().required('Service plan is required'),
        email: yup.string().email().required('Email is required'),
    })
});

const firstname = useField('firstname');
const lastname = useField('lastname');
const phonenumber = useField('phonenumber');
const email = useField('email');
const location = useField('location');
const router = useField('router');
const status = useField('status');
const bandwidth = useField('bandwidth');
const serviceplan = useField('serviceplan');

const submit = handleSubmit(async () => {
    const data = {
        first_name: values.firstname,
        last_name: values.lastname,
        phone_number: values.phonenumber,
        email: values.email,
        location: values.location,
        router: values.router,
        status: values.status,
        bandwidth: values.bandwidth,
        service_plan: values.serviceplan
    }
    await axios.post('/accounts/client/', data, { headers: { "Authorization": `Token ${localStorage.getItem("token")}` } })
        .then((resp) => {
            toast.showToast(3000, `${resp.data.first_name} registered successfully`, "success")
            pageRouter.push({ name: 'clients' })
        })
        .catch((errors) => {
            toast.showToast(3000, "An error occurred", "warning")
            console.log(errors.response.data)
            setErrors({
                firstname: errors.response.data.first_name,
                lastname: errors.response.data.last_name,
                phonenumber: errors.response.data.phone_number,
                email: errors.response.data.email,
                location: errors.response.data.location,
                router: errors.response.data.router,
                bandwidth: errors.response.data.bandwidth,
                serviceplan: errors.response.data.service_plan
            })
        })

    // alert(JSON.stringify(values))
})
</script>
<template>
    <BaseLayout>
        <template v-slot:pageMenu>
            <v-container>
                Client's Registration
            </v-container>
        </template>
        <template v-slot:childComponent>
            <v-sheet width="500" class="mx-auto overflow-auto">
                <v-form @submit.prevent="submit" title="Client Registrtion">
                    <v-responsive>
                        <v-text-field clearable variant="underlined" :error-messages="errors.firstname"
                            v-model="firstname.value.value" label="First name"></v-text-field>
                        <v-text-field clearable variant="underlined" :error-messages="errors.lastname"
                            v-model="lastname.value.value" label="Last name"></v-text-field>
                        <v-text-field clearable variant="underlined" :error-messages="errors.phonenumber"
                            v-model="phonenumber.value.value" label="Phone number"></v-text-field>
                        <v-text-field clearable variant="underlined" :error-messages="errors.email"
                            v-model="email.value.value" label=" Email"></v-text-field>
                        <v-text-field clearable variant="underlined" :error-messages="errors.location"
                            v-model="location.value.value" label=" location"></v-text-field>
                        <v-text-field clearable variant="underlined" :error-messages="errors.router"
                            v-model="router.value.value" label=" router"></v-text-field>
                        <v-select label="status" :items="['active', 'inactive']" variant="underlined"
                            v-model="status.value.value"></v-select>
                        <v-select label="service plan" :items="['static', 'hotspot', 'ppoe']" variant="underlined"
                            v-model="serviceplan.value.value"></v-select>
                        <v-select label="bandwidth" :items="bandwidthStore.package" :error-messages="errors.bandwidth"
                            v-model="bandwidth.value.value" :item-props="itemProps" variant="underlined"></v-select>

                        <v-container>
                            <v-btn type="submit" block class="mt-2">Submit</v-btn>
                        </v-container>
                    </v-responsive>
                </v-form>
            </v-sheet>

        </template>
    </BaseLayout>
</template>
<style scoped>
.v-btn {
    background-color: #00E676;
}
</style>