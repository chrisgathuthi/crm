<script setup>
import { onMounted, watchEffect} from 'vue';
import { useTransactionStore } from '@/stores/transaction'
import MpesaTransactions from './Billing/MpesaTransactions.vue';

const store = useTransactionStore()

onMounted(async () => {
    await store.getTransactions()
    await store.getYearJoined()

});
const yearArray = () =>{
    const dateJoined = new Date(store.yearJoined)
    const yearJoined =  dateJoined.getFullYear()

    const yearRange = []
    for (let year = yearJoined; year <= yearJoined; year++){
        yearRange.push(year)
    }
    return yearRange

}
// call function
const years = yearArray()

watchEffect(()=>{
    store.searchTransaction(store.search)
})
</script>
<template>
    <div class="my-10">
        <v-row justify="space-around">
            <v-col cols="auto">
                <v-card height="100" width="200">
                    <v-card-title>
                        Total Revenue
                    </v-card-title>
                    <v-card-subtitle class="text-green-darken-1 text-subtitle-2">
                        Ksh 30,000
                    </v-card-subtitle>
                </v-card>
            </v-col>
            <v-col cols="auto">
                <v-card height="100" width="200">
                    <v-card-title>
                        Unpaid amount
                    </v-card-title>
                    <v-card-subtitle class="text-red-accent-4">
                        Ksh 30,000
                    </v-card-subtitle>
                </v-card>
            </v-col>
            <v-col cols="auto">
                <v-card height="100" width="200">
                    <v-card-title>
                        Paid clients
                    </v-card-title>
                    <v-card-subtitle class="text-black">
                        150
                    </v-card-subtitle>
                </v-card>
            </v-col>
            <v-col cols="auto">
                <v-card height="100" width="200">
                    <v-card-title>
                        Unpaid clients
                    </v-card-title>
                    <v-card-subtitle class="text-red-accent-4">
                        100
                    </v-card-subtitle>
                </v-card>
            </v-col>
        </v-row>
    </div>
    <!-- data grid -->
    <div class="info my-4 text-subtitle-1">
        Payment as of <span class="text-body-1 text-grey-accent-4">{{ new Date().toDateString() }}</span>
    </div>
    <!-- table controls -->
    <v-row>
        <v-toolbar class="bg-white box-shadow border">

            <div class="w-50 px-2">
                <v-text-field variant="underlined" label="search" placeholder="search by name or serial ..." color="primary"
                    clearable v-model="store.search"></v-text-field>
            </div>
            <v-spacer></v-spacer>
            <div class="w-75 d-flex justify-end">
                <div class="w-25 mx-2">
                    <v-select clearable label="Year" variant="underlined" 
                        :items="years"></v-select>
                </div>

                <div class="w-25 mx-2">
                    <v-select clearable label="Month" variant="underlined"
                        :items="['Jan','Feb','Mar','Apr','May','Jun','Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']"
                        ></v-select>
                </div>
            </div>
        </v-toolbar>
    </v-row>
    <v-row>
        <v-col>
            <MpesaTransactions/>
        </v-col>
    </v-row>
</template>