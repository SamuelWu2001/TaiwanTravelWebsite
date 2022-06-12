<template>
    <div v-for="(rt) in RouteList" style="display:flex; justify-content: center;align-items: center;">
        <RtCard :Name="rt.Name" :Time="rt.Time" :key="RouteList"/>
    </div>
</template>

<script>

import RtCard from './components/Route_Card.vue'
import { mapState, mapGetters } from 'vuex';
export default {
    components: {
        RtCard,
    },
    computed: {
        ...mapState({
            RouteList: state => state.RouteList,
        }),
    },
    data() {
        return {
        }
    }
}

</script>

<style>
#text_input {
    margin-right: 15px;
    padding: 10px;
    font-size: 25px;
    width: 40%;
    height: 40px;
}

#Search_btn {
    background-color: rgb(159, 200, 222);
    border: none;
    border-radius: 10px;
    font-size: 24px;
    width: 120px;
    height: 40px;
}

#Search_btn:hover {
    background-color: rgb(170, 210, 225);
    color: rgb(120, 120, 120);
}
</style>