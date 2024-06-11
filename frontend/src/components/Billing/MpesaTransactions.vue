<script setup>
import { onMounted } from 'vue';
import { useTransactionStore } from '@/stores/transaction'

const store = useTransactionStore()

const headers = [
    { title: '#', value: 'id', key: 'index', sortable: false, align: 'start' },
    { title: "Acc No", value: 'bill_ref_number', key: 'serialNo', sortable: false, align: 'start' },
    { title: "Transaction code", value: 'transaction_id', key: 'transactionCode', sortable: false, align: 'start' },
    { title: "Full name", value: 'full_name', key: 'fullName', sortable: false, align: 'start' },
    { title: "Date", value: 'transaction_time', key: 'transactionTime', sortable: false, align: 'start' },
    { title: "Phone Number", value: 'phone_number', key: 'phoneNumber', sortable: false, align: 'start' },
    { title: "Amount", value: 'transaction_amount', key: 'transactionAmount', sortable: true, align: 'start' },
]

onMounted(async () => {
    await store.getTransactions()
    await store.getYearJoined()
});


// function loadNewData(page) {
//     console.log("load more data", page);

// }

</script>
<template>
    <v-data-table-server :headers="headers" :loading="store.loading" :items="store.transactions" :items-value="id"
        v-model:items-per-page="store.itemsPerPage" :items-length="store.dataCount" @update:page="store.loadMoreData"
        hover="true" items-per-page-text="transcations" loading-text="loading more transactions">
    </v-data-table-server>
</template>