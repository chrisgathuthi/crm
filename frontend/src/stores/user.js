import {defineStore} from 'pinia'
import axios from 'axios'


export const useUserStore = defineStore({
    id: "user",
    state: () =>({
        user: {
            isAuthenticated: false,
            id: null,
            username: null,
            email: null,
            access: null,
            refresh: null,
        }
    }),
    actions: {
        initStore(){
            console.log('init store');
            if (localStorage.getItem('user.access')){
                this.user.isAuthenticated = true,
                this.user.id = localStorage.getItem('user.id'),
                this.user.username = localStorage.getItem('user.username'),
                this.user.email = localStorage.getItem('user.email'),
                this.user.access = localStorage.getItem('user.access'),
                this.user.refresh = localStorage.getItem('user.refresh')

                this.refreshToken()
                console.log("Init user", this.username);
            }
        },
        // save token
        setToken(data){
            console.log("setToken",data);
            this.user.access = data.access,
            this.user.refresh = data.refresh,
            this.user.isAuthenticated = true
        },
        removeToken(){
            console.log('remove token');
            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = false
            this.user.username = false

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.username', '')
            localStorage.setItem('user.email', '')
        },
        setUserInfo(user){
            console.log('set user info', user);

            this.user.id = user.id
            this.user.username = user.username
            this.user.email = user.email

            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.username', this.user.username)
            localStorage.setItem('user.email', this.user.email)

            console.log('user', this.user);
        },
        refreshToken(){
            axios.post('/accounts/token/refresh/',{refresh: this.user.refresh})
            .this((response) => {
                this.user.access = response.data.access

                localStorage.setItem('user.access', response.data.access)
                axios.defaults.headers.common['Authorized'] = 'Bearer '+ response.data.access
            })
            .catch((error) =>{
                console.log(error);
                this.removeToken()
            })
        }
    }
});