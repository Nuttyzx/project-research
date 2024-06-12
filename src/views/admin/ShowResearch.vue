<template>
  <br><br>
  <div style="margin: 40px; ">
    <!-- <select class="select select-bordered w-36 max-w-xs" @change="navigateSelect">
      <option value="/showresearch">รายชื่องานวิจัย</option>
      <option value="/showuser">รายชื่อนักวิจัย</option>
      
    </select>
    <br> 
    <br> -->
    <div class="flex justify-end">
      <label class="input input-bordered flex items-center w-96 gap-2">
        <input type="text" class="grow" placeholder="ค้นหาชื่องานวิจัย" v-model="searchQuery" @input="fetch_researchs" />
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path fill-rule="evenodd" d="M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z" clip-rule="evenodd" /></svg>
      </label>
    </div>
    <br>
    <div v-if="notFoundSearchResearch || !paginatedResearchs.length" class="flex justify-center">ไม่พบข้อมูล</div>
    <div v-else>
      <div class="overflow-x-auto ">
          <table class="table table table-zebra ">
          <thead>
              <tr class="text-center text-base ">
              <th></th>
              <th>ชื่องานวิจัย</th>
              <th>ปีที่เผยแพร่</th>
              <th>ชื่อวารสารหรือบทความ</th>
              <th>ประเภทงานวิจัย</th>
              <th>หมายเลขหน้า</th>
              <th>Doi</th>
              <th>แหล่งที่เผยแพร่</th>
              <th>Abstract URL</th>
              <th></th>
              </tr>
          </thead>
          <tbody>
              <tr v-for="(article, index) in paginatedResearchs" :key="index">
                <th class="align-top">{{ index + 1 }}</th>
                <td class="align-top" :style="{ textAlign: article.t.title ? 'left' : 'center' }">{{ article.t.title ? article.t.title : "-" }}</td>
                <td class="align-top" :style="{ textAlign: article.t.publication_year ? 'left' : 'center' }">{{ article.t.publication_year ? article.t.publication_year : "-" }}</td>
                <td class="align-top" :style="{ textAlign: article.t.publication_title ? 'left' : 'center' }">{{ article.t.publication_title ? article.t.publication_title : "-" }}</td>
                <td class="align-top" :style="{ textAlign: article.t.content_type ? 'left' : 'center' }">{{ article.t.content_type ? article.t.content_type : "-" }}</td>
                <td class="align-top" :style="{ textAlign: (article.t.start_page && article.t.end_page) ? 'left' : 'center'  }">{{ (article.t.start_page && article.t.end_page) ? article.t.start_page + ' - ' + article.t.end_page : '-' }}</td>
                <td class="align-top" :style="{ textAlign: article.t.doi ? 'left' : 'center' }">{{ article.t.doi ? article.t.doi : "-" }}</td>
                <td class="align-top" :style="{ textAlign: article.t.publisher ? 'left' : 'center' }">{{ article.t.publisher ? article.t.publisher : "-" }}</td>
                <td class="align-top" :style="{ textAlign: article.t.abstract_url ? 'left' : 'center' }">
                  <template v-if="article.t.abstract_url && article.t.abstract_url !== '-'">
                    <a :href="article.t.abstract_url" target="_blank" class="link link-primary">{{article.t.abstract_url ? article.t.abstract_url : "-"}}</a>
                  </template>
                  <template v-else>
                    <span class="text-black">-</span>
                  </template>
                </td>

              <td class="align-top flex justify-between"> 
                  <router-link :to="{ name: 'editresearch', params: { id: article.id} }">
                  <button class="btn btn-success btn-sm mx-2">แก้ไข</button>
                  </router-link>
                  <button class="btn btn-error btn-sm" @click="checkDelete_research(article.id)">ลบ</button>
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
        <button v-for="page in totalPages" :key="page" :class="{ 'btn-primary': page === currentPage, btn: true }" v-on:click="goToPage(page)">{{ page }}</button> &nbsp;

        <!-- Next button -->
        <button :disabled="currentPage === totalPages || totalPages === 0" v-on:click="goToPage(currentPage + 1)">Next</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted ,watch } from "vue";
import axios from "axios";
import router from "../../router";
import { useStore } from "vuex";
const researchs = ref({});
const store = useStore();
const searchQuery = ref(store.state.searchQueryResearch); // ค่าที่ใช้สำหรับการค้นหา
const notFoundSearchResearch = ref(false);


const fetch_researchs = async () => {
  await axios
    .get(`${import.meta.env.VITE_FASTAPI}/all_researchs`, {
      params: { search: searchQuery.value.trim() },
      withCredentials: true,
    })
    .then((response) => {
      researchs.value = response.data;
      notFoundSearchResearch.value = false;
      console.log(researchs.value);
    })
    .catch((error) => {
      notFoundSearchResearch.value = true;
      console.log(error);
    });
};
onMounted(() => {
  console.log(searchQuery.value)
  fetch_researchs();
});

watch(searchQuery, (newsearchQueryResearch) => {
  store.commit('setSearchQueryResearch', newsearchQueryResearch);
  console.log(store.state.searchQueryResearch)
});

const currentPage = ref(1); // หน้าปัจจุบัน
const itemsPerPage = 15; // จำนวนรายการต่อหน้า

// ฟังก์ชันสำหรับการคำนวณหน้าทั้งหมด
const totalPages = computed(() => {
  const totalItems = Object.keys(researchs.value).length; // จำนวนรายการทั้งหมด
  return Math.ceil(totalItems / itemsPerPage); // จำนวนหน้าทั้งหมด
});
// จำนวนรายการต่อหน้า (itemsPerPage)

// ฟังก์ชันสำหรับการแบ่งข้อมูลที่ต้องการแสดงในหน้าปัจจุบัน
const paginatedResearchs = computed(() => {
  const startIndex = (currentPage.value - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  return Object.values(researchs.value).slice(startIndex, endIndex);
});

// ฟังก์ชันสำหรับการเปลี่ยนหน้า
const goToPage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
    store.commit('setSearchQueryResearch', searchQuery.value);
  }
};


const checkDelete_research = async(research_id) => {
  try {
    const isSure = confirm("คุณต้องการลบข้อมูลงานวิจัยใช่ไหม?");
    if (isSure) {
      await delete_research(research_id)
    } else {
      console.log("ยกเลิกลบข้อมูลงานวิจัย");
    }
  } catch (error) {
    console.log(error);
  }
};

const delete_research = async (research_id) => {
  try {
    await axios.delete(`${import.meta.env.VITE_FASTAPI}/delete_research/${research_id}`);
    alert("ลบข้อมูลงานวิจัยสำเร็จ");

    // ลบสำเร็จ ทำการ fetch ข้อมูลใหม่
    await fetch_researchs();
  } catch (error) {
    console.log(error.response.data);
  }
}

// const delete_research = async (research_title) => {
//   try {
//     await axios.delete(
//       `${import.meta.env.VITE_FASTAPI}/delete_research/${research_title}`
//     );
//     alert("Delete Success");

//     // ลบสำเร็จ ทำการ fetch ข้อมูลใหม่
//     await fetch_researchs();
//   } catch (error) {
//     console.log(error.response.data);
//   }
// };
</script>
<style>
.table td:nth-child(2) {
  min-width: 280px;
}
.table td:nth-child(3) {
  min-width: 160px; 
}
.table td:nth-child(4) {
  min-width: 280px; 
}
.table td:nth-child(5) {
  min-width: 200px;
}
.table td:nth-child(6) {
  min-width: 130px; 
}
.table td:nth-child(8) {
  min-width: 100px; 
}
.table td:nth-child(10) {
  min-width: 160px; 
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