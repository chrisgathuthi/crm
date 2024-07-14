<script setup>
import RegisterInventory from './RegisterInventory.vue';



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
        <v-table hover>
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
                <tr>
                    <td>Ethernet cables</td>
                    <td>100</td>
                    <td>10</td>
                    <td>50</td>
                    <td>60</td>
                    <td>available</td>
                    <td>{{ new Date().toLocaleDateString() }}</td>
                    <td>{{ new Date().toLocaleDateString() }}</td>

                </tr>
                <tr>
                    <td>Routers</td>
                    <td>100</td>
                    <td>20</td>
                    <td>30</td>
                    <td>40</td>
                    <td>unavailable</td>
                    <td>{{ new Date().toLocaleDateString() }}</td>
                    <td>{{ new Date().toLocaleDateString() }}</td>
                </tr>
            </tbody>
        </v-table>
    </section>
</template>