import { defineStore } from "pinia";
import axios from "axios";

export const useFieldWorkStore = defineStore("fieldwork", {
  state: () => ({
    fieldworks: [],
  }),
  actions: {
    getFieldWorkList() {
      axios.get("/accounts/fieldworks/")
        .then((resp) => {
          this.fieldworks = resp.data;
        })
        .catch((error) => console.log(error));
    },
  },
});
