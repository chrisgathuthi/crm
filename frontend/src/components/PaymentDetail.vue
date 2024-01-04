<script setup>
import { onMounted, ref } from 'vue';
import { Converter } from '@/functions/DateConverter'
import { useTransactionStore } from '@/stores/transaction'

const store = useTransactionStore()

onMounted(async () => {
    await store.getTransactions()

});
</script>
<template>
    <div class="my-10">
        <v-row>
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
        These are payment records for <span class="text-body-1 text-purple-accent-4">{{ new Date().toDateString() }}</span>
    </div>
    <!-- table controls -->
    <v-row>
        <v-toolbar class="bg-white box-shadow border">

            <div class="w-50 px-2">
                <v-text-field variant="underlined" label="search"
                    placeholder="search by name serial ..." color="primary" clearable  v-model="store.getTransactionDetail"></v-text-field>
            </div>
            <v-spacer></v-spacer>
            <div class="w-75">

            </div>
        </v-toolbar>
    </v-row>

    <v-table fixed-header height="300px" class="mt-5">
        <thead>
            <tr>
                <th class="text-left">
                    #
                </th>
                <th class="text-left">
                    serial no: <!--Bill ref number--->
                </th>
                <th class="text-left">
                    Mpesa code
                </th>
                <th class="text-left">
                    Full name
                </th>
                <th class="text-left">
                    Date
                </th>
                <th class="text-left">
                    Phone number
                </th>
                <th class="text-left">
                    Amount
                </th>
                <th class="text-left">
                    Balance
                </th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="transaction in store.transactions" :key="transaction.id">
                <td>{{ transaction.id }}</td>
                <td>{{ transaction.bill_ref_number }}</td>
                <td>{{ transaction.transaction_id }}</td>
                <td>{{ transaction.full_name }}</td>
                <td>{{ Converter(transaction.transaction_time) }}</td>
                <td>{{ transaction.phone_number }}</td>
                <td>{{ transaction.transaction_amount }}</td>
                <td>0</td>
            </tr>
            <tr v-if="store.transactions.length < 1">
                <td colspan="8">
                    <v-col cols="auto">
                        <div class="text-h4">
                            <v-icon icon="mdi-emoticon-sad-outline"></v-icon>
                            No Transaction
                        </div>
                    </v-col>

                </td>

            </tr>
        </tbody>
    </v-table>
</template>