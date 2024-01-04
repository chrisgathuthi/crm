import axios from "axios";
import { defineStore } from "pinia";

export const useTransactionStore = defineStore("transaction", {
  state: () => ({
    transactions: [],
    search: "",
  }),
  getters: {
    getTransactionDetail(state) {
        if (state.search != "") {
            this.transactions = this.transactions.filter((transaction) => {transaction.bill_ref_number = state.search});

        }else {
            this.getTransactionDetail()
        }
    },
  },
  actions: {
    async getTransactions() {
      await axios
        .get("/accounts/mpesatransactions/", {
          headers: { Authorization: `Token ${localStorage.getItem("token")}` },
        })
        .then((response) => {
          this.transactions = response.data;
        })
        .catch((response) => console.log(response));
    },
  },
});
