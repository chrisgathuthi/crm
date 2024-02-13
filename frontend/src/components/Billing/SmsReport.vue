<!-- <template>
    <section>

        <v-table fixed-header>
            <thead class="text-bold">
                <tr>
                    <th>#</th>
                    <th>Cost (KES)</th>
                    <th>Message ID</th>
                    <th>Phone Number</th>
                    <th>Status</th>
                    <th>Status Code</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="i in 20" :key="i">
                    <td>{{ i }}</td>
                    <td>0.60</td>
                    <td>ee37b39e-af7b-412a-885f-62f23a15f685</td>
                    <td>254757164343</td>
                    <td> <span class="bg-green pa-1 rounded">SUCCESS</span> </td>
                    <td>0</td>
                </tr>
            </tbody>
        </v-table>

    </section>
</template> -->
<template>
    <v-data-table-server
      v-model:items-per-page="itemsPerPage"
      :headers="headers"
      :items-length="totalItems"
      :items="serverItems"
      :loading="loading"
      :search="search"
      item-value="name"
      @update:options="loadItems"
    ></v-data-table-server>
  </template>
  <script>
    const desserts = [
      {
        id: '1',
        cost: 0.60,
        messageID: 'ee37b39e-af7b-412a-885f-62f23a15f685',
        phoneNumber: 254757164343,
        status: 'success',
        statusCode: '0',
      },
      {
        id: '1',
        cost: 0.60,
        messageID: 'ee37b39e-af7b-412a-885f-62f23a15f685',
        phoneNumber: 254757164343,
        status: 'failed',
        statusCode: '10',
      },
      {
        id: '1',
        cost: 0.60,
        messageID: 'ee37b39e-af7b-412a-885f-62f23a15f685',
        phoneNumber: 254757164343,
        status: 'success',
        statusCode: '0',
      },
      {
        id: '1',
        cost: 0.60,
        messageID: 'ee37b39e-af7b-412a-885f-62f23a15f685',
        phoneNumber: 254757164343,
        status: 'success',
        statusCode: '0',
      },
      {
        id: '1',
        cost: 0.60,
        messageID: 'ee37b39e-af7b-412a-885f-62f23a15f685',
        phoneNumber: 254757164343,
        status: 'success',
        statusCode: '0',
      },
    ]
  
    const FakeAPI = {
      async fetch ({ page, itemsPerPage, sortBy }) {
        return new Promise(resolve => {
          setTimeout(() => {
            const start = (page - 1) * itemsPerPage
            const end = start + itemsPerPage
            const items = desserts.slice()
  
            if (sortBy.length) {
              const sortKey = sortBy[0].key
              const sortOrder = sortBy[0].order
              items.sort((a, b) => {
                const aValue = a[sortKey]
                const bValue = b[sortKey]
                return sortOrder === 'desc' ? bValue - aValue : aValue - bValue
              })
            }
  
            const paginated = items.slice(start, end)
  
            resolve({ items: paginated, total: items.length })
          }, 500)
        })
      },
    }
  
    export default {
      data: () => ({
        itemsPerPage: 5,
        headers: [
          {
            title: '#',
            align: 'start',
            sortable: false,
            key: 'id',
          },
          { title: 'Cost (ksh)', key: 'cost', align: 'start' },
          { title: 'Message ID', key: 'messageID', align: 'start' },
          { title: 'Phone Number', key: 'phoneNumber', align: 'start' },
          { title: 'Status', key: 'status', align: 'start' },
          { title: 'Status code', key: 'statusCode', align: 'start' },
        ],
        search: '',
        serverItems: [],
        loading: true,
        totalItems: 0,
      }),
      methods: {
        loadItems ({ page, itemsPerPage, sortBy }) {
          this.loading = true
          FakeAPI.fetch({ page, itemsPerPage, sortBy }).then(({ items, total }) => {
            this.serverItems = items
            this.totalItems = total
            this.loading = false
          })
        },
      },
    }
  </script>