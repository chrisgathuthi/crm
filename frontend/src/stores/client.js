import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useClientStore = defineStore('clients',{
  state: () => ({
    clients: []
  }),

  actions: {
    getClientList(){
      axios.get("/accounts/client/")
      .then((resp) => {
        this.clients = resp.data;
      })
      .catch((error) => console.log(error));
    }
  }
})

