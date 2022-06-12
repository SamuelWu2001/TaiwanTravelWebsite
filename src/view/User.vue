<template>
<div style="display:flex;justify-content:center;align-items: center;"> 
    <div v-show="UserValid===0" class="UserCard" style="font-size:30px;font-weight:bold;">
        <div > 
            您尚未登入
            <br>
            請輸入您的帳號並點選登入
            <br>
            <input id="userID" v-model="userID" style="border-radius:5px;height:46px;border: hidden;margin:25px;" placeholder="userID" >
            <br>
            <button class="Login" style="font-size: 25px;height:46px;border-radius: 10px;width:150px;" type="submit" @click="login();">登入</button>
            <button style="font-size: 25px;margin-left:10px;height:46px;border-radius: 10px;width:150px;" type="submit" data-bs-toggle="modal" data-bs-target="#adduser">註冊帳號</button>
        </div>
    </div>
    <div v-show="UserValid===1" class="UserCard" style="font-size:30px;font-weight:bold;">
        <div > 
            <div style="text-align: left;">姓名 : {{UserData.Name}} </div>
            <div style="text-align: left;">性別 : {{UserData.Sex}} </div>
            <div style="text-align: left;">生日 : {{UserData.Birth}} </div>
            <div style="text-align: left;">電話 : {{UserData.Phone}} </div>
            <button style="font-size: 25px;margin-left:10px;height:46px;border-radius: 10px;width:150px;" type="submit" @click="addroute">新增路線</button>
            <button style="font-size: 25px;margin-left:10px;height:46px;border-radius: 10px;width:150px;" type="submit" @click="logout">登出</button>
        </div>
    </div>
    <div class="modal fade" id="adduser">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h3><b>註冊帳號</b></h3>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body">
              <div style="margin:5px;">
                <b style="float:left;">帳號</b>
                <input v-model="user.ID" placeholder="USXXXXXXXX">
              </div>
              <div style="margin:5px;">
                <b style="float:left;">姓名</b>
                <input v-model="user.Name" placeholder="">
              </div>
              <div style="margin:5px;">
                <b style="float:left;">性別</b>
                <select v-model="user.Sex" id="tool_type" name="tool_type" style="cursor:pointer;width:44%;font-size: 25px;" class=" ml-1 mb-2" >
	            	<option value="0"></option>
	            	<option value="M">男</option>
	            	<option value="F">女</option>
	            </select>
              </div>
              <div style="margin:5px;">
                <b style="float:left;">生日</b>
                <input class="me-4 " v-model="user.Birth" style="border-radius:5px;height:40px;" type="date">
              </div>
              <div style="margin:5px;">
                <b style="float:left;">電話</b>
                <input v-model="user.Phone" placeholder="">
              </div>
          </div>
          <div class="modal-footer">
            <button type="button" data-bs-dismiss="modal" @click="addUser" style="background: rgb(112, 105, 104);color:white;">送出</button> 
          </div>
        </div>
      </div>
    </div>
</div>
</template>
<script>
import { mapState, mapGetters } from 'vuex';
import axios from 'axios';
import store from '../store'
export default ({
    created(){
      if(this.$store.state.User.ID!= ''){
          this.UserValid=1;
      }
    },
    computed: {
      ...mapState({
        UserData: state => state.User,
      }),
    },
    data(){
        return { 
           UserValid : 0,
           userID : '',
           user : {
               ID : '',
               Name : '',
               Sex : '',
               Birth : '',
               Phone : '',
           }
        }
    },
    methods:{
        addUser :function(){
            console.log('adduser',this.user.Birth,this.user.Sex)
            axios.post('http://127.0.0.1:5000/api/adduser',
              {
                ID : this.user.ID,
                Name : this.user.Name,
                Sex : this.user.Sex,
                Birth : this.user.Birth,
                Phone : this.user.Phone,
              }
            ).then((res)=>{
                console.log('資料 : ',res.data)
                alert(res.data)
            }).catch(function(err) {
                console.error(err);
            });
        },
        logout :function(){
            this.UserValid=0;
            this.$store.state.User.ID = ''
        },
        login :function(){
            console.log(this.userID)
            axios.get("http://127.0.0.1:5000/api/Login",{
              params:{
                userID : this.userID,
              }
            })
            .then((res)=>{
                console.log('資料 : ',res.data)
                if(res.data==='error'){
                    alert('查無此帳號')
                }
                else{
                    store.dispatch("LoadUser",res.data)
                    this.UserValid=1;
                }
            })
        },
        addroute :function(){
            this.$router.push({
              path : `/addroute`,
            });
        }
    },

})
</script>
<style >
    .UserCard {
        width:80%;
        padding : 50px;
        background: rgb(129, 212, 196);
        border-radius: 20px;
        margin-top:50px;
    }
    .Login:active {
        background:rgb(43, 150, 226);
    }
</style>