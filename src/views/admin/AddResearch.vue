
<template>
  <br><br><br><br>
  <form class="flex items-center justify-center" @submit.prevent="submitForm">
    <div class="space-y-12 ">
      <div class="border-b border-gray-900/10 pb-12">
        <h2 class="text-xl text-center leading-7 text-gray-900">แบบฟอร์มเพิ่มข้อมูลงานวิจัย</h2>
        
          <!------------------------- แบบฟอร์มข้อมูลงานวิจัย -------------------------------->
          <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
          <!-- ชื่องานวิจัย -->
          <div class="sm:col-span-4">
            <label class="block text-sm font-medium leading-6 text-gray-900">ชื่องานวิจัย</label>
            <textarea v-model="formData.title" id="title" name="title" rows="3" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
          </div>
          <!-- ปีที่เผยแพร่ -->
          <div class="sm:col-span-3">
            <label class="block text-sm font-medium leading-6 text-gray-900">ปีที่เผยแพร่</label>
            <div class="mt-2">
              <input v-model="formData.publication_year" type="number" id="publication_year" name="publication_year" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder=" เช่น 2023" />
            </div>
          </div>
          <!-- ชื่อวารสารหรือบทความ -->
          <div class="col-span-full">
            <label class="block text-sm font-medium leading-6 text-gray-900">ชื่อวารสารหรือบทความ</label>
            <div class="mt-2">
              <textarea v-model="formData.publication_title" id="publication_title" name="publication_title" rows="3" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>
          <!-- abstract -->
          <div class="col-span-full">
            <label class="block text-sm font-medium leading-6 text-gray-900">Abstract</label>
            <div class="mt-2">
              <textarea v-model="formData.abstract" id="abstract" name="abstract" rows="5" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>

          <!-- หมายเลขงานวิจัย -->
          <div class="sm:col-span-4">
            <label class="block text-sm font-medium leading-6 text-gray-900">หมายเลขงานวิจัย </label>
            <div class="mt-2">
              <input v-model="formData.article_number" type="text" name="article_number" id="article_number" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>
          <!-- ประเภทงานวิจัย -->
          <div class="sm:col-span-4">
            <label class="block text-sm font-medium leading-6 text-gray-900">ประเภทงานวิจัย</label>
            <div class="mt-2">
              <select v-model="formData.content_type" id="content_type" name="content_type"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                <option value="" disabled selected>เลือก</option>
                <option>Journals</option>
                <option>Conferences</option>
                <option>Books</option>
              </select>
            </div>
          </div>
          <!-- หมายเลขหน้า -->
          <div class="sm:col-span-4">
            <label class="block text-sm font-medium leading-6 text-gray-900">หมายเลขหน้า</label>
            <div class="mt-2 flex">
              <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
                <input v-model="formData.start_page" type="text" name="start_page" id="start_page"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="1" />
              </div>
              <pre> - </pre>
              <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
                <input v-model="formData.end_page" type="text" name="end_page" id="end_page"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="10" />
              </div>
            </div>
          </div>
          <!-- doi -->
          <div class="sm:col-span-4">
            <label class="block text-sm font-medium leading-6 text-gray-900">doi </label>
            <div class="mt-2">
              <input v-model="formData.doi" type="text" name="doi" id="doi"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>
          <!-- แหล่งที่เผยแพร่ -->
          <!-- <div class="sm:col-span-4">
            <label class="block text-sm font-medium leading-6 text-gray-900">แหล่งที่เผยแพร่</label>
            <div class="mt-2">
              <input v-model="formData.publisher" type="text" name="publisher" id="publisher" autocomplete="publisher" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div> -->
          <div class="sm:col-span-4">
            <label class="block text-sm font-medium leading-6 text-gray-900">แหล่งที่เผยแพร่</label>
            <div class="mt-2">
              <select v-model="formData.publisher" id="publisher" name="publisher" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                <!-- <option value="01">Scopus</option>
                <option value="02">IEEE</option>
                <option value="03">TCI1</option>
                <option value="04">TCI2</option>
                <option value="05">TCI3</option> -->
                <option value="" disabled selected>เลือก</option>
                <option>scopus</option>
                <option>IEEE</option>
                <option>TCI1</option>
                <option>TCI2</option>
                <option>TCI3</option>
                <option>อื่นๆ</option>
              </select>
            </div>
          </div>
          <!-- keyword -->
          <!-- <div class="sm:col-span-4">
              <label class="block text-sm font-medium leading-6 text-gray-900">คำสำคัญ/keyword</label>
              <div class="mt-2" v-for="(keywordIndex) in author.degree" :key="keywordIndex">
                  <input v-model="formData.keyword" type="text" :id="keyword"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  <button @click="removeKeyword(keywordIndex)">ลบ</button>
              </div>
              <div>
                  <button @click="addKeyword(index)" class="btn btn-warning rounded-none">เพิ่มรายการวุฒิการศึกษา</button>
              </div>
          </div>  -->
          
          <!-- keyword -->
          <div class="sm:col-span-4">
              <label class="block text-sm font-medium leading-6 text-gray-900">คำสำคัญ/keyword</label>
              <div class="mt-2">
                  <input v-model="formData.keywords" type="text" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
              <div>
                  <button @click="addKeyword()" class="btn btn-warning rounded-none">เพิ่มรายการ keyword</button>
              </div>
          </div>

          
        </div>
      </div>


      <!-- ----------------------เลือกนักวิจัยที่มีอยู๋ในระบบ--------------------- -->
   
      <div class="sm:col-span-full">
        <div class="relative">
          <label class="block text-sm font-medium leading-6 text-gray-900">รายชื่อนักวิจัยที่มีอยู่ในระบบ</label>
          <button @click="openOffAuthorDropdown" class="select select-bordered w-full text-black flex-grow bg-white relative z-10 items-center">
            {{ dropdownButtonTextAuthor }}
          </button>
          <div v-if="isOpenOff" class="absolute inset-x-0 mt-1 py-1 px-2 bg-white text-black rounded shadow-lg z-20">
            <!-- เพิ่ม checkbox สำหรับเลือกนักวิจัย -->
            <label v-for="(author, index) in all_author" :key="index" class="flex items-center cursor-pointer">
              <input type="checkbox" :value="author.n.full_name" :checked="isSelectedAuthor(author.n.full_name)" class="form-checkbox rounded" @change="handleAuthorSelection(author.n.full_name)">
              <span class="ml-2 text-black">{{ author.n.full_name}}</span>
            </label>
          </div>
        </div>
      </div>


      <button @click="addNewAuthor" class="btn btn-warning rounded-none">เพิ่มข้อมูลนักวิจัย</button>

     <!-- ----------------------------------แบบฟอร์มข้อมูลนักวิจัย------------------------- -->
     <!-- ใช้ v-for เพื่อวนลูปผ่านแต่ละนักวิจัยร่วมในอาร์เรย์ formData.authors และส่ง index เข้าไปในฟังก์ชันที่สร้างขึ้นมาเพื่อเพิ่มหรือลบ  -->
     <!-- โดย index จะใช้เพื่อให้แต่ละรายการของนักวิจัยร่วมมีการเลขที่ต่อเนื่อง และใช้เป็นส่วนหนึ่งของ ID และชื่อของฟิลด์ input เพื่อให้ง่ายต่อการอ้างอิงและการจัดการข้อมูลใน Vue.js  -->
     <div class="border-b border-gray-900/10 pb-12" v-for="(author, index) in formData.authors" :key="index">
      <h2 class="text-base font-semibold leading-7 text-gray-900">นักวิจัยร่วม</h2>
      <p class="mt-1 text-sm leading-6 text-gray-600">คนที่ {{ index + 1 }}</p>
      <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
          <!-- ชื่อ-นามสกุล (ภาษาอังกฤษ) -->
          <div class="sm:col-span-3">
              <label class="block text-sm font-medium leading-6 text-gray-900">ชื่อ-นามสกุล (ภาษาอังกฤษ)</label>
              <div class="mt-2">
                  <input v-model="author.full_name" type="text" :id="'full_name_' + index"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
          </div>
          <!-- ชื่อ-นามสกุล (ภาษาไทย) -->
          <div class="sm:col-span-3">
              <label class="block text-sm font-medium leading-6 text-gray-900">ชื่อ-นามสกุล (ภาษาไทย)</label>
              <div class="mt-2">
                  <input v-model="author.name_th" type="text" :id="'name_th_' + index"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
          </div>

          <!-- หมายเลขนักวิจัย -->
          <div class="sm:col-span-4">
              <label class="block text-sm font-medium leading-6 text-gray-900">หมายเลขนักวิจัย</label>
              <div class="mt-2">
                  <input v-model="author.id" type="number" :id="'id_' + index"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
          </div>

          <!-- วุฒิการศึกษา -->
          <!-- <div class="sm:col-span-4">
              <label class="block text-sm font-medium leading-6 text-gray-900">วุฒิการศึกษา</label>
              <div class="mt-2" v-for="(degree, degreeIndex) in author.degree" :key="degreeIndex">
                  <input v-model="author.degree[degreeIndex]" type="text" :id="'degree_name_' + index + '_' + degreeIndex" :autocomplete="'degree_name_' + index + '_' + degreeIndex" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  <button @click="removeDegree(index, degreeIndex)">ลบ</button>
              </div>
              <div>
                  <button @click="addDegree(index)" class="btn btn-warning rounded-none">เพิ่มรายการวุฒิการศึกษา</button>
              </div>
          </div> -->


         <div class="sm:col-span-4">
              <label class="block text-sm font-medium leading-6 text-gray-900">วุฒิการศึกษา</label>
              <div class="mt-2" v-for="(degree, degreeIndex) in author.degree" :key="degreeIndex">
                  <input v-model="degree.degree_name" type="text" :id="'degree.degree_name_' + index + '_' + degreeIndex"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  <button @click="removeDegree(index, degreeIndex)">ลบ</button>
              </div>
              <div>
                  <button @click="addDegree(index)" class="btn btn-warning rounded-none">เพิ่มรายการวุฒิการศึกษา</button>
              </div>
          </div> 
          <!-- สาขาที่เชี่ยวชาญ -->

          <div class="sm:col-span-full">
            <div class="relative">
              <label class="block text-sm font-medium leading-6 text-gray-900">สาขาที่เชี่ยวชาญ</label>
              <button @click="toggleDropdown(index)" class="select select-bordered w-full text-black flex-grow bg-white relative z-10 items-center">
                {{ dropdownButtonText(index) }}
              </button>

              <div v-if="isOpen[index]" class="absolute inset-x-0 mt-1 py-1 px-2 bg-white text-black rounded shadow-lg z-20">
                <label v-for="expertise in search_expertise" :key="expertise.n.id_e" class="flex items-center cursor-pointer">
                  <input type="checkbox" :value="expertise.n.expertise_name" :checked="isSelected(index, expertise.n.expertise_name)" class="form-checkbox rounded" @change="handleExpertiseSelection(index, expertise.n.expertise_name)"> <!-- ต้องการส่งindexauthor และชื่อ -->
                  <span class="ml-2 text-black">{{ expertise.n.expertise_name }}</span>
                </label>
              </div>
            </div>
          </div>

          <!-- <div class="sm:col-span-full">
              <label class="block text-sm font-medium leading-6 text-gray-900">สาขาที่เชี่ยวชาญ</label>
              <div class="mt-2">
                  <select v-model="author.expertise" :id="'expertise_' + index" :name="'expertise_' + index" :autocomplete="'expertise_' + index" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                      <option>United States</option>
                      <option>Canada</option>
                      <option>Mexico</option>
                  </select>
              </div>
          </div> -->
          <!-- อีเมล -->
          <div class="sm:col-span-full">
              <label for="email" class="block text-sm font-medium leading-6 text-gray-900">อีเมล</label>
              <div class="mt-2">
                  <input v-model="author.email" type="email" :id="'email_' + index" :name="'email_' + index"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
          </div>

          <p class="mt-1 text-sm leading-6 text-gray-600">ที่อยู่สำนักงาน</p>
          <!-- ชื่อสำนักงาน -->
          <div class="col-span-full">
              <label class="block text-sm font-medium leading-6 text-gray-900">ชื่อสำนักงาน</label>
              <div class="mt-2">
                  <input v-model="author.affiliation" type="text" :id="'affiliation_' + index" :name="'affiliation_' + index"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
          </div>
          <!-- จังหวัดสำนักงาน -->
          <div class="sm:col-span-3">
              <label class="block text-sm font-medium leading-6 text-gray-900">จังหวัด</label>
              <div class="mt-2">
                  <input v-model="author.province" type="text" :id="'province_' + index" :name="'province_' + index"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
          </div>
          <!-- ประเทศสำนักงาน -->
          <div class="sm:col-span-3">
              <label class="block text-sm font-medium leading-6 text-gray-900">ประเทศ</label>
              <div class="mt-2">
                  <input v-model="author.country" type="text" :id="'country_' + index" :name="'country_' + index"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
          </div>
          <button @click="removeAuthor(index)">ลบ</button>
      </div>
  </div>

      <div>
        <button @click="addAuthor" class=" btn btn-warning rounded-none ">เพิ่มรายการชื่อนักวิจัยร่วม</button>
      </div>
    </div>

    

  </form>


   <div class="mt-6 flex items-center justify-end gap-x-6">
      <button type="button" class="text-sm font-semibold leading-6 text-gray-900">ยกเลิก</button>
      <button type="submit" @click="formImportData" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">บันทึก</button>
  </div>
  
</template>

  
<script setup>
import {ref, onMounted , computed} from 'vue'
import axios from 'axios' //ใช้เพื่อยิงไปที่ตัว api
import router from '../../router'



const formData = ref({
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
  authors: [{
    full_name: '',
    name_th: '', 
    office: '',
    expertise: [{expertise_name: ''}],
    country: '',
    email: '',
    degree: [{degree_name: ''}],
    id: '',
    province: ''
  }]
});


// -------------------------author-------------------

const isOpenOff = ref((false));// ประกาศ reactive ref สำหรับเก็บสถานะการเปิดหรือปิด dropdown
const all_author = ref({}); 
const fetch_all_author = async () => {
      try {
        const response = await axios.get(`${import.meta.env.VITE_FASTAPI}/all_author`, {
          withCredentials: true,
        });
        all_author.value = response.data;
        console.log(all_author.value);
      } catch (error) {
        console.log(error);
      }
};

 // ฟังก์ชันสำหรับเปิดหรือปิด dropdown
 const openOffAuthorDropdown = () => {
    isOpenOff.value = !isOpenOff.value;
};
const handleAuthorSelection = (authorName) => {
   
    // ตรวจสอบว่าชื่อนักวิจัยนี้ถูกเลือกหรือไม่
    const isSelected = isSelectedAuthor(authorName);
    // หากชื่อนักวิจัยถูกเลือกแล้วให้ลบออกจากรายการ
    if (isSelected) {
        formData.value.authors = formData.value.authors.filter(author => author.full_name !== authorName);
    } else {
        // หากชื่อนักวิจัยยังไม่ถูกเลือกให้เพิ่มเข้าไปในรายการ
        formData.value.authors.push({ full_name: authorName});
    }
    console.log(formData.value);
};

// ฟังก์ชันที่ใช้สำหรับตรวจสอบว่านักวิจัยชื่อนี้ถูกเลือกหรือไม่ ในcheckbox
const isSelectedAuthor = (authorName) => {
    return formData.value.authors.some(author => author.full_name === authorName);
};


const dropdownButtonTextAuthor = computed(() => {
  if (formData.value.authors) {
    if (formData.value.authors.length > 0) {
        // สร้างข้อความที่มีรายชื่อนักวิจัยที่ถูกเลือกแสดงบนปุ่ม dropdown
        return formData.value.authors.map(author => author.full_name).join(', ');
    } else {
        // ถ้าไม่มีนักวิจัยที่ถูกเลือกให้แสดงข้อความ 'Open Dropdown'
        return "เลือก";
    }
  } else {
      return "เลือก";
  }

});




// เพิ่มนักวิจัยร่วม
const addAuthor = () => {
  if (!formData.value.authors) {
    // ถ้า formData.authors ยังไม่ได้ถูกกำหนดค่าให้เป็นอาร์เรย์ ให้กำหนดค่าเริ่มต้นเป็นอาร์เรย์ว่าง
    formData.value.authors = [];
  }


  formData.value.authors.push({
    full_name: '',
    name_th: '', 
    office: '',
    expertise: [{expertise_name: ''}],
    country: '',
    email: '',
    degree: [{degree_name: ''}],
    id: '',
    province: ''
  });

  console.log(formData.value)
};

// ------------------------degree--------------------

// เพิ่มวุฒิการศึกษา
const addDegree = (authorIndex) => {

  // formData.value.authors[authorIndex].degree.push({degree_name: '' });
  formData.value.authors[authorIndex].degree.push({degree_name: '' });
  console.log(formData.value)
};

const removeDegree = (authorIndex, degreeIndex) => {
    formData.value.authors[authorIndex].degree.splice(degreeIndex, 1);
};

// ----------------------------form-------------------------

// ลบนักวิจัยร่วม
const removeAuthor = (index) => {
    // ลบอาร์เรย์ที่ตำแหน่ง index ออกจาก formData.authors
    formData.authors.splice(index, 1);
};

async function formImportData() {
  // ลบช่องว่างซ้ายและขวาของข้อความทุกอย่างที่กรอกลงฟอร์ม
  for (let field in formData.value) {
        if (typeof formData.value[field] === 'string') { // เป็น string หรือไม่ โดยใช้ typeof
            formData.value[field] = formData.value[field].trim();  // เป็นตัดช่องว่างซ้ายขวา
        }
  }
  console.log(formData.value)
    try {
        const response = await axios.post(`${import.meta.env.VITE_FASTAPI}/form_import_data`, formData.value);
        console.log("เพิ่มสำเร็จ");
        alert("เพิ่มข้อมูลสำเร็จ");
        console.log(response.data);
        router.push("/showuser");
    } catch (error) {
        console.error("เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง API:", error);
        alert("ไม่สามารถเพิ่มข้อมูลได้");
        
    }
}
// ----------------- keyword----------------
const addKeyword = () => {
    const newKeyword = formData.value.keywords.trim();
      if (newKeyword !== '') {
        formData.value.keywords += (formData.value.keywords === '') ? newKeyword : `, ${newKeyword}`;
      }
};

// -----------------------------expertise---------------------

    const search_expertise = ref({}); // ประกาศตัวแปร ref สำหรับเก็บข้อมูลสาขาที่เชี่ยวชาญ
    const isOpen = ref({}); // ประกาศตัวแปร ref สำหรับเก็บสถานะการแสดง dropdown

    const fetch_search_expertise = async () => {
      try {
        const response = await axios.get(`${import.meta.env.VITE_FASTAPI}/search_expertise`, {
          withCredentials: true,
        });
        search_expertise.value = response.data;
        console.log(search_expertise.value)
      } catch (error) {
        console.log(error);
      }
    };

    // ฟังก์ชันสำหรับเปิดหรือปิด dropdown
    const toggleDropdown = (authorIndex) => {
      isOpen.value[authorIndex] = !isOpen.value[authorIndex];
    };


    onMounted(() => {
      fetch_search_expertise();
      formData.value.authors.forEach((index) => {
        isOpen.value[index] = false;
      });
      fetch_all_author();
    });

// เมื่อเลือกตัวเลือกสาขาที่เชี่ยวชาญ
const handleExpertiseSelection = (authorIndex , expertiseName) => { //expertiseId, 
    // ตัดช่องว่างซ้ายขวาก่อนเพิ่มสาขาที่เชี่ยวชาญ
    expertiseName = expertiseName.trim();
    // ตรวจสอบว่าสาขาที่เชี่ยวชาญนี้มีอยู่ในอาร์เรย์ expertise หรือไม่
    const expertiseIndex = formData.value.authors[authorIndex].expertise.findIndex(exp => exp.expertise_name === expertiseName);
    if (expertiseIndex === -1 && expertiseName !== '') {
        // หากไม่พบสาขาที่เชี่ยวชาญนี้ในอาร์เรย์ expertise ให้เพิ่มลงไป
        formData.value.authors[authorIndex].expertise.push({ expertise_name: expertiseName });
        console.log(formData.value)
      } else if (expertiseName === '') {
        // หากชื่อสาขาว่างเปล่า ให้แสดงข้อความแจ้งเตือน
        alert("กรุณากรอกชื่อสาขาที่เชี่ยวชาญ");
      }
      else {
        // หากพบสาขาที่เชี่ยวชาญนี้ในอาร์เรย์ expertise ให้ลบออก
        formData.value.authors[authorIndex].expertise.splice(expertiseIndex, 1);
        console.log(formData.value)
    }
    // กรองค่าที่เป็นค่าว่างออกจากอาร์เรย์ expertise
    formData.value.authors[authorIndex].expertise = formData.value.authors[authorIndex].expertise.filter(exp => exp.expertise_name !== '');
};
// ฟังก์ชันเช็คสถานะของ checkbox ว่าถูกเลือกหรือไม่
const isSelected = (authorIndex, expertiseName) => {
    return formData.value.authors[authorIndex].expertise.some(exp => exp.expertise_name === expertiseName);
};


// แก้ไขฟังก์ชัน dropdownButtonText เพื่อให้ทำงานกับ Vue.js โดยใช้ function declaration
function dropdownButtonText(index) {
  // ตรวจสอบว่ามีสาขาที่ถูกเลือกไว้หรือไม่
  if (formData.value.authors[index].expertise.length > 0) {
    // ถ้ามี ให้สร้างข้อความแสดงสาขาที่ถูกเลือก
    return formData.value.authors[index].expertise.map(exp => exp.expertise_name).join(", ");
  } else {
    // ถ้าไม่มี ให้แสดงข้อความ "เลือก"
    return "เลือก";
  }
}


</script>
  
<style lang="scss" scoped>
  
</style>