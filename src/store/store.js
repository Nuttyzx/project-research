import { createStore } from 'vuex';

export default createStore({
  state: {
    authorName: {}, // สร้าง state เพื่อเก็บค่า author_name
    researchName: {},
    searchQueryAuthor: '', // เพิ่มสถานะสำหรับค่าการค้นหา
    searchQueryResearch: '',
    // isLogin: false
    isLogin: localStorage.getItem('isLogin') === 'true',
    formData: {
      title: '',
      publication_year: '',
      publication_title: '',
      abstract: '',
      article_number: '',
      content_type: '',
      start_page: '',
      end_page: '',
      doi: '',
      publisher: '',
      abstract_url: '',
      keywords: [],
      authors: []
    },
    authorIndatabase: [],
    isAddAuthorFormVisible: '',
    currentPublisher: '',
    otherExpertise: '',
    oldExpertise: ''
  },
  mutations: {
    setAuthorName(state, payload) {
      state.authorName = payload; // สร้าง mutation เพื่อเปลี่ยนแปลงค่าใน state
    },
    setResearchName(state, payload) {
      state.researchName = payload; 
    },
    setSearchQueryAuthor(state, query) { // เพิ่ม mutation สำหรับการตั้งค่าการค้นหา
      state.searchQueryAuthor = query;
    },
    setSearchQueryResearch(state, query) { // เพิ่ม mutation สำหรับการตั้งค่าการค้นหา
      state.searchQueryResearch = query;
    },
    setLogin_status(state, status){
      state.isLogin = status;
      localStorage.setItem('isLogin', status ? 'true' : 'false'); // เก็บค่า isLogin ลงใน localStorage
    },
    logout(state) {
      state.isLogin = false;
      localStorage.removeItem('isLogin'); // ลบค่า isLogin ออกจาก localStorage เมื่อ logout
    },
    setFormData(state, formData) {
      state.formData = formData;
      console.log(state.formData)
    },
    // updateFormData(state, { field, value }) {
    //   state.formData[field] = value;
    // },
    setAuthorIndatabase(state, data) {
      state.authorIndatabase = data;
    },
    setIsAddAuthorFormVisible(state, data) {
      state.isAddAuthorFormVisible = data;
    },
    setOtherPublisherInput(state,data){
      state.otherPublisherInput = data;
    },
    setOtherExpertise(state,data){
      state.otherExpertise = data;
    },
    setOldExpertise(state,data){
      state.oldExpertise = data;
    }
  },
  actions: {
    saveFormData({ commit }, formData) {
      commit('setFormData', formData);
    },
    // updateFormField({ commit }, payload) {
    //   commit('updateFormData', payload);
    // },
  },
});
