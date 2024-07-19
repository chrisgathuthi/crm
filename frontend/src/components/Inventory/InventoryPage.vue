<script setup>
import { onMounted, ref } from 'vue';
import RegisterInventory from './RegisterInventory.vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

// change path
const router = useRouter()
const inventories = ref([])
onMounted(async () => {
    await axios.get("/accounts/inventories/", { headers: { Authorization: `Token ${localStorage.getItem("token")}` } })
        .then((response) => {
            inventories.value = response.data
        })
        .catch((error) => {
            console.log(error);
        })
})

</script>
<template>
    <section>
        <v-row>
            <v-col>
                <RegisterInventory />
            </v-col>
        </v-row>
    </section>
    <section>
        <v-table hover fixed-header>
            <thead>
                <tr>
                    <th>Item</th>
                    <th>Stock Opening</th>
                    <th>Stock In</th>
                    <th>Stock Out</th>
                    <th>Remaining Stock</th>
                    <th>Status</th>
                    <th>Purchase Date</th>
                    <th>Restoking Date</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="data in inventories" :key="data.id" class="hover"
                    @click="router.push({ name: 'inventoryUpdate', params: { id: `${data.id}` } })">
                    <td>{{ data.name }}</td>
                    <td>{{ data.opening_stock }}</td>
                    <td>{{ data.additional_stock }}</td>
                    <td>{{ data.out_stock }}</td>
                    <td>{{ data.remaining_stock }}</td>
                    <td>
                        <p class="p-1 bg-green-accent-2 text-green-darken-4">{{ data.status }}</p>
                    </td>
                    <td>{{ data.opening_stock_date }}</td>
                    <td>{{ data.restocking_date }}</td>
                </tr>
            </tbody>
        </v-table>
    </section>
</template>