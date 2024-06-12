
<template>
  <br><br>
  <div class="max-w-4xl mx-auto mt-12 pb-18 p-6 bg-white rounded-md shadow-md">
    <form class="flex items-center justify-center" @submit.prevent="submitForm">
      <div class="space-y-12 ">
        <div class=" pb-12">
          <h2 class="text-xl text-center leading-7 text-gray-900">แก้ไขข้อมูลงานวิจัย</h2>
          
            <!------------------------- แบบฟอร์มแก้ไขข้อมูลงานวิจัย -------------------------------->
            <div v-if="edit_research.t" class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
            <!-- ชื่องานวิจัย -->
            
            <div class="sm:col-span-full">
                <label class="block text-sm font-medium leading-6 text-gray-900">ชื่องานวิจัย</label>
                <textarea v-model="edit_research.t.title" id="title" name="title" rows="2" class="textarea textarea-bordered w-full " placeholder=" ชื่องานวิจัย"></textarea>
            </div>
            
            <!-- ปีที่เผยแพร่ -->
            <div class="sm:col-span-2">
              <label class="block text-sm font-medium leading-6 text-gray-900">ปีที่เผยแพร่</label>
              <div class="mt-2">
                <input v-model="edit_research.t.publication_year" type="number" id="publication_year" name="publication_year" class="input input-bordered w-full shadow-none " placeholder="2024" />
              </div>
            </div>
            <!-- ชื่อวารสารหรือบทความ -->
            <div class="col-span-full">
              <label class="block text-sm font-medium leading-6 text-gray-900">ชื่อวารสารหรือบทความ</label>
              <div class="mt-2">
                <textarea v-model="edit_research.t.publication_title" id="publication_title" name="publication_title" rows="3" class="textarea textarea-bordered w-full " placeholder="ชื่อวารสารหรือบทความ"></textarea>
              </div>
            </div>
             <!-- abstract -->
          <div class="col-span-full">
            <label class="block text-sm font-medium leading-6 text-gray-900">บทคัดย่อ</label>
            <div class="mt-2">
              <textarea v-model="edit_research.t.abstract" id="abstract" name="abstract" rows="5" class="textarea textarea-bordered w-full " placeholder="บทคัดย่อ"></textarea>
            </div>
          </div>
            <!-- หมายเลขงานวิจัย -->
            <div class="sm:col-span-3">
              <label class="block text-sm font-medium leading-6 text-gray-900">หมายเลขงานวิจัย </label>
              <div class="mt-2">
                <input v-model="edit_research.t.article_number" type="text" name="article_number" id="article_number" class="input input-bordered w-full shadow-none " placeholder="หมายเลขงานวิจัย"/>
              </div>
            </div>
            <!-- ประเภทงานวิจัย -->
            <div class="sm:col-span-2">
              <label class="block text-sm font-medium leading-6 text-gray-900">ประเภทงานวิจัย</label>
              <div class="mt-2">
                <select v-model="edit_research.t.content_type" id="content_type" name="content_type"  class="select select-bordered w-full">
                  <option value="" disabled selected>กรุณาเลือก</option>
                  <option>Journal</option>
                  <option>Conferences</option>
                  <option>Conference Proceeding</option>
                  <option>Book</option>
                  <option>Book Series</option>
                </select>
              </div>
            </div>
            <!-- หมายเลขหน้า -->
            <div class="sm:col-span-4">
              <label class="block text-sm font-medium leading-6 text-gray-900">หมายเลขหน้า</label>
              <div class="mt-2 flex">
                <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
                  <input v-model="edit_research.t.start_page" type="text" name="start_page" id="start_page"  class="input input-bordered w-full shadow-none " placeholder="1" />
                </div>
                <pre class="flex items-center"> - </pre>
                <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
                  <input v-model="edit_research.t.end_page" type="text" name="end_page" id="end_page"  class="input input-bordered w-full shadow-none " placeholder="10" />
                </div>
              </div>
            </div>
            <!-- doi -->
            <div class="sm:col-span-3">
              <label class="block text-sm font-medium leading-6 text-gray-900">doi </label>
              <div class="mt-2">
                <input v-model="edit_research.t.doi" type="text" name="doi" id="doi"  class="input input-bordered w-full shadow-none " placeholder="10.123/456789"/>
              </div>
            </div>
            <!-- แหล่งที่เผยแพร่ -->
            <!-- <div class="sm:col-span-4">
              <label class="block text-sm font-medium leading-6 text-gray-900">แหล่งที่เผยแพร่</label>
              <div class="mt-2">
                <input v-model="formData.publisher" type="text" name="publisher" id="publisher" autocomplete="publisher" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div> -->
            <div class="sm:col-span-2">
              <label class="block text-sm font-medium leading-6 text-gray-900">แหล่งที่เผยแพร่</label>
              <div class="flex flex justify-start">
                <div class="mt-2 ">
                  <select v-model="edit_research.t.publisher" id="publisher" name="publisher"  class="select select-bordered w-28 mr-3 ">
                    <!-- <option value="01">Scopus</option>
                    <option value="02">IEEE</option>
                    <option value="03">TCI1</option>
                    <option value="04">TCI2</option>
                    <option value="05">TCI3</option> -->
                    <option value="" disabled selected>กรุณาเลือก</option>
                    <option>scopus</option>
                    <option>IEEE</option>
                    <option>TCI1</option>
                    <option>TCI2</option>
                    <option>TCI3</option>
                    <option>อื่นๆ</option>
                  </select>
                </div>
                <input v-if="edit_research.t.publisher === 'อื่นๆ' " v-model="otherPublisherInput" type="text" class="input input-bordered w-48 mt-2 shadow-none" placeholder="ระบุแหล่งที่เผยแพร่"/>
              </div>
            </div>
            <div class="sm:col-span-full">
              <label class="block text-sm font-medium leading-6 text-gray-900">abstract_url</label>
              <div class="mt-2">
                <input v-model="edit_research.t.abstract_url" type="text" name="abstract_url" id="abstract_url" autocomplete="abstract_url" class="input input-bordered w-full shadow-none " placeholder="https://www.example.com/"/>
              </div>
            </div>

            <!-- keyword -->
            <div class="col-span-full">
              <label class="block text-sm font-medium leading-6 text-gray-900">คำสำคัญ</label>
              <div class="mt-2">
                <textarea v-model="edit_research.t.keyword" id="keyword" name="keyword" rows="5" class="textarea textarea-bordered w-full " placeholder="คำสำคัญ แต่ละคำคั่นด้วย (,)"></textarea>
              </div>
            </div>

          </div>
        </div>
    </div>
    </form>
    <br>
      <div class="mt-6 flex items-center justify-end gap-x-6">
          <button type="button"  @click="cancelForm" class="text-sm font-semibold leading-6 text-gray-900">ยกเลิก</button>
          <button type="submit" @click="editFormResearch" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">บันทึก</button>
      </div>
  </div>
  
     
    <br>
  </template>
  
    
<script setup>
import {ref, onMounted} from 'vue'
import axios from 'axios' //ใช้เพื่อยิงไปที่ตัว api
import {useRouter,useRoute} from 'vue-router'
import routers from "../../router";
import { useStore } from "vuex";
const route = useRoute()// ใช้ useRoute สำหรับการเข้าถึงพารามิเตอร์ของเส้นทางปัจจุบัน
const router = useRouter(); // ใช้ useRouter สำหรับการนำทาง
const store = useStore();
//  console.log(router.params.id)

 const edit_research = ref({
    keyword: '',
    abstract: '',
    title: '',
    publication_year: '',
    publication_title: '',
    article_number: '',
    content_type: '',
    start_page: '',
    end_page: '',
    doi: '',
    publisher: '',
    abstract_url: ''
 })
  
  const otherPublisherInput = ref('');
  const fetch_single_research = async () => {
    await axios
        .get(`${import.meta.env.VITE_FASTAPI}/single_research/${route.params.id}`, {
            withCredentials: true,
        })
        .then((response) => {
            edit_research.value = response.data[0];
            console.log(edit_research.value);
            const publisher = edit_research.value.t.publisher
            // ตรวจสอบค่า publisher ว่าตรงกับ options ใน dropdown หรือไม่
          if (!['scopus', 'IEEE', 'TCI1', 'TCI2', 'TCI3'].includes(publisher)) {
              // หากไม่ตรงกับ options ใน dropdown ให้เลือก "อื่นๆ"
              edit_research.value.t.publisher = 'อื่นๆ';
              // แสดงค่าที่ได้รับมาจากข้อมูล research ในช่อง input ของ "อื่นๆ"
              otherPublisherInput.value = publisher;
          }
        })
        .catch((error) => {
            console.error("เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง API:", error);

        });
  }
 
 onMounted(() => fetch_single_research());
  // ----------------------------form-------------------------


  async function editFormResearch() {
     // ลบช่องว่างซ้ายและขวาของข้อความทุกอย่างที่กรอกลงฟอร์ม
    
     for (let field in edit_research.value) {
        if (typeof edit_research.value[field] === 'string') { // เป็น string หรือไม่ โดยใช้ typeof
            edit_research.value[field] = edit_research.value[field].trim();  // เป็นตัดช่องว่างซ้ายขวา
        }
    }


    try {
        let edit_publisher = "";
        if(edit_research.value.t.publisher === 'อื่นๆ'){
          edit_publisher = otherPublisherInput.value;
        }
        else{
          edit_publisher = edit_research.value.t.publisher;
        }
        const response = await axios.put(`${import.meta.env.VITE_FASTAPI}/edit_research/${route.params.id}`, {
            abstract: edit_research.value.t.abstract,
            title: edit_research.value.t.title,
            publication_year: edit_research.value.t.publication_year,
            publication_title: edit_research.value.t.publication_title,
            article_number: edit_research.value.t.article_number, 
            content_type: edit_research.value.t.content_type,
            start_page: edit_research.value.t.start_page ,
            end_page: edit_research.value.t.end_page ,
            doi: edit_research.value.t.doi ,
            publisher: edit_publisher,
            abstract_url: edit_research.value.t.abstract_url,
            keyword: edit_research.value.t.keyword
        });
        console.log(edit_research.value);
        console.log("แก้ไขสำเร็จ");
        alert("แก้ไขสำเร็จ");
        console.log(store.state.searchQueryResearch);
        store.commit('setSearchQueryResearch', store.state.searchQueryResearch);
        console.log(store.state.searchQueryResearch);
        router.push({ name: 'showresearch', query: { search: store.state.searchQueryResearch } });
       
        console.log(response.data);
        
    } catch (error) {
        console.error("เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง API:", error);
        alert("ไม่สามารถแก้ไขข้อมูลได้");
    }
}

  // ----------------- keyword----------------
const temporaryKeywords = ref([''])
const addKeyword = () => {
    temporaryKeywords.value.push('');

    console.log(temporaryKeywords.value)
};
const removeKeyword = index => {
    temporaryKeywords.value.splice(index, 1);
};
  


const cancelForm = () => {
  try {
    const isSure = confirm("คุณแน่ใจที่จะยกเลิกใช่ไหม?");
    if (isSure) {
      router.push("/showresearch");
    } else {
      console.log("ยกเลิกฟอร์ม");
    }
  } catch (error) {
    console.log(error);
  }
};
  
  </script>
    
  <style lang="scss" scoped>
    
  </style>