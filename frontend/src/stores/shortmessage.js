import {defineStore} from 'pinia'
import axios from 'axios'

export const useShortMessageStore = defineStore("shortMessage",{
    state: ()=>({
        messages: []
    }),
    actions:{
        async getMessages(){
            await axios.get("/accounts/shortmessages/",{headers:{"Authorization":`Token ${localStorage.getItem("token")}`}})
            .then((response)=>{
                this.messages = response.data

            })
            .catch((error)=>{
                console.log(error);
            })
        }
    }
})