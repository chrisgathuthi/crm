<script setup>
import axios from 'axios';
import { useForm, useField } from 'vee-validate';
import * as yup from 'yup';

const { errors, handleSubmit } = useForm({
    initialValues: {
        to: 'everyone',
        date: new Date().toDateString

    },
    validationSchema: yup.object({
        to: yup.string().required(),
        message: yup.string().required(),
        date: yup.date().min("12/012/2023").required("schedule sms")
    })
})
const to = useField('to')
const message = useField('message')
const date = useField('date')

</script>
<template>
    <v-container>
        <v-form>
            <v-row cols="4">
                <v-col cols="4">
                    <v-select label="To" :items="['everyone',]" variant="underlined" v-model="to.value.value"
                        :error-messages="errors.to"></v-select>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="4">
                    <v-text-field label="schedule date & time*" :error-messages="errors.date" v-model="date.value.value" type="datetime-local  "
                        required></v-text-field>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="6">
                    <v-textarea class="bg-white" counter clearable :error-messages="errors.message" label="message"
                        v-model="message.value.value"></v-textarea>

                </v-col>
            </v-row>
            <v-row>
                <v-col cols="4">
                    <v-btn type=submit block class="bg-purple-darken-4">
                        send
                    </v-btn>

                </v-col>
            </v-row>
        </v-form>
    </v-container>
</template>