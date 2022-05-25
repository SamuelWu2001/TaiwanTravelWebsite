<template>
    <div v-for="(ac) in AcList" style="display:flex;justify-content: center;align-items: center;">
        <ACCard :ID="ac.ID"/>
    </div>
</template>
<script>
import ACCard from './components/AC_Card.vue'  //可以不管
import{mapState,mapGetters} from 'vuex';
export default {
    components:{
        ACCard,
    },
    computed:{
      ...mapState({
        AcList : state=>state.AcList,
      }),
    },
}
</script>

<style>
</style>
