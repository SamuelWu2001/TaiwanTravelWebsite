<template>
  <form class="search " style="margin-top:50px;margin-bottom:10px;font-size:25px;" >
    <input class="me-4 " id="keyword" v-model="SearchElement.keyword" style="border-radius:5px;height:46px;" type="search" placeholder="關鍵詞" aria-label="Search">
    <label style="padding-right:20px;"> 入住日期 </label>
    <input class="me-4 " id="checkin" style="border-radius:5px;height:46px" aria-label="Search" type="date">
    <!-- <label style="padding-right:20px;"> 離開日期 </label>
    <input class="me-4 " id="checkout" style="border-radius:5px;height:46px" aria-label="Search" type="date"> -->
    <input class="me-4 " id="keyword" v-model="SearchElement.pnumber" style="border-radius:5px;height:46px;width:5%;" type="search" placeholder="人數" aria-label="Search">
    <button class="btn btn-outline-success" style="font-size: 25px;height:46px" type="submit" @click="processFormData();">Search</button>
  </form>
  <div v-for="(ac) in AcList" :key="AcList" style="display:flex;justify-content: center;align-items: center;">
    <ACCard :ID="ac.ID" :key="AcList" :pnumber="this.SearchElement.pnumber" :checkin="this.checkin"  />
    <!-- {{ac}} -->
  </div>
</template>

<script>
import ACCard from './components/AC_Card.vue'  //可以不管
import axios from "axios";
import store from '../store'
import { mapState, mapGetters } from 'vuex';
export default {
  created(){
  },
  components: {
    ACCard,
  },
  computed: {
    ...mapState({
      AcList: state => state.AcList,

    }),
  },
  data(){
    return{ 
      SearchElement :{
        keyword : this.$store.state.keyword,
        pnumber : this.$store.state.pnumber,
      },
      checkin : this.$store.state.checkin,
    }
  },
  methods: {
    processFormData: function(){
        console.log('test',this.checkin,this.SearchElement.keyword,this.SearchElement.pnumber)
        const CheckinElement = document.getElementById("checkin");
        const Checkin = CheckinElement.value;
        if(Checkin!=''){
          this.checkin = Checkin.replace(/-/g,'/');
        }
        this.$store.state.checkin = this.checkin;
        this.$store.state.keyword = this.SearchElement.keyword;
        this.$store.state.pnumber = this.SearchElement.pnumber;
        this.$router.push({
            path: '/Accommodation',
            query: {
                keyword : this.SearchElement.keyword,
                pnumber : this.SearchElement.pnumber,
                checkin : this.checkin,
            }
        });
        console.log(this.checkin,this.checkout,this.SearchElement)
        axios.get("http://127.0.0.1:5000/api/LoadACdata",{
          params:{
            keyword : this.SearchElement.keyword,
            pnumber : this.SearchElement.pnumber,
          }
        })
        .then((res)=>{
            console.log('資料 : ',res.data)
            store.dispatch("LoadACdata", res.data);
        })
    }
  }
}
</script>

<style>
label {
  padding-bottom: 10px;
  padding-right: 10px;
}

.Fixsize {
  font-size: 25px;
}

.date_input {
  margin-right: 15px;
  padding: 10px;
  font-size: 25px;
  width: 15%;
  height: 40px;
}

#text_input {
  margin-right: 15px;
  padding: 10px;
  font-size: 25px;
  width: 40%;
  height: 40px;
}

#people {
  margin-right: 15px;
  padding: 10px;
  font-size: 25px;
  width: 5%;
  height: 40px;
}

#Search_btn {
  background-color: rgb(159, 200, 222);
  border: none;
  border-radius: 10px;
  font-size: 24px;
  width: 120px;
  height: 40px;
  flex: 1;
}

#Search_btn:hover {
  background-color: rgb(170, 210, 225);
  color: rgb(120, 120, 120);
}

</style>
