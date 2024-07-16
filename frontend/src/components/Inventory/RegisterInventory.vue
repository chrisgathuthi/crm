<script setup>
import { useForm, useField } from 'vee-validate';
import * as yup from 'yup'
import { ref } from 'vue';
import axios from 'axios';
import { useToastStore } from '@/stores/toast';

// toast
const toast = useToastStore()
// dialog
const dialog = ref(false)

const { errors, values, handleSubmit, resetForm, setErrors } = useForm({
    validationSchema: yup.object({
        name: yup.string().required(),
        openingStock: yup.string().required(),
        additionalStock: yup.number().default(0),
        outStock: yup.number().default(0),
    })
})
const name = useField('name')
const openingStock = useField('openingStock')
const additionalStock = useField('additionalStock')
const outStock = useField('outStock')

const submit = handleSubmit(async () => {
    // api call
    const data = {
        name: values.name,
        opening_stock: values.openingStock,
        additional_stock: values.additionalStock,
        out_stock: values.outStock
    }
    await axios.post("/accounts/inventory/", data, { headers: { Authorization: `Token ${localStorage.getItem("token")}` } })
        .then(() => {
            toast.showToast(3000, "stock item created successfully", "success")
            resetForm()
        })
        .catch((errors) => {
            toast.showToast(5000, "An error occurred fill the form correctly", "warning")
            setErrors({
                name: errors.data.response.name,
                openingStock: errors.data.response.openingStock,
                additionalStock: errors.data.response.additionalStock,
                outStock: errors.data.response.outStock,
            })
        })
})
</script>
<template>
    <div class="pa-4 text-center">
        <v-dialog v-model="dialog" max-width="800">
            <template v-slot:activator="{ props: activatorProps }">
                <v-btn class="text-none font-weight-regular" prepend-icon="mdi-account" text="Add inventory"
                    variant="tonal" v-bind="activatorProps"></v-btn>
            </template>

            <v-form @submit.prevent="submit">


                <v-card prepend-icon="mdi-account" title="Employee Registration">
                    <v-card-text>
                        <div class="text-right">
                            <v-btn prepend-icon="mdi mdi-window-close" text="close" color="red lighten-3"
                                variant="plain" @click="dialog = false"></v-btn>
                        </div>
                        <div>
                            <v-text-field label="Item name*" :error-messages="errors.name" v-model="name.value.value"
                                type="text" clearable required></v-text-field>
                            <v-text-field label="Opening stock*" :error-messages="errors.openingStock"
                                v-model="openingStock.value.value" type="text" clearable required></v-text-field>
                            <v-text-field label="Additional stock*" :error-messages="additionalStock.username"
                                v-model="additionalStock.value.value" type="text" clearable required></v-text-field>
                            <v-text-field label="Out Stock" type="email" :error-messages="errors.outStock"
                                v-model="outStock.value.value" clearable required></v-text-field>
                        </div>

                        <small class="text-caption text-medium-emphasis">*indicates required field</small>
                    </v-card-text>

                    <v-divider></v-divider>

                    <v-card-actions>
                        <v-spacer></v-spacer>

                        <v-btn text="Close" variant="plain" @click="dialog = false"></v-btn>

                        <v-btn color="primary" text="Save" variant="tonal" type="submit"></v-btn>
                    </v-card-actions>
                </v-card>
            </v-form>

        </v-dialog>
    </div>
</template>
