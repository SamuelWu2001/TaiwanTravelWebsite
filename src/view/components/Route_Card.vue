<template>
    <div @click="info" v-for="(rt) in [FindRt(this.name,this.time)]" :key="RouteList" class="At-card shadow" style="display:block;cursor:pointer;">
        <div style="font-size:35px;margin-top:30px;height:50px;">
            <b style="margin-top:px;"> {{rt.Name}}</b>
            <div style="float:right;margin:10px; padding:10px; border-radius: 10px;color:aliceblue;background: rgb(17,126,209);font-size:20px;font-weight:bolder;">
                {{ rt.Price }} 元
            </div>
        </div>
        <div style="display:flex;margin:10px;"> 
            <div style="background:rgb(142, 175, 228);font-size:18px;margin:5px;margin-top:15px;padding:10px;border-radius:10px;" v-for="(spot) in FindRt(this.name,this.time).spotlist"> 
                {{spot.Name}}
            </div>
        </div>
    </div>
</template>
<script>
import { mapGetters,mapState } from 'vuex';
import axios from "axios";
import store from '../../store';
export default ({
    props: ['Name','Time'],
    computed: {
        ...mapGetters(["FindRt"]),
        ...mapState({
          RouteList: state => state.RouteList,
        }),
    },
    methods: {
        FindRt(name,time) {
            console.log('Samuel')
            console.log(this.FindRt(name,time));
            return this.FindRt(name,time);
        },
        info: function () {
            this.$router.push({
                path: '/RtInfo',
                query: {
                    Name: this.name,
                    Time: this.time,
                }
            });
            // axios.get("http://127.0.0.1:5000/api/LoadRTinfo",{
            //   params:{
            //         Name: this.name,
            //         Time: this.time,
            //   }
            // })
            // .then((res)=>{
            //     console.log('資料 : ',res.data)
            //     store.dispatch("LoadRTinfo", res.data);
            // });
        }
    },
    data() {
        return {
            name: this.Name,
            time: this.Time,
        }
    }
})
</script>
<style >
.At-card {
    width: 80%;
    height: 200px;
    border-radius: 10px;
    background: rgb(195, 227, 213);
    display: flex;
    margin: 20px
}
</style>