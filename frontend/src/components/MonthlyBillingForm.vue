<script setup>
import axios from 'axios';
import { useForm, useField } from 'vee-validate';
import * as yup from 'yup';

import { useShortMessageStore } from '../stores/shortmessage'
import { useToastStore } from '../stores/toast'
import { onMounted } from 'vue';

import { Converter } from "@/functions/DateConverter";


// stores
const store = useShortMessageStore()
const toast = useToastStore()


// nessages history
onMounted(async () => {
    store.getMessages()
})

const { errors, values, handleSubmit, resetForm, setErrors } = useForm({
    initialValues: {
        to: 'everyone',
        // date: new Date().toDateString()

    },
    validationSchema: yup.object({
        to: yup.string().required(),
        message: yup.string().required(),
        date: yup.date().min(new Date().toDateString(), "Scheduled time must not be ealier than today").required("schedule sms")
    })
})
const to = useField('to')
const message = useField('message')
const date = useField('date')

const submit = handleSubmit(async () => {

    const data = {
        to: values.to,
        from: values.from,
        message: values.message,
        schedule_time: values.date
    }
    await axios.post("/accounts/shortmessage/", data, { headers: { "Authorization": `Token ${localStorage.getItem('token')}` } })
        .then((response) => {
            response.data
            toast.showToast(3000, "sms task scheduled successfully", "success")
            resetForm()

        })
        .catch((error) => {
            setErrors({
                to: error.response.data.to,
                schedule_time: error.response.data.schedule_time,
                message: error.response.data.message,
            })

        })
    })

</script>
<template>
    <div class="wrapper">
        <div class="container">
            <h4>send bulk sms</h4>

            <v-form class="mt-3" @submit.prevent="submit">
                <v-row>
                    <v-col cols="12">
                        <v-select label="To" :items="['everyone',]" variant="underlined" v-model="to.value.value"
                            :error-messages="errors.to"></v-select>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12">
                        <v-text-field label="schedule date & time*" :error-messages="errors.date" v-model="date.value.value"
                            type="datetime-local" hint="set future date and time" :min="new Date().toDateString()" required></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12">
                        <v-textarea class="bg-white" counter clearable :error-messages="errors.message" label="message"
                            v-model="message.value.value"></v-textarea>

                    </v-col>
                </v-row>
                <v-row justify="center">
                    <v-col cols="8">
                        <v-btn type=submit block class="bg-purple-darken-4">
                            send
                        </v-btn>

                    </v-col>
                </v-row>
            </v-form>

        </div>
        <div class="continer border-l">
            <div class="text-body">
                <h4>Message history</h4>
                <v-infinite-scroll :height="300">
                    <v-timeline side="end">
                        <v-timeline-item v-for="item in store.messages" :key="item.id"
                            dot-color="primary" size="small">
                            <v-card max-width="400">
                                <v-card-item>
                                    <v-card-title>{{ Converter(item.schedule_time)}}</v-card-title>
                                    <v-card-subtitle :class="text-success ? '{{ item.is_sent }}' : 'text-red'">{{item.is_sent ? 'sent' : 'not sent'}}</v-card-subtitle>
                                </v-card-item>
                                <v-card-text>
                                    {{item.message}}
                                </v-card-text>
                            </v-card>
                        </v-timeline-item>
                        <v-timeline-item v-if="store.messages < 1">
                            <v-card>
                                <v-card-text>
                                    No previous sms history
                                </v-card-text>
                            </v-card>
                        </v-timeline-item>
                    </v-timeline>

                </v-infinite-scroll>



            </div>
        </div>
    </div>
</template>
<style scoped>
.wrapper {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
}
</style>