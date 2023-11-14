import axios from "axios";
import { defineStore } from "pinia";

export const useBandwidth = defineStore("bandwidth", {
    state: ()=>({
        package: []
    }),
    actions:{
        getBandwith(){
            axios.get("/accounts/bandwidth/")
            .then((response) => {
                response.data.forEach(element => {
                    this.package.push(element.name)
                    
                });
            })
            .catch((response) => console.log(response))
        }
    }
});
