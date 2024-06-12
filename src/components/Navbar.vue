<template>
  <!-- <div class="navbar bg-blue-900 flex justify-between items-center h-20 ">
    <div > 
    <button class="btn btn-ghost text-2xl font-extrabold text-white" v-on:click="redirectToPath">Research</button>
    </div>
    <div >
    <router-link v-if="isLogins" to="/showuser" class="mr-24 text-white font-bold hoverable ">รายชื่อนักวิจัย</router-link>
    <router-link v-if="isLogins" to="/showresearch" class="mr-24 text-white font-bold hoverable">รายชื่องานวิจัย</router-link>
    <router-link v-if="isLogins" to="/add" class="mr-24 text-white font-bold hoverable">เพิ่มข้อมูล</router-link>
    </div>
    <div >
    <button v-if="isLogins" class="btn btn-error " v-on:click="logout">ออกจากระบบ</button>
    </div>
  </div> -->

<div class="navbar container bg-gradient-to-r from-sky-500 to-indigo-500 min-w-full flex justify-between items-center ">
    <div class="navbar-center hidden lg:flex text-black">
      <div > 
        <button class="btn btn-ghost text-4xl font-black text-white" @click="redirectToPath">Research</button>
      </div>
      <div>
        <ul class="menu menu-horizontal px-1 ">
          <router-link v-if="isLogins" to="/showuser" class="font-bold hoverable" :class="{ 'text-white': $route.path === '/showuser' }">
            <li><a>รายชื่อนักวิจัยทั้งหมด</a></li>
          </router-link>
          <router-link v-if="isLogins" to="/showresearch" class="font-bold hoverable" :class="{ 'text-white': $route.path === '/showresearch' }">
            <li><a>รายชื่องานวิจัยทั้งหมด</a></li>
          </router-link>
          <router-link v-if="isLogins" to="/add" class="font-bold hoverable" :class="{ 'text-white': $route.path === '/add' }">
            <li><a>เพิ่มข้อมูลจาก IEEE Xplore</a></li>
          </router-link>
          <router-link v-if="isLogins" to="/addscopus" class="font-bold hoverable" :class="{ 'text-white': $route.path === '/addscopus' }">
            <li><a>เพิ่มข้อมูลจาก Scopus</a></li>
          </router-link>
          <router-link v-if="isLogins" to="/testaddresearch" class="font-bold hoverable" :class="{ 'text-white': $route.path === '/testaddresearch' }">
            <li><a>แบบฟอร์มเพิ่มข้อมูลงานวิจัย</a></li>
          </router-link>
        </ul>
      </div>
    </div>
    <div class="navbar-end">
      <button v-if="isLogins" class="btn bg-rose-500 text-white tracking-widest" @click="logout">ออกจากระบบ</button>
    </div>
  </div>

<!-- <li v-if="isLogins"> 
        <details>
          <summary>รายชื่อทั้งหมด</summary>
          <ul class="p-2">
            <router-link v-if="isLogins" to="/showuser" class="text-black font-bold hoverable"><li>รายชื่อนักวิจัย</li></router-link>
            <router-link v-if="isLogins" to="/showresearch" class="text-black font-bold hoverable"><li>รายชื่องานวิจัย</li></router-link>
          </ul>
        </details>
      </li> -->
</template>

<!-- <template>
  <div class="navbar bg-blue-900 flex justify-between items-center h-20">
    <div>
      <button class="btn btn-ghost text-2xl font-extrabold text-white" @click="redirectToPath">Research</button>
    </div>
    <div>
      <div class="dropdown mr-10 " v-if="isLogins">
        <button class="btn btn-ghost text-white font-bold hoverable">รายชื่อทั้งหมด <i class="fas fa-caret-down ml-2"></i></button>
        <div class="dropdown-content">
          <router-link to="/showuser" class="text-white font-bold hoverable">รายชื่อนักวิจัย</router-link>
          <router-link to="/showresearch" class="text-white font-bold hoverable">รายชื่องานวิจัย</router-link>
        </div>
      </div>
      <div class="dropdown mr-10" v-if="isLogins">
        <button class="btn btn-ghost text-white font-bold hoverable">เพิ่มข้อมูล <i class="fas fa-caret-down ml-2"></i></button>
        <div class="dropdown-content">
          <router-link to="/add" class="text-white font-bold hoverable">จาก IEEE</router-link>
          <router-link to="/addscopus" class="text-white font-bold hoverable">จาก Scopus</router-link>
          <router-link to="/addResearch" class="text-white font-bold hoverable">ฟอร์มเพิ่มข้อมูล</router-link>
        </div>
      </div>
      <button v-if="isLogins" class="btn btn-error" @click="logout">ออกจากระบบ</button>
    </div>
  </div>
</template> -->

  
<script setup>
  import { computed, ref } from 'vue';
  import { useRoute } from 'vue-router'; 
  import { useStore } from 'vuex'; 
  import router from "../router";

  const store = useStore();
  const route = useRoute();
  const isLogins = computed(() => store.state.isLogin);
  const redirectToPath = () => {
    router.push({ name: "testhome" });
  };
  const logout = () => {
    // ทำการออกจากระบบ โดยอาจจะต้อง dispatch action ไปยัง store หรือทำการ clear session ตามที่คุณต้องการ
    // ทำการออกจากระบบ โดยการเรียกใช้ mutations เพื่อเปลี่ยนสถานะการเข้าสู่ระบบเป็น false
    store.commit('logout');
    router.push({ name: "login" });
  };

</script>


   
<style>
.hoverable:hover {
    color: rgb(255, 255, 255); 
   
    text-decoration: underline; /* เพิ่มขีดเส้นใต้ */
    cursor: pointer; /* เปลี่ยนรูปแบบของ cursor เมื่อวางเม้าส์ที่ element */
} 
.text-black {
  color:rgb(255, 255, 255); /* สีแดง */
}
.text-4xl {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* เพิ่มเอฟเฟ็กต์เงา */
  -webkit-text-stroke-width: 1px; /* เพิ่มเส้นขอบ */
  -webkit-text-stroke-color: white; /* สีขอบ */
}
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000; /*เพื่อให้ Navbar อยู่ด้านบนสุด */
 
  text-align: center;
}
</style>