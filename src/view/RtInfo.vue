<template>
    <div style="display:flex; justify-content: center;align-items: center;">
        <div @click="info" v-for="(rt) in [FindRt(this.name,this.time)]" class="Ac-info shadow">
            <div style="font-size:50px;font-weight: bolder;padding-top:30px;">
                <a>{{ rt.Name }}</a>
            </div>
            <div style="margin:50px; font-size:20px;">
                <a style="display:block;text-align: left;margin:10px;"><b>發布時間 : </b>{{ rt.Time }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>描述 : </b>{{ rt.Description }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>花費 : </b>{{ rt.Price }} 元</a>
                <a style="display:block;text-align: left;margin:10px;"><b>行程 : </b></a>
                <table class="table table-striped" style="margin-top:20px;font-size:20px;">
                  <thead >
                    <tr>
                      <th scope="col">名稱</th>
                      <th scope="col">地址</th>
                      <!-- <th scope="col">描述</th> -->
                    </tr>
                  </thead>
                  <tbody>
                    <tr  v-for="(spot) in rt.spotlist">
                      <td>{{spot.Name}}</td>
                      <td>{{spot.Address}}</td>
                      <!-- <td>{{spot.Description}}</td> -->
                    </tr>
                  </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters,mapState } from 'vuex';
import axios from 'axios';
export default ({
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
    },
    data() {
        return {
            name: this.$route.query.Name,
            time: this.$route.query.Time,
        }
    }
})
</script>

<style >
.Ac-info {
    width: 80%;
    border-radius: 10px;
    background: rgb(195, 227, 213);
    margin: 20px
}
</style>