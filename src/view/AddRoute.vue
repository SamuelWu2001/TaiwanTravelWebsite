<template>
    <!-- <div style="display:flex;justify-content:center;align-items: center;">
      <div style="font-size: 50px;background:aquamarine;border-radius: 15px;width:20%;margin:20px;">
        <b>新增路線</b>
      </div>
    </div> -->
    <div style="display:flex;">
      <div style="flex:1;margin-top:50px;margin-left:50px;margin-bottom:50px;margin-right:25px;background:lightblue;border-radius: 20px;"> 
        <div style="padding: 20px;"> 
            <input style="border-radius:5px;font-size: 25px;" v-model="keyword" placeholder="關鍵字搜尋">
            <button class="AddRouteSearch" @click="search" style="font-size: 25px;margin-left: 20px;border-radius: 5px;">Search</button>
            <table class="table table-striped" style="margin-top:20px;font-size:20px;">
              <tbody>
                <tr  v-for="(Spot) in SpotList">
                  <td>{{Spot.ID}}</td>
                  <td>{{Spot.Name}}</td>
                </tr>
              </tbody>
            </table>
        </div>
      </div>
      <div style="flex:1;margin-top:50px;margin-left:25px;margin-bottom:50px;margin-right:50px;background:lightblue;border-radius: 20px;">
        <div style="padding: 20px;">
          <div class="form-group">
            <b style="float:left;">路線名稱</b>
            <input class="form-control" v-model="route.Name" placeholder="Route Name">
          </div>
          <div class="form-group">
            <b style="float:left;">花費</b>
            <input class="form-control" v-model="route.price" placeholder="">
          </div>
          <div class="form-group">
            <b style="float:left;">地點1</b>
            <input class="form-control" v-model="route.spot1" placeholder="Spot1">
          </div>
          <div class="form-group">
            <b style="float:left;">地點2</b>
            <input class="form-control" v-model="route.spot2" placeholder="Spot2">
          </div>
          <div class="form-group">
            <b style="float:left;">地點3</b>
            <input class="form-control" v-model="route.spot3" placeholder="Spot3">
          </div>
          <div class="form-group">
            <b style="float:left;">地點4</b>
            <input class="form-control" v-model="route.spot4" placeholder="Spot4">
          </div>
          <div class="form-group">
            <b style="float:left;">地點5</b>
            <input class="form-control" v-model="route.spot5" placeholder="Spot5">
          </div>
          <div class="form-group">
            <b style="float:left;">地點6</b>
            <input class="form-control" v-model="route.spot6" placeholder="Spot6">
          </div>
          <div class="form-group">
            <b style="float:left;">地點7</b>
            <input class="form-control" v-model="route.spot7" placeholder="Spot7">
          </div>
          <div class="form-group">
            <b style="float:left;">描述</b>
            <textarea name="textarea"  style="width:100%;height:150px;border: none;" v-model="route.description" placeholder="description" ></textarea>
          </div>
          <div style="text-align: right;"> 
            <button type="button" class="btn btn-info" data-bs-dismiss="modal" @click="submitRoute" style="margin-top:10px;width:15%;background:cornflowerblue;border-style:none;color:white;font-size:20px;">送出</button> 
          </div>
        </div>
      </div>
    </div>
    
</template>
<script> 
import { mapState, mapGetters } from 'vuex';
import axios from 'axios';
import store from '../store';
    export default({
        computed: {
            ...mapState({
                SpotList: state => state.SpotList,
            }),
        },
        data(){
            return { 
               keyword : '',
               userID : this.$store.state.User.ID,
               route : {
                   Name :'',
                   spot1:'',
                   spot2:'',
                   spot3:'',
                   spot4:'',
                   spot5:'',
                   spot6:'',
                   spot7:'',
                   description : '',
                   price : '',
               }
            }
        },
        methods:{ 
            submitRoute :function(){
              console.log(this.userID)
              axios.post("http://127.0.0.1:5000/api/AddRoutedata",{
                  userID : this.userID,
                  Name : this.route.Name,
                  spot1: this.route.spot1,
                  spot2: this.route.spot2,
                  spot3: this.route.spot3,
                  spot4: this.route.spot4,
                  spot5: this.route.spot5,
                  spot6: this.route.spot6,
                  spot7: this.route.spot7,
                  description : this.route.description,
                  price : this.route.price,
              })
              .then((res)=>{
                  console.log('資料 : ',res.data)
                  this.$router.push({
                    path : `/User`,
                  });
              })
            },
            search : function(){   
                axios.get("http://127.0.0.1:5000/api/LoadSpotdata",{
                  params:{
                    keyword : this.keyword,
                  }
                })
                .then((res)=>{
                    console.log('資料 : ',res.data)
                    store.dispatch("LoadSpotdata", res.data);
                })
            },
        }
    })
</script>
<style >
    .AddRouteSearch:active{ 
        background:lightblue;
    }
</style>