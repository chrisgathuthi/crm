<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useForm, useField } from 'vee-validate';
import * as yup from 'yup';
import { useToastStore } from '../stores/toast';
const toast = useToastStore()

const bandwidths = ref([])
const isLoading = ref(true)
onMounted(async () => {
    await axios.get("/accounts/bandwidths/", { headers: { Authorization: `Token ${localStorage.getItem("token")}` } })
        .then((response) => {
            bandwidths.value = response.data
            isLoading.value = false
        })
        .catch((error) => {
            console.log(error);
        })
})
// creating plan
const { errors, handleSubmit, values, resetForm, setErrors } = useForm({
    validationSchema: yup.object({
        name: yup.string().required(),
        size: yup.string().required()
    })
})
const name = useField("name")
const size = useField("size")

const sumbit = handleSubmit(async () => {
    await axios.post("/accounts/bandwidth/", { name: values.name, size: values.size }, { headers: { Authorization: `Token ${localStorage.getItem("token")}` } })
        .then((response) => {
            toast.showToast(3000, "plan created successfully", "success")
            resetForm()
            bandwidths.value.push(response.data)
        })
        .catch((error) => {
            console.log(error);
            setErrors({
                name: error.response.data.name,
                size: error.response.data.size
            })

        })

})


</script>
<template>
    <div class="plans mt-4">
        Your active data plans
    </div>
    <v-row class="mt-5">
        <v-col cols="auto" v-for="(bandwidth, index) in bandwidths" :key="index">
            <v-card height="100" width="150" class="rounded-te-xl">
                <v-card-title>
                    {{ bandwidth.name }}
                </v-card-title>
                <v-card-subtitle class="text-h6">
                    {{ bandwidth.size }} mbps
                </v-card-subtitle>
            </v-card>
        </v-col>
        <v-col cols="auto" v-if="isLoading">
            <v-card height="100" width="150">
                <v-progress-circular :size="50" color="primary" indeterminate></v-progress-circular>
                <v-card-subtitle>loading</v-card-subtitle>
            </v-card>

        </v-col>
    </v-row>
    <div class="heading mt-6">
        Create a new plan below
    </div>
    <div class="form">
        <v-form @submit.prevent="sumbit">
            <v-row>
                <v-col cols="4">
                    <v-text-field variant="outlined" v-model="name.value.value" :error-messages="errors.name" label="name"
                        type="text"></v-text-field>
                </v-col>
                <v-col cols="4">
                    <v-text-field variant="outlined" v-model="size.value.value" :error-messages="errors.size" label="size"
                        type="number"></v-text-field>
                </v-col>
                <v-col cols="auto" class="justify-center">
                    <v-btn block type="submit" variant="elevated" size="medium">Add</v-btn>
                </v-col>
            </v-row>
        </v-form>
    </div>
</template>