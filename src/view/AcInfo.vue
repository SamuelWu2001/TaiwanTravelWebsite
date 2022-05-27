<template>
    <div style="display:flex; justify-content: center;align-items: center;">
        <div @click="info" v-for="(ac) in [FindAc(this.id)]" class="Ac-info shadow">
            <div style="font-size:50px;font-weight: bolder;padding-top:30px;">
                <a>{{ ac.Title }}</a>
            </div>
            <div style="margin:50px; font-size:20px;">
                <a style="display:block;text-align: left;margin:10px;"><b>地址 : </b>{{ ac.Address }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>電話 : </b>{{ ac.Phone }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>停車資訊 : </b>{{ ac.Park }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>有無WIFI : </b>{{ ac.Wifi }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>房型價格 : </b></a>
                <img :src=ac.Image style="width:70%;height:100%;padding:20px;">
            </div>
            <div>
                <iframe :src=ac.GoogleMapKey width="600" height="400" style="border:0;margin-bottom:50px;"
                    allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default ({
    computed: {
        ...mapGetters(["FindAc"]),
    },
    methods: {
        FindAc(id) {
            return this.FindAc(id);
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
.Ac-info {
    width: 80%;
    border-radius: 10px;
    background: rgb(195, 227, 213);
    margin: 20px
}
</style>