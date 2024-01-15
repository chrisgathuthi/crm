import { defineStore } from "pinia";
import axios from "axios";

export const useFieldWorkStore = defineStore("fieldwork", {
  state: () => ({
    fieldworks: [],
  }),
  getters: {
    completed() {
      return this.fieldworks = this.fieldworks.filter(
        (fieldwork) => (fieldwork.isclosed = true)
      );
    },
    open() {
      return this.fieldworks = this.fieldworks.filter(
        (fieldwork) => (fieldwork.isclosed = false)
      );
    },
  },

  actions: {
    async getFieldWorkList() {
      await axios
        .get("/accounts/fieldwork/",{headers:{Authorization: `Token ${localStorage.getItem("token")}`}})
        .then((resp) => {
          this.fieldworks = resp.data;
          console.log(this.fieldworks);
        })
        .catch((error) => console.log(error));
    },
  },
});
