<template>
    <div @click="info" v-for="(re) in [FindRe(this.id)]" :key="ReList" class="Re-card shadow" style="cursor:pointer;">
        <div style="flex:3">
            <img :src=re.Image style="width:100%;height:100%;padding:15px;">
        </div>
        <div style="flex:7;">
            <a style="margin-top:50px;font-size:35px;font-weight: bolder;display: block;">{{ re.Title }}</a>
            <a style="margin:10px;font-size:20px;">地址 : {{ re.Address }}</a>
        </div>
        <div
            style="margin:10px;height:30%;width:90%; border-radius: 10px;;color:aliceblue;background: rgb(17,126,209);flex:1;padding-top:10px;font-size:25px;font-weight:bolder;">
            {{ re.Rate }}
        </div>
    </div>
</template>
<script>
import { mapGetters,mapState } from 'vuex';
import axios from "axios";
import store from '../../store';
export default ({
    props: ['ID'],
    computed: {
        ...mapGetters(["FindRe"]),
        ...mapState({
          ReList: state => state.ReList,
        }),
    },
    methods: {
        FindRe(id) {
            console.log('Samuel')
            console.log(id);
            console.log(this.FindRe(id));
            return this.FindRe(id);
        },
        info: function () {
            this.$router.push({
                path: '/ReInfo',
                query: {
                    ID: this.id,
                }
            });
            axios.get("http://127.0.0.1:5000/api/LoadREinfo",{
              params:{
                ID: this.id,
              }
            })
            .then((res)=>{
                console.log('資料 : ',res.data)
                store.dispatch("LoadREinfo", res.data);
            });
        }
    },
    data() {
        return {
            id: this.ID,
        }
    }
})
</script>
<style >
.Re-card {
    width: 80%;
    height: 200px;
    border-radius: 10px;
    background: rgb(195, 227, 213);
    display: flex;
    margin: 20px
}
</style>