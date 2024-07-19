<template>
    <section>
        <v-table hover>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Item</th>
                    <th>Quantity</th>
                    <th>Date</th>
                    <th>Staff</th>
                    <th>Activity</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>2</td>
                    <td>Ethernet cable</td>
                    <td>30</td>
                    <td>{{ new Date().toLocaleDateString() }}</td>
                    <td>Chris</td>
                    <td>
                        <p>Lorem ipsum dolor sit</p>
                    </td><!-- clickable link to the activity -->
                </tr>
                <tr>
                    <td>2</td>
                    <td>Ethernet cable</td>
                    <td>30</td>
                    <td>{{ new Date().toLocaleDateString() }}</td>
                    <td>Chris</td>
                    <td>
                        <p>Lorem ipsum dolor sit</p>
                    </td><!-- clickable link to the activity -->
                </tr>

            </tbody>
        </v-table>
    </section>

</template>