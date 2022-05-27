<template>
    <div style="display:flex;justify-content: center;align-items: center;">
        <div @click="info" v-for="(at) in [FindAt(this.id)]" class="at-info shadow">
            <div style="font-size:50px;font-weight: bolder;padding-top:30px;">
                <a>{{ at.Title }}</a>
            </div>
            <div style="margin:50px; font-size:20px;">
                <a style="display:block;text-align: left;margin:10px;"><b>地址 : </b>{{ at.Address }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>電話 : </b>{{ at.Phone }}</a>
                <!-- <a style="display:block;text-align: left;margin:10px;"><b>開放時間 : </b>{{ at.VisitHours }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>門票價格 : </b>{{ at.Ticket }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>路線指引 : </b>{{ at.Traf_Guide }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>停車資訊 : </b>{{ at.Park }}</a> -->
                <a style="display:block;text-align: left;margin:10px;"><b>照片 : </b></a>
                <img :src=at.Image style="width:70%;height:100%;padding:20px;">
            </div>
            <div>
                <iframe :src=at.GoogleMapKey width="600" height="400" style="border:0;margin-bottom:50px;"
                    allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
        </div>
    </div>
</template>
<script>
import { mapGetters } from 'vuex';
export default ({
    computed: {
        ...mapGetters(["FindAt"]),
    },
    methods: {
        FindAt(id) {
            return this.FindAt(id);
        },
    },
    data() {
        return {
            id: this.$route.query.ID,
        }
    }
})
</script>
<style >
.At-info {
    width: 80%;
    border-radius: 10px;
    background: rgb(195, 227, 213);
    margin: 20px
}
</style>