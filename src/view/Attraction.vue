<template>
    <div style="margin: 10px;">
        <input id="text_input" v-model="keyword" placeholder="Search Here">
        <button @click="processFormData()"  id="Search_btn">Search</button>
    </div>
    <div v-for="(at) in AtList" :key="AtList" style="display:flex; justify-content: center;align-items: center;">
        <ATCard :ID="at.ID" :key="AtList" />
        <!-- {{at}} -->
    </div>
</template>

<script>

import ATCard from './components/AT_Card.vue'  //可以不管
import { mapState, mapGetters } from 'vuex';
import axios from 'axios';
import store from '../store'
export default {
    components: {
        ATCard,
    },
    computed: {
        ...mapState({
            AtList: state => state.AtList,
        }),
    },
    data() {
        return {
            keyword: ''
        }
    },
    methods:{
        processFormData: function(){
            this.$router.push({
                path: '/Attraction',
                query: {
                    keyword : this.keyword,
                }
            });
            axios.get("http://127.0.0.1:5000/api/LoadATdata",{
              params:{
                keyword : this.keyword,
              }
            })
            .then((res)=>{
                console.log('資料 : ',res.data)
                store.dispatch("LoadATdata", res.data);
            })
        },
    }
}

</script>

<style>
#text_input {
    margin-right: 15px;
    padding: 10px;
    font-size: 25px;
    width: 40%;
    height: 40px;
}

#Search_btn {
    background-color: rgb(159, 200, 222);
    border: none;
    border-radius: 10px;
    font-size: 24px;
    width: 120px;
    height: 40px;
}

#Search_btn:hover {
    background-color: rgb(170, 210, 225);
    color: rgb(120, 120, 120);
}
</style>
