<template>
  <div style="margin: 10px;">
    <label class="Fixsize">Keyword :</label>
    <input id="text_input" v-model="text" placeholder="Search Here">
    <label class="Fixsize">People amount :</label>
    <input id="people" type="number" min=1 value=1>
    <br>
    <label class="Fixsize">Check-in :</label>
    <input id="checkin" class="date_input" type="date" min=1>
    <label class="Fixsize">Check-out :</label>
    <input id="checkout" class="date_input" type="date" min=1>
    <button id="Search_btn">Search</button>
  </div>
  <div v-for="(ac) in AcList" style="display:flex;justify-content: center;align-items: center;">
    <ACCard :ID="ac.ID" />
  </div>
</template>

<script>
import ACCard from './components/AC_Card.vue'  //可以不管
import { mapState, mapGetters } from 'vuex';
export default {
  components: {
    ACCard,
  },
  computed: {
    ...mapState({
      AcList: state => state.AcList,
    }),
  },
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
}

#Search_btn:hover {
  background-color: rgb(170, 210, 225);
  color: rgb(120, 120, 120);
}
</style>
