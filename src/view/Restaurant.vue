<template>
    <div style="margin: 10px;">
        <input id="text_input" v-model="text" placeholder="Search Here">
        <button id="Search_btn">Search</button>
    </div>
    <div v-for="(re) in ReList" style="display:flex; justify-content: center;align-items: center;">
        <RECard :ID="re.ID" />
    </div>
</template>

<script>

import RECard from './components/RE_Card.vue'  //可以不管
import { mapState, mapGetters } from 'vuex';
export default {
    components: {
        RECard,
    },
    computed: {
        ...mapState({
            AtList: state => state.AtList,
        }),
    },
    data() {
        return {
            keyword: ''
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
