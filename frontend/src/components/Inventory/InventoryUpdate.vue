<script setup>
import axios from 'axios';
import { useField, useForm } from 'vee-validate';
import { onBeforeMount, ref } from 'vue';
import { useRoute } from 'vue-router';
import * as yup from 'yup'

const inventoryData = ref([])



const route = useRoute()
onBeforeMount(async () => {
    await axios.get(`/accounts/inventory/${route.params.id}`, {
            headers: { Authorization: `Token ${localStorage.getItem("token")}` },
        })
        .then((response) => {
            this.inventories = response.data;
        })
        .catch();
})
const { handleSubmit, values, errors, resetForm } = useForm({
    validationSchema: yup.object({
        additionalStock: yup.number().default(0),
    })
})
const additionalStock = useField("additionalStock")
const submit = handleSubmit(async () => {
    const data = { additional_stock: values.additionalStock }
    await axios.patch(`/accounts/inventory/${route.params.id}/update/`, data, { headers: { Authorization: `Token ${localStorage.getItem("token")}` } })
        .then((response) => {
            inventoryData.value = response.data
            resetForm()
        })
        .catch()
})
</script>
<template>
    <v-row>
        <v-col>
            <v-card min-height="350">
                <v-card-item>
                    <v-card-title>
                        {{ inventoryData.name }}
                    </v-card-title>
                    <v-form @submit.prevent="submit">
                        <v-text-field label="Additional stock" v-model="additionalStock.value.value"
                            :error-messages="errors.additionalStock" clearable hint="additional stock"
                            type="text"></v-text-field>
                        <v-btn type="submit" prepend-icon="mdi mdi-plus" color="primary">stock</v-btn>

                    </v-form>
                </v-card-item>
            </v-card>
        </v-col>
        <v-col>
            <v-card min-height="350">
                <v-card-item>
                    <v-card-title>
                        {{ inventoryData.name }}
                    </v-card-title>
                    <v-card-subtitle>
                        status {{ inventoryData.status }}
                    </v-card-subtitle>
                </v-card-item>
                <v-card-text>
                    <h4>
                        Initial stock
                        {{ inventoryData.opening_stock }}
                    </h4>
                    <h4>
                        Last added stock {{ inventoryData.additional_stock }}
                    </h4>
                    <h4>
                        Out stock {{ inventoryData.out_stock }}
                    </h4>
                    <h4>
                        Remaining stock {{ inventoryData.remaining_stock }}
                    </h4>
                </v-card-text>
            </v-card>
        </v-col>
    </v-row>
</template>