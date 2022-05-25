import Vuex from 'vuex'
 
export default new Vuex.Store({
  state: { 
    AcList :[
      {
        ID : 'AC00000001',
        Title : '雨島旅店',
        Address : '基隆仁三路8號',
        Image : "/src/assets/雨島旅店.jpg",
        Rate : 4.2,
        Phone : '02-5846125',
        Wifi : '有',
        Park : '',
        GoogleMapKey : "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3612.223667623945!2d121.74270321484381!3d25.128127983928284!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x345d4e3e5e12fe35%3A0xa3b061f887ea7615!2zMjAw5Z-66ZqG5biC5LuB5oSb5Y2A5LuB5LiJ6LevOOiZnw!5e0!3m2!1szh-TW!2stw!4v1653476658510!5m2!1szh-TW!2stw",
      },
      {
        ID : 'AC00000002',
        Title : '華國商務飯店',
        Address : '基隆愛三路49巷18號',
        Image : '/src/assets/華國商務飯店.jpg',
        Rate : 4.0,
        Phone : '02-2216169',
        Wifi : '有',
        Park : '飯店往左走150公尺有公有停車場',
        GoogleMapKey : "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3612.2201487529937!2d121.74010991484377!3d25.128246983928253!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x345d4e15f622d71d%3A0xa8a123671935d794!2zMjAw5Z-66ZqG5biC5LuB5oSb5Y2A5oSb5LiJ6LevNDnlt7cxOOiZnw!5e0!3m2!1szh-TW!2stw!4v1653477500807!5m2!1szh-TW!2stw",
      }
    ],
    AtList :[],
    ReList :[],
  },
  mutations: {
  },
  actions: {
  },
  getters: {
    FindAc:state=>(id)=>{
      return state.AcList.find(AcList=>AcList.ID===id)
    },
  }
});





