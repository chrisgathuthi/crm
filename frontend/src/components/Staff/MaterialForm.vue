<script setup>
import { useForm, useField } from 'vee-validate'
import * as yup from 'yup'
import axios from 'axios';
import { useToastStore } from '@/stores/toast';
const toast = useToastStore()

const props = defineProps(["fieldworkID"])

const { values, handleSubmit, errors, setErrors, resetForm } = useForm({

    validationSchema: yup.object({
        material: yup.string().required(),
        quantity: yup.number().integer().min(1).required()
    })
})
const material = useField("material")
const quantity = useField("quantity")

const submit = handleSubmit(async () => {
    axios.post("/accounts/material/", { name: values.material, quantity: values.quantity, fieldwork: props.fieldworkID }, { headers: { Authorization: `Token ${localStorage.getItem('token')}` } })
        .then(() => { toast.showToast(3000, 'failed to attach field materials', 'success'), resetForm()})
        .catch((error) => { 
            toast.showToast(3000, 'failed to attach field materials', 'warning')
            setErrors({
                username: error.response.data.name,
                password: error.response.data.quantity
            })
        })

})

</script>
<template>
    <v-divider class="my-3"></v-divider>
    <v-row>
        <v-col cols="12">
            <v-form @submit.prevent="submit">
                <v-table>
                    <thead class="bg-grey">
                        <th>#</th>
                        <th>Material</th>
                        <th>Size</th>
                    </thead>
                    <tbody id="tbody">
                        <tr>
                            <td>1</td>
                            <td><v-text-field :error-messages="errors.material" v-model="material.value.value"
                                    label="material" variant="underlined"></v-text-field></td>
                            <td><v-text-field :error-messages="errors.quantity" v-model="quantity.value.value"
                                    label="quantity" variant="underlined"></v-text-field></td>
                        </tr>
                    </tbody>
                </v-table>
                <v-row>
                    <v-col>
                        <v-btn elevation-1 block variant="outlined" class="w-50 my-3" prepend-icon="mdi-paperclip-plus"
                                        type="submit" >Materials</v-btn>

                    </v-col>
                </v-row>


            </v-form>
        </v-col>
    </v-row>
</template>
<!-- <template>
    <v-btn elevation-1 block variant="outlined" class="w-50 my-3" prepend-icon="mdi-paperclip-plus"
        type="submit">Materials</v-btn>
</template> -->