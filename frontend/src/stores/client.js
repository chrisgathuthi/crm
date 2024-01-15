import { defineStore } from 'pinia'
import axios from 'axios'

export const useClientStore = defineStore('clients',{
  state: () => ({
    clients: []
  }),

  actions: {
    getClientList(){
      axios.get("/accounts/client/",{
        headers: { Authorization: `Token ${localStorage.getItem("token")}` },
    })
      .then((resp) => {
        this.clients = resp.data;
      })
      .catch((error) => console.log(error));
    }
  }
})

