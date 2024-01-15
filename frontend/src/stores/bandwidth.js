import axios from "axios";
import { defineStore } from "pinia";

export const useBandwidth = defineStore("bandwidth", {
    state: ()=>({
        package: []
    }),
    actions:{
        getBandwith(){
            axios.get("/accounts/bandwidths/",{
                headers: { Authorization: `Token ${localStorage.getItem("token")}` },
            })
            .then((response) => {
                response.data.forEach(element => {
                    this.package.push(element.name)
                    
                });
            })
            .catch((response) => console.log(response))
        }
    }
});
