<template>
    <div style="display:flex; justify-content: center;align-items: center;">
        <div @click="info" v-for="(re) in [FindRe(this.id)]" class="Re-info shadow">
            <div style="font-size:50px;font-weight: bolder;padding-top:30px;">
                <a>{{ re.Title }}</a>
            </div>
            <div style="margin:50px; font-size:20px;">
                <a style="display:block;text-align: left;margin:10px;"><b>地址 : </b>{{ re.Address }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>電話 : </b>{{ re.Phone }}</a>
                <a style="display:block;text-align: left;margin:10px;"><b>停車資訊 : </b>{{ re.Park }}</a>
                <img :src=re.Image style="width:70%;height:100%;padding:20px;">
            </div>
            <div>
                <iframe :src=re.GoogleMapKey width="600" height="400" style="border:0;margin-bottom:50px;"
                    allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default ({
    computed: {
        ...mapGetters(["FindRe"]),
    },
    methods: {
        FindRe(id) {
            return this.FindRe(id);
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
.Re-info {
    width: 80%;
    border-radius: 10px;
    background: rgb(195, 227, 213);
    margin: 20px
}
</style>