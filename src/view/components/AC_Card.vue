<template>
    <div @click="info" v-for="(ac) in [FindAc(this.id)]" :key="AcList" class="Ac-card shadow" style="cursor:pointer;">
        <!-- {{ac}} -->
        <div style="flex:3">
            <img :src=ac.Image style="width:100%;height:100%;padding:15px;">    
        </div>
        <div style="flex:7;">
            <a style="margin-top:50px;font-size:35px;font-weight: bolder;display: block;">{{ ac.Title }}</a>
            <a style="margin:10px;font-size:20px;">地址 : {{ ac.Address }}</a>
            <br>
        </div>
        <div
            style="margin:10px;height:30%;width:90%; border-radius: 10px;;color:aliceblue;background: rgb(17,126,209);flex:1;padding-top:10px;font-size:25px;font-weight:bolder;">
            {{ ac.Rate }}
        </div>
    </div>
</template>
<script>
import { mapGetters,mapState } from 'vuex';
import axios from "axios";
import store from '../../store';
export default ({
    props: ['ID','pnumber','checkin'],
    computed: {
        ...mapGetters(["FindAc"]),
        ...mapState({
          AcList: state => state.AcList,
        }),
    },
    methods: {
        FindAc(id) {
            console.log('Samuel')
            console.log(id);
            console.log(this.FindAc(id));
            return this.FindAc(id);
        },
        info: function () {
            this.$router.push({
                path: '/AcInfo',
                query: {
                    ID: this.id,
                }
            });
            axios.get("http://127.0.0.1:5000/api/LoadACinfo",{
              params:{
                ID: this.id,
                pnumber : this.pnum,
                checkin : this.Checkin,
              }
            })
            .then((res)=>{
                console.log('資料 : ',res.data)
                store.dispatch("LoadACinfo", res.data);
            })
        }
    },
    data() {
        return {
            id: this.ID,
            pnum : this.pnumber,
            Checkin : this.checkin,
        }
    }
})
</script>
<style >
.Ac-card {
    width: 80%;
    height: 200px;
    border-radius: 10px;
    background: rgb(195, 227, 213);
    display: flex;
    margin: 20px
}
</style>