<template>
  <br><br>
  
  <div style="margin: 40px; ">
    <div class="flex justify-end">
      <label class="input input-bordered flex items-center w-96 gap-2">
        <input type="text" class="grow" placeholder="ค้นหาชื่อนักวิจัย เป็นภาษาอังกฤษหรือภาษาไทย" v-model="searchQuery" @input="fetch_authors" />
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path fill-rule="evenodd" d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z" clip-rule="evenodd" /></svg>
      </label>
    </div>
     <br>
    <div v-if="notFoundSearchAuthor || !paginatedAuthors.length" class="flex justify-center">ไม่พบข้อมูล</div>
    <div v-else>
      <div class="overflow-x-auto">
        <table class="table table-zebra">
          <thead>
            <tr class="text-center text-base ">
              <th></th>
              <th>ชื่อภาษาอังกฤษ</th>
              <th>ชื่อภาษาไทย</th>
              <th>วุฒิการศึกษาสูงสุด</th>
              <th>สาขาที่เชี่ยวชาญ</th>
              <th>อีเมล</th>
              <th>หน่วยงาน</th>
              <th>จังหวัด/เมือง</th>
              <th>ประเทศ</th>
              <th>IEEE URL</th>
              <th>เว็บไซต์</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(author, index) in paginatedAuthors" :key="index">
              <!--index คือ ตัวนับจำนวน เริ่มต้น 0 -->
              <th class="align-top">{{ index + 1 }}</th>
              <td class="align-top" :style="{ textAlign: author.n.full_name ? 'left' : 'center' }">
                {{ author.n.full_name ? author.n.full_name : "-" }}
              </td>
              <td class="align-top" :style="{ textAlign: author.n.name_th ? 'left' : 'center' }">
                {{ author.n.name_th ? author.n.name_th : "-" }}
              </td>
              <td class="align-top" :style="{textAlign:author.degrees && author.degrees.length > 0 ? 'left' : 'center',}">
                <template v-if="author.degrees && author.degrees.length > 0">
                  <template v-for="(degree) in author.degrees" :key="degree.id_e">
                    <div>{{ "- " + (degree.degree_name ? degree.degree_name : "-") }}
                      <br><br>
                    </div>
                  </template>
                </template>
                <template v-else>
                  <div>-</div>
                </template>
              </td>
              <td class="align-top" :style="{textAlign:author.expertises && author.expertises.length > 0? 'left': 'center',}">
                <template v-if="author.expertises && author.expertises.length > 0">
                  <template v-for="(expertise) in author.expertises" :key="expertise.id_e">
                    <div>
                      {{"- " +(expertise.expertise_name ? expertise.expertise_name : "-")}}
                      <br><br>
                    </div>
                  </template>
                </template>
                <template v-else>
                  <div>-</div>
                </template>
              </td>
              <td class="align-top" :style="{ textAlign: author.n.email ? 'left' : 'center' }">
                {{ author.n.email ? author.n.email : "-" }}
              </td>
              <td class="align-top" :style="{ textAlign: author.n.office ? 'left' : 'center' }">
                {{ author.n.office ? author.n.office : "-" }}
              </td>
              <td class="align-top" :style="{ textAlign: author.n.province ? 'left' : 'center' }">
                {{ author.n.province ? author.n.province : "-" }}
              </td>
              <td class="align-top" :style="{ textAlign: author.n.country ? 'left' : 'center' }">
                {{ author.n.country ? author.n.country : "-" }}
              </td>
              <td class="align-top" :style="{ textAlign: author.n.authorUrl ? 'left' : 'center' }">
                <template v-if="author.n.authorUrl && author.n.authorUrl !== '-'">
                  <a :href="author.n.authorUrl" target="_blank" class="link link-primary">{{author.n.authorUrl}}</a>
                </template>
                <template v-else>
                  <span class="text-black">-</span>
                </template>
              </td>
              <td class="align-top" :style="{ textAlign: author.n.website ? 'left' : 'center' }">
                  <template v-if="author.n.website && author.n.website !== '-'">
                    <a :href="author.n.website" target="_blank" class="link link-primary">{{author.n.website}}</a>
                  </template>
                  <template v-else>
                    <span class="text-black">-</span>
                  </template>
              </td>
              <td class="align-top flex justify-between" >
                <router-link :to="{ name: 'edituser', params: { id: author.id_author} }">
                  <button class="btn btn-success btn-sm mx-2">แก้ไข</button>
                </router-link>
                <button class="btn btn-error btn-sm" @click="checkDelete_author(author.id_author)">ลบ</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <br>
      <div class="pagination text-center">
        <!-- Previous button -->
        <button :disabled="currentPage === 1" v-on:click="goToPage(currentPage - 1)">Previous</button>&nbsp; 
        
        <!-- Numbered pages -->
        <button v-for="page in totalPages" :key="page" :class="{ 'btn-primary': page === currentPage, btn: true } " v-on:click="goToPage(page)">{{ page }} </button> &nbsp;

        <!-- Next button -->
        <button :disabled="currentPage === totalPages || totalPages === 0" v-on:click="goToPage(currentPage + 1)">Next</button>
      </div>
    </div>
    
  </div>
</template>

<script setup>
import { ref, computed, onMounted ,watch} from "vue";
import axios from "axios";
import router from "../../router";
import { useStore } from "vuex";
const store = useStore();
const authors = ref({});
const searchQuery = ref(store.state.searchQueryAuthor); // ค่าที่ใช้สำหรับการค้นหา
const notFoundSearchAuthor = ref(false);

//ใน function fetch_user จะมีการยิง api
const fetch_authors = async () => {
  console.log(searchQuery.value )
  await axios
    .get(`${import.meta.env.VITE_FASTAPI}/author`, {
      params: { search: searchQuery.value.trim() },
      withCredentials: true,
    })
    .then((response) => {
      authors.value = response.data;
      notFoundSearchAuthor.value = false;
      console.log(authors.value);
      
    })
    .catch((error) => {
      notFoundSearchAuthor.value = true;
      console.log(error);
    });
};


onMounted(() => {
  
  console.log(searchQuery.value)
  fetch_authors();
  
});

watch(searchQuery, (newsearchQuery) => {
  store.commit('setSearchQueryAuthor', newsearchQuery);
  console.log(store.state.searchQueryAuthor)
});

const currentPage = ref(1); // หน้าปัจจุบัน
const itemsPerPage = 8; // จำนวนรายการต่อหน้า

// ฟังก์ชันสำหรับการคำนวณหน้าทั้งหมด
const totalPages = computed(() => {
  const totalItems = Object.keys(authors.value).length; // จำนวนรายการทั้งหมด
  return Math.ceil(totalItems / itemsPerPage); // จำนวนหน้าทั้งหมด
});
// จำนวนรายการต่อหน้า (itemsPerPage)

// ฟังก์ชันสำหรับการแบ่งข้อมูลที่ต้องการแสดงในหน้าปัจจุบัน
const paginatedAuthors = computed(() => {
  const startIndex = (currentPage.value - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  return Object.values(authors.value).slice(startIndex, endIndex);
});

// ฟังก์ชันสำหรับการเปลี่ยนหน้า
const goToPage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
    store.commit('setSearchQueryAuthor', searchQuery.value);
  }
};

// const navigateSelect = (event) =>{
//   const selectedOption = event.target.value;
//   if (selectedOption) { 
//     router.push(selectedOption);
//   }
// }

const checkDelete_author = async(author_id) => {
  try {
    const isSure = confirm("คุณต้องการลบข้อมูลนักวิจัยใช่ไหม?");
    if (isSure) {
      await delete_author(author_id)
    } else {
      console.log("ยกเลิกลบข้อมูลนักวิจัย");
    }
  } catch (error) {
    console.log(error);
  }
};

const delete_author = async (author_id) => {

  try {
    await axios.delete(
      `${import.meta.env.VITE_FASTAPI}/delete_author/${author_id}`
    );
    alert("ลบข้อมูลนักวิจัยสำเร็จ");

    // ลบสำเร็จ ทำการ fetch ข้อมูลใหม่
    await fetch_authors();
  } catch (error) {
    console.log(error.response.data);
  }
};
</script>

<style>
.table td:nth-child(2) {
  min-width: 200px;
}
.table td:nth-child(3) {
  min-width: 200px; 
}
/* 4 คือลำดับของคอลัมน์ คือช่อง วุฒิการศึกษา*/
.table td:nth-child(4) {
  min-width: 240px; 
}
.table td:nth-child(5) {
  min-width: 250px;
}
.table td:nth-child(10) {
  min-width: 160px;
}
.table td:nth-child(7) {
  min-width: 160px; 
}
.table td:nth-child(8) {
  min-width: 140px; 
}
.table td:nth-child(9) {
  min-width: 80px; 
}

/* .table {
  border-collapse: collapse;
  width: 100%;
}

.table th, */
/* กำหนดสีขอบตารางเป็นสีดำ */
/* .table td {
  border: 1px solid #000; 
} */

</style>
