import Vuex from 'vuex'

export default new Vuex.Store({
  state: {
    AcList: [
      {
        ID: 'AC00000001',
        Title: '雨島旅店',
        Address: '基隆仁三路8號',
        Image: "/src/assets/雨島旅店.jpg",
        Rate: 4.2,
        Phone: '02-5846125',
        Wifi: '有',
        Park: '',
        GoogleMapKey: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3612.223667623945!2d121.74270321484381!3d25.128127983928284!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x345d4e3e5e12fe35%3A0xa3b061f887ea7615!2zMjAw5Z-66ZqG5biC5LuB5oSb5Y2A5LuB5LiJ6LevOOiZnw!5e0!3m2!1szh-TW!2stw!4v1653476658510!5m2!1szh-TW!2stw",
      },
      {
        ID: 'AC00000002',
        Title: '華國商務飯店',
        Address: '基隆愛三路49巷18號',
        Image: '/src/assets/華國商務飯店.jpg',
        Rate: 4.0,
        Phone: '02-2216169',
        Wifi: '有',
        Park: '飯店往左走150公尺有公有停車場',
        GoogleMapKey: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3612.2201487529937!2d121.74010991484377!3d25.128246983928253!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x345d4e15f622d71d%3A0xa8a123671935d794!2zMjAw5Z-66ZqG5biC5LuB5oSb5Y2A5oSb5LiJ6LevNDnlt7cxOOiZnw!5e0!3m2!1szh-TW!2stw!4v1653477500807!5m2!1szh-TW!2stw",
      },
    ],
    AtList: [
      {
        ID: 'AT00000001',
        Title: '基隆海洋廣場',
        Address: '基隆市仁愛區忠一路',
        Image: "/src/assets/雨島旅店.jpg",
        Rate: 3.9,
        VisitHours: '開放式空間，無時間限制。',
        Ticket: '無門票',
        Traf_Guide: '1. 基隆火車站下車過天橋即達，或搭乘國光客運於基隆站（海洋廣場前）下車，步行即可抵達。',
        Park: '基隆東岸地下停車場；另小艇碼頭停車場可停小客車',
        Phone: "",
        GoogleMapKey: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3612.223667623945!2d121.74270321484381!3d25.128127983928284!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x345d4e3e5e12fe35%3A0xa3b061f887ea7615!2zMjAw5Z-66ZqG5biC5LuB5oSb5Y2A5LuB5LiJ6LevOOiZnw!5e0!3m2!1szh-TW!2stw!4v1653476658510!5m2!1szh-TW!2stw",
      },
      {
        ID: 'AT00000002',
        Title: '和平島公園',
        Address: '基隆市中正區平一路360號',
        Image: "/src/assets/雨島旅店.jpg",
        Rate: 4.4,
        VisitHours: '"05/01-10/31：08:00 - 19:00（18:00 停止售票，19:00休園）11/01-04/30：08:00 - 18:00（17:00 停止售票，18:00休園）"',
        Ticket: '"全票80元 [ 一般遊客 ] 基隆市民60元 [ 本年度優惠40元/除中正區 ] 敬老票40元 [ 年滿65歲以上長者（需本國籍） ] 學生票40元 [ 6歲~12歲之學童/國中、高中、大學、研究所在學學生 ]"',
        Traf_Guide: '"1. 搭乘基隆市公車101號於「和平島公園站」下車，步行約5分鐘即可抵達。2. 搭乘T99濱海奇基線於「和平島公園站」下車即可抵達。"',
        Park: '備停車場',
        Phone: '02-24635452',
        GoogleMapKey: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3612.223667623945!2d121.74270321484381!3d25.128127983928284!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x345d4e3e5e12fe35%3A0xa3b061f887ea7615!2zMjAw5Z-66ZqG5biC5LuB5oSb5Y2A5LuB5LiJ6LevOOiZnw!5e0!3m2!1szh-TW!2stw!4v1653476658510!5m2!1szh-TW!2stw",
      },
    ],
    ReList: [],
  },
  mutations: {
  },
  actions: {
  },
  getters: {
    FindAc: state => (id) => {
      return state.AcList.find(AcList => AcList.ID === id)
    },
    FindAt: state => (id) => {
      return state.AtList.find(AtList => AtList.ID === id)
    },
    FindRe: state => (id) => {
      return state.ReList.find(ReList => ReList.ID === id)
    },
  }
});





