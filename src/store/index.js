import Vuex from 'vuex'

export default new Vuex.Store({
  state: {
    pnumber : '',
    checkin : '',
    keyword : '',
    AcList: [
    ],
    Acinfo : {
    },
    AtList: [
    ],
    Atinfo :{},
    ReList: [],
    ReInfo :{},
    SpotList:[],
    User :{
      ID : '',
      Name : '',
      Sex : '',
      Birth : '',
      Phone : '',
    },
    RouteList : [
      {
        Name : '忠烈祠路線',
        Time : '2020-02-02 13:40:00',
        spotlist : [
          {
            ID : 'AT00000274',
            Name : '123456',
            Address : '',
            Descritption : '',
          },
          {
            ID : 'AT00000025',
            Name : '456789',
            Address : '',
            Descritption : '',
          },
        ],
        Descritption : '嗨嗨嗨嗨嗨嗨',
        Price : '5000',
      },
    ],
  },
  mutations: {
    LoadACdata(state,AcData){
      console.log('mutations',AcData);
      state.AcList = AcData;
    },
    LoadACinfo(state,Acinfo){
      console.log('mutations',Acinfo);
      state.Acinfo = Acinfo;
    },
    LoadREdata(state,ReData){
      console.log('mutations',ReData);
      state.ReList = ReData;
    },
    LoadREinfo(state,Reinfo){
      console.log('mutations',Reinfo);
      state.Reinfo = Reinfo;
    },
    LoadATdata(state,AtData){
      console.log('mutations',AtData);
      state.AtList = AtData;
    },
    LoadATinfo(state,Atinfo){
      console.log('mutations',Atinfo);
      state.Atinfo = Atinfo;
    },
    LoadUser(state,Userinfo){
      console.log('mutations',Userinfo);
      state.User = Userinfo;
    },
    LoadSpotdata(state,SpotData){
      console.log('mutations',SpotData);
      state.SpotList = SpotData;
    },
    LoadRoutedata(state,RtData){
      state.RouteList = RtData;
      console.log('mutations',RtData);
    },
  },
  actions: {
    LoadACdata({commit},data){
      commit('LoadACdata',data);
    },
    LoadACinfo({commit},data){
      commit('LoadACinfo',data);
    },
    LoadREdata({commit},data){
      commit('LoadREdata',data);
    },
    LoadREinfo({commit},data){
      commit('LoadREinfo',data);
    },
    LoadATdata({commit},data){
      commit('LoadATdata',data);
    },
    LoadATinfo({commit},data){
      commit('LoadATinfo',data);
    },
    LoadUser({commit},data){
      commit('LoadUser',data);
    },
    LoadSpotdata({commit},data){
      commit('LoadSpotdata',data);
    },
    LoadRtdata({commit},data){
      console.log(data);
      commit('LoadRoutedata',data);
    },
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
    FindRt: state => (Name,Time) => {
      return state.RouteList.find(RouteList => (RouteList.Name === Name && RouteList.Time === Time))
    },
  }
});





