<script setup>
import { onMounted } from "vue";
import { useRouter } from "vue-router";
import { useClientStore } from "@/stores/client";
import { useToastStore } from "@/stores/toast";
import { Converter } from "@/functions/DateConverter";
const router = useRouter();
// clients data
const store = useClientStore()
const toast = useToastStore()

onMounted(async () => {
  await store.getClientList()
  await toast.showToast(3000, "welcome back captain", "success")
});

</script>
<template>
  <section>

    <v-table fixed-header>
      <thead class="text-bold">
        <tr>
          <th>Serial no:</th>
          <th>Names</th>
          <th>Location</th>
          <th>Phone Number</th>
          <th>Service</th>
          <th>Router</th>
          <th>Bandwith</th>
          <th>Status</th>
          <th>Reg date</th>

        </tr>
      </thead>
      <tbody v-if="store.clients.length > 1">
        <tr v-for="client in store.clients" :key="client.id"
          @click="router.push({ name: 'client-detail', params: { id: client.id } })"
          @mouseover="style = { backgroundColor: 'green' }" class="pointer">
          <td>{{ client.serial }}</td>
          <td>{{ client.full_name }}</td>
          <td>{{ client.location }}</td>
          <td>{{ client.phone_number }}</td>
          <td>{{ client.service_plan }}</td>
          <td>{{ client.router }}</td>
          <td>{{ client.bandwidth }}</td>
          <td>{{ client.status }}</td>
          <td>{{ Converter(client.registration_date) }}</td>
        </tr>
      </tbody>
      <tbody v-else>
        <tr>
          <td colspan="9">
            <p>No clients registered</p>
          </td>
        </tr>
      </tbody>

    </v-table>

  </section>
</template>
<style scoped>
.action-menu {
  background-color: green;
}

.data-list {
  cursor: pointer;
}

.v-row:hover {
  background-color: #dfdfdfef;
}
</style>
