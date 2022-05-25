<template>
<div @click="info" v-for="(ac) in [FindAc(this.id)]" class="Ac-card shadow" style="cursor:pointer;">
    <div style="flex:4">
        <img :src=ac.Image style="width:100%;height:100%;padding:15px;">
    </div>
    <div style="flex:6;">
        <a style="margin:30px;font-size:25px;font-weight: bolder;display: block;">{{ac.Title}}</a>
        <a style="margin:30px;font-size:15px;">{{ac.Address}}</a>
    </div>
    <div style="margin:10px;height:30%;width:90%; border-radius: 10px;;color:aliceblue;background: rgb(17,126,209);flex:1;padding-top:10px;font-size:25px;font-weight:bolder;">
        {{ac.Rate}}
    </div>     
</div>
</template>
<script>
import{mapGetters} from 'vuex';
export default({
    props : ['ID'],
    computed:{
      ...mapGetters(["FindAc"]),
    },
    methods:{ 
      FindAc(id){
          console.log('Samuel')
          console.log(id);
          console.log(this.FindAc(id));
          return this.FindAc(id);
      },
      info :function(){
          this.$router.push({
          path : `/AcInfo`,
          query: {
            ID : this.id,
          }
        });
      }
    },
    data(){ 
        return{ 
            id : this.ID,
        }
    }
})
</script>
<style >
    .Ac-card{
        width:80%;
        height:200px;
        border-radius: 10px;
        background: rgb(195, 227, 213);
        display: flex;
        margin:20px
    }
</style>