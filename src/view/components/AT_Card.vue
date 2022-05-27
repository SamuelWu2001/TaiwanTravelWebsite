<template>
    <div @click="info" v-for="(at) in [FindAt(this.id)]" class="At-card shadow" style="cursor:pointer;">
        <div style="flex:3">
            <img :src=at.Image style="width:100%;height:100%;padding:15px;">
        </div>
        <div style="flex:7;">
            <a style="margin:30px;font-size:25px;font-weight: bolder;display: block;">{{ at.Title }}</a>
            <a style="margin:30px;font-size:15px;">地址 : {{ at.Address }}</a>
        </div>
        <div
            style="margin:10px;height:30%;width:90%; border-radius: 10px;;color:aliceblue;background: rgb(17,126,209);flex:1;padding-top:10px;font-size:25px;font-weight:bolder;">
            {{ at.Rate }}
        </div>
    </div>
</template>
<script>
import { mapGetters } from 'vuex';
export default ({
    props: ['ID'],
    computed: {
        ...mapGetters(["FindAt"]),
    },
    methods: {
        FindAt(id) {
            console.log('Samuel')
            console.log(id);
            console.log(this.FindAt(id));
            return this.FindAt(id);
        },
        info: function () {
            this.$router.push({
                path: '/AtInfo',
                query: {
                    ID: this.id,
                }
            });
        }
    },
    data() {
        return {
            id: this.ID,
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