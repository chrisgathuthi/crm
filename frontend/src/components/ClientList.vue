<script setup>
import { onMounted } from "vue";
import { useRouter } from "vue-router";
import { useClientStore } from "../stores/client";

const router = useRouter();

// clients data
const store = useClientStore()

onMounted(async () => {
  await store.getClientList()

});

</script>
<template>
  <v-container>
    <v-row no-gutters style="font-weight: bold">
      <v-col>
        <v-sheet class="ma-1"> serial no </v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="ma-1">Names</v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="ma-1">Location</v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="ma-1">Phone Number</v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="ma-1"> Plan </v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="ma-1"> Router </v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="ma-1"> Reg date </v-sheet>
      </v-col>
    </v-row>
    <v-row
      no-gutters
      v-for="client in store.clients"
      :key="client.id"
      @click="router.push({ name: 'client-detail', params: { id: client.id } })"
      class="data-list"
    >
      <v-col>
        <v-sheet class="ma-1">
          {{ client.serial }}
        </v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="ma-1"
          >{{ client.first_name }} {{ client.last_name }}</v-sheet
        >
      </v-col>
      <v-col>
        <v-sheet class="ma-1">{{ client.location }}</v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="ma-1">{{ client.phone_number }}</v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="ma-1">
          {{ client.service_plan }}
        </v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="ma-1">{{ client.router }}</v-sheet>
      </v-col>
      <v-col>
        <v-sheet>
          {{ client.registration_date }}
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>
<style scoped>
.action-menu {
  background-color: green;
}
.data-list{
  cursor: pointer;
}
.v-row:hover{
  background-color: #dfdfdfef;
}
</style>
