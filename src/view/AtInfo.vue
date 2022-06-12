<template>
    <div style="display:flex; justify-content: center;align-items: center;">
        <div @click="info" v-for="(at) in [Atinfo]" class="Ac-info shadow">
            <div style="font-size:50px;font-weight: bolder;padding-top:30px;">
                <a>{{ at.Title }}</a>
            </div>
            <div style="margin:50px; font-size:20px;">
                <a style="display:block;text-align: left;margin:10px;"><b>地址 : </b>{{ at.Address }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>電話 : </b>{{ at.Phone }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>開放時間 : </b>{{ at.Visit }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>門票價格 : </b>{{ at.Ticket }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>路線指引 : </b>{{ at.Traffic }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>停車資訊 : </b>{{ at.Park }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>評價與評論 : </b></a>
                <table class="table table-striped" style="margin-top:20px;font-size:20px;">
                  <thead >
                    <tr>
                      <th scope="col">UserID</th>
                      <th scope="col">Rate</th>
                      <th scope="col">Comment</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr  v-for="(comment) in at.feedback">
                      <td>{{comment[1]}}</td>
                      <td>{{comment[2]}}</td>
                      <td>{{comment[0]}}</td>
                    </tr>
                  </tbody>
                </table>
                <div style="display:flex;"> 
                    <img :src=at.Image style="width:50%;padding:20px;flex:1;">
                    <iframe :src=at.GoogleMapKey width="600"  style="padding:20px;border:0;margin-bottom:50px;flex:1;"
                        allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                </div>
            </div>
            <div style="float:right;margin:20px;"> 
                <button data-bs-toggle="modal" data-bs-target="#feedback" style="width:100px;font-size:larger;background: azure;border-radius: 5px;"> 
                    新增評論
                </button>
            </div>
            <div class="modal fade" id="feedback">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h3><b>新增評論</b></h3>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                  </div>
                  <div class="modal-body">
                      <div class="">
                        <b style="float:left;">評分</b>
                        <input v-model="feedback.rate" placeholder="1.0~5.0">
                      </div>
                      <div class="">
                        <b style="float:left;">評論</b>
                        <textarea name="textarea" style="width:100%;height:150px;border: none;"  v-model="feedback.comment" placeholder="寫點什麼..." ></textarea>
                      </div>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-info" data-bs-dismiss="modal" @click="submitFeedback" style="background: rgb(112, 105, 104);color:white;">送出</button> 
                  </div>
                </div>
              </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex';
import axios from 'axios';
export default ({
    computed: {
        ...mapState({
            Atinfo: state => state.Atinfo,
        }),
    },
    methods: {
        submitFeedback : function(){
            if(this.feedback.userID==''){
                alert('您尚未登入，完成登入後即可發表評論');
            }
            else if(this.feedback.rate==''){
                alert('評分為必填選項');
            }
            else{
                axios.post('http://127.0.0.1:5000/api/addfeedback',
                  {
                    userID : this.feedback.userID,
                    spotID : this.feedback.spotID,
                    comment : this.feedback.comment,
                    rate : this.feedback.rate,
                  }
                ).catch(function(err) {
                    console.error(err);
                });
            }
        },
    },
    data() {
        return {
            feedback : {
                userID : this.$store.state.User.ID,
                spotID : this.$route.query.ID,
                comment : '',
                rate : '',
            }
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