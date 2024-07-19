import { defineStore } from "pinia";
import axios from "axios";
import { useRoute } from "vue-router";

export const useInventoryStore = defineStore("inventory", {
  state: () => ({
    inventories: []
  }),
  actions: {
    async getInventoryDetail() {
    const route = useRoute()
      await axios
        .get(`/accounts/inventory/${route.params.id}`, {
          headers: { Authorization: `Token ${localStorage.getItem("token")}` },
        })
        .then((response) => {
          this.inventories = response.data;
        })
        .catch();
    },
  },
});
