import axios from "axios";
import { defineStore } from "pinia";

export const useTransactionStore = defineStore("transaction", {
  state: () => ({
    transactions: [],
    search: "",
    yearJoined: "",
    dataCount: "",
    loading: undefined,
  }),
  actions: {
    async getTransactions() {
      await axios
        .get("/accounts/mpesatransactions/", {
          headers: { Authorization: `Token ${localStorage.getItem("token")}` },
        })
        .then((response) => {
          this.loading = true;
          this.dataCount = response.data.count;
          this.transactions = response.data.results;
          this.loading = false;
          this.itemsPerPage = this.transactions.length;
        })
        .catch((response) => console.log(response));
    },
    async getYearJoined() {
      await axios
        .get("/accounts/provider-detail/", {
          headers: { Authorization: `Token ${localStorage.getItem("token")}` },
        })
        .then((response) => {
          this.yearJoined = response.data["yearJoined"];
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async searchTransaction() {
      await axios
        .get(
          "/accounts/mpesatransaction/",
          { params: { search: this.search } },
          {
            headers: {
              Authorization: `Token ${localStorage.getItem("token")}`,
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          this.transactions = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async loadMoreData(page){
      await axios.get(`/api/accounts/mpesatransactions/?page=${page}`,{headers: { Authorization: `Token ${localStorage.getItem("token")}`}})
      .then((response)=>{
        console.log("load more data");
        console.log(response.data);
      })
      .catch((error)=>{
        console.log(error);
      })


    }
  },
});
