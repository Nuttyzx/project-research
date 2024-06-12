<template>
    <br><br>
      <div class="mt-16">
      <form class="flex items-center justify-center" @submit.prevent="submitForm">
        <div class="space-y-8 ">
          <div class="border-b border-black pb-12">
            <h2 class="text-xl text-center leading-7 text-gray-900 ">บันทึกข้อมูลสำเร็จ</h2>
            <br>
              <!------------------------- แบบฟอร์มข้อมูลงานวิจัย -------------------------------->
              <div class="max-w-4xl mx-auto px-12 bg-white rounded-md border border-black">
              <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <!-- ชื่องานวิจัย -->
              <div class="sm:col-span-full">
                <label class="block text-sm font-medium leading-6 text-gray-900">ชื่องานวิจัย </label><!-----<span class="text-red-500">*</span> ---->
                <textarea v-model="formData.title" id="title" name="title" rows="2" class="textarea textarea-bordered w-full " placeholder=" ชื่องานวิจัย" :disabled="!isEditing"></textarea>
              </div>
              <!-- ปีที่เผยแพร่ -->
              <div class="sm:col-span-2">
                <label class="block text-sm font-medium leading-6 text-gray-900">ปีที่เผยแพร่ </label>
                <div class="mt-2">
                  <input v-model="formData.publication_year" type="number" id="publication_year" name="publication_year" class="input input-bordered w-full shadow-none" placeholder="2024" :disabled="!isEditing"/>
                </div>
              </div>
              <!-- ชื่อวารสารหรือบทความ -->
              <div class="col-span-full">
                <label class="block text-sm font-medium leading-6 text-gray-900">ชื่อวารสารหรือบทความ </label>
                <div class="mt-2">
                  <textarea v-model="formData.publication_title" id="publication_title" name="publication_title" rows="3" class="textarea textarea-bordered w-full" placeholder="ชื่อวารสารหรือบทความ" :disabled="!isEditing"></textarea>
                </div>
              </div>
              <!-- abstract -->
            <div class="col-span-full">
              <label class="block text-sm font-medium leading-6 text-gray-900">บทคัดย่อ</label>
              <div class="mt-2">
                <textarea v-model="formData.abstract" id="abstract" name="abstract" rows="5" class="textarea textarea-bordered w-full" placeholder="บทคัดย่อ" :disabled="!isEditing"></textarea>
              </div>
            </div>
              <!-- หมายเลขงานวิจัย -->
              <div class="sm:col-span-3">
                <label class="block text-sm font-medium leading-6 text-gray-900">หมายเลขงานวิจัย</label>
                <div class="mt-2">
                  <input v-model="formData.article_number" type="text" name="article_number" id="article_number"  class="input input-bordered w-full shadow-none" placeholder="หมายเลขงานวิจัย" :disabled="!isEditing"/>
                </div>
              </div>
              <!-- ประเภทงานวิจัย -->
              <div class="sm:col-span-2">
                <label class="block text-sm font-medium leading-6 text-gray-900">ประเภทงานวิจัย </label>
                <div class="mt-2">
                  <select v-model="formData.content_type" id="content_type" name="content_type"  class="select select-bordered w-full" :disabled="!isEditing">
                    <option value="" disabled selected>กรุณาเลือก</option>
                    <option>Journal</option>
                    <option>Conferences</option>
                    <option>Conference Proceeding</option>
                    <option>Book</option>
                    <option>Book Series</option>
                    <option>อื่นๆ</option>
                  </select>
                </div>
              </div>
              <!-- หมายเลขหน้า -->
              <div class="sm:col-span-4">
                <label class="block text-sm font-medium leading-6 text-gray-900">หมายเลขหน้า</label>
                <div class="mt-2 flex">
                  <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
                    <input v-model="formData.start_page" type="text" name="start_page" id="start_page"  class="input input-bordered w-full shadow-none" placeholder="1" :disabled="!isEditing"/>
                  </div>
                  <pre class="flex items-center"> - </pre>
                  <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
                    <input v-model="formData.end_page" type="text" name="end_page" id="end_page"  class="input input-bordered w-full shadow-none" placeholder="10" :disabled="!isEditing"/>
                  </div>
                </div>
              </div>
              <!-- doi -->
              <div class="sm:col-span-2">
                <label class="block text-sm font-medium leading-6 text-gray-900">doi </label>
                <div class="mt-2">
                  <input v-model="formData.doi" type="text" name="doi" id="doi"  class="input input-bordered w-full shadow-none" placeholder="10.123/456789" :disabled="!isEditing"/>
                </div>
              </div>
              <!-- แหล่งที่เผยแพร่ -->
              <div class="w-12">
                <label class="block text-sm font-medium leading-6 text-gray-900">แหล่งที่เผยแพร่ </label>
                <div class="mt-2">
                  <select v-model="formData.publisher" id="publisher" name="publisher"  class="select select-bordered w-full" :disabled="!isEditing">
                    <option value="" disabled selected>กรุณาเลือก</option>
                    <option value="scopus">scopus</option>
                    <option value="IEEE">IEEE</option>
                    <option value="TCI1">TCI1</option>
                    <option value="TCI2">TCI2</option>
                    <option value="TCI3">TCI3</option>
                    <option value="อื่นๆ">อื่นๆ</option>
                  </select>
                </div>
                <!-- ช่อง input เมื่อเลือก "อื่นๆ" -->
                 <input v-if="formData.publisher === 'อื่นๆ' " v-model="otherPublisherInput" type="text" class="input input-bordered w-full mt-2" placeholder="โปรดระบุ" :disabled="!isEditing"/>
              </div>
              <!-- abstract_url -->
              <div class="sm:col-span-full">
                <label class="block text-sm font-medium leading-6 text-gray-900">abstract_url</label>
                <div class="mt-2">
                  <input v-model="formData.abstract_url" type="text" name="abstract_url" id="abstract_url" class="input input-bordered w-full shadow-none" placeholder="https://www.example.com/" :disabled="!isEditing"/>
                </div>
              </div>
  
             <!-- keyword -->
              <!-- <div class="sm:col-span-4">
                  <label class="block text-sm font-medium leading-6 text-gray-900">คำสำคัญ </label>
                  <div class="mt-2">
                      <div v-for="(tempKeyword, index) in temporaryKeywords" :key="index" class="flex items-center ">
                          <input v-model="temporaryKeywords[index]" type="text" class="input input-bordered w-full shadow-none mr-5 mb-5" placeholder="คำสำคัญ ช่องละ 1 คำสำคัญ" :disabled="!isEditing"/>
                          
                      </div>
                  </div>
                  <div>
                      <button @click="addKeyword()" class="btn btn-warning btn-sm  rounded-md" :disabled="!isEditing">เพิ่มคำสำคัญ</button>
                  </div>
              </div> -->

              <div class="col-span-full">
              <label class="block text-sm font-medium leading-6 text-gray-900">คำสำคัญ</label>
              <div class="mt-2">
                <textarea v-model="formData.keyword" id="keyword" name="keyword" rows="5" class="textarea textarea-bordered w-full " placeholder="คำสำคัญ แต่ละคำคั่นด้วย (,)" :disabled="!isEditing"></textarea>
              </div>
            </div>
  
            </div>
            <br><br>
          </div>
          </div>
    
    
          <!-- ----------------------เลือกนักวิจัยที่มีอยู๋ในระบบ--------------------- -->
          <div>
              <label class="block text-sm font-medium leading-6 text-gray-900">กรณีมีรายชื่อนักวิจัยอยู่ในระบบ</label>
          </div>
          <div class="sm:col-span-full border-b border-black pb-12">
            <div class="relative">
              <label class="block text-sm font-medium leading-6 text-gray-900">รายชื่อนักวิจัยที่มีอยู่ในระบบ</label>
              <button @click="openOffAuthorDropdown" class="select select-bordered w-full text-black flex-grow bg-white relative z-10 items-center" :disabled="!isEditing">
                {{ dropdownButtonTextAuthor }}
              </button>
              <div v-if="isOpenOff" class="absolute inset-x-0 mt-1 py-1 px-2 bg-white text-black rounded shadow-lg z-20">
                <!-- เพิ่ม checkbox สำหรับเลือกนักวิจัย -->
                <label v-for="(author, index) in all_author" :key="index" class="flex items-center cursor-pointer" >
                  <input type="checkbox" :value="author.n.full_name" :checked="isSelectedAuthor(author.n.full_name)" class="form-checkbox rounded" @change="handleAuthorSelection(author.n.full_name)" :disabled="!isEditing">
                  <span class="ml-2 text-black">{{ author.n.full_name}}</span>
                </label>
              </div>
            </div>
          </div>
          
          <div>
              <label class="block text-sm font-medium leading-6 text-gray-900">กรณีไม่มีรายชื่อนักวิจัยอยู่ในระบบ</label>
          </div>
    
         <!-- ----------------------------------แบบฟอร์มข้อมูลนักวิจัย------------------------- -->
         <!-- ใช้ v-for เพื่อวนลูปผ่านแต่ละนักวิจัยร่วมในอาร์เรย์ formData.authors และส่ง index เข้าไปในฟังก์ชันที่สร้างขึ้นมาเพื่อเพิ่มหรือลบ  -->
         <!-- โดย index จะใช้เพื่อให้แต่ละรายการของนักวิจัยร่วมมีการเลขที่ต่อเนื่อง และใช้เป็นส่วนหนึ่งของ ID และชื่อของฟิลด์ input เพื่อให้ง่ายต่อการอ้างอิงและการจัดการข้อมูลใน Vue.js  -->
        <div v-if="isAuthorFormVisible">
         <div class="pb-8" v-for="(author, index) in formData.authors" :key="index" >
          <!-- <br> -->
          <div class="max-w-4xl mx-auto px-12 py-8 bg-white rounded-md border border-black">
          <h2 class="text-base font-semibold leading-7 text-gray-900 ">นักวิจัย</h2>
          <p class="mt-1 text-sm leading-6 text-gray-600">คนที่ {{ index + 1 }}</p>
          <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <!-- ชื่อ-นามสกุล (ภาษาอังกฤษ) -->
              <div class="sm:col-span-3">
                  <label class="block text-sm font-medium leading-6 text-gray-900">ชื่อ-นามสกุล (ภาษาอังกฤษ) </label>
                  <div class="mt-2">
                      <input v-model="author.full_name" type="text" :id="'full_name_' + index"  class="input input-bordered w-full shadow-none" placeholder="ชื่อ-นามสกุล ภาษาอังกฤษ" :disabled="!isEditing"/>
                  </div>
              </div>
              <!-- ชื่อ-นามสกุล (ภาษาไทย) -->
              <div class="sm:col-span-3">
                  <label class="block text-sm font-medium leading-6 text-gray-900">ชื่อ-นามสกุล (ภาษาไทย)</label>
                  <div class="mt-2">
                      <input v-model="author.name_th" type="text" :id="'name_th_' + index"  class="input input-bordered w-full shadow-none" placeholder="ชื่อ-นามสกุล ภาษาไทย" :disabled="!isEditing"/>
                  </div>
              </div>
    
              <!-- หมายเลขนักวิจัย -->
              <div class="sm:col-span-4">
                  <label class="block text-sm font-medium leading-6 text-gray-900">หมายเลขนักวิจัย</label>
                  <div class="mt-2">
                      <input v-model="author.id" type="number" :id="'id_' + index"  class="input input-bordered w-full shadow-none" placeholder="หมายเลขนักวิจัย" :disabled="!isEditing"/>
                  </div>
              </div>
    
              <!-- วุฒิการศึกษา -->
              <div class="sm:col-span-3 ">
                    <label class="block text-sm font-medium leading-6 text-gray-900">วุฒิการศึกษาสูงสุด</label>
                    <div class="flex items-center">
                    <div class="sm:col-span-1">
                        <div class="mt-2 mr-3">
                        <select v-model="leveldegree[index]"  :id="'leveldegree_' + index" :name="'leveldegree_' + index" class="select select-bordered w-full " :disabled="!isEditing">
                            <option value="">กรุณาเลือก</option>
                            <option value="ปริญญาเอก">ปริญญาเอก</option>
                            <option value="ปริญญาโท">ปริญญาโท</option>
                            <option value="ปริญญาตรี">ปริญญาตรี</option>
                        </select>
                        </div>
                    </div>
                    <div class="mt-7" >
                        <input v-model="author.degree[0].degree_name" type="text" :id="'author.degree.degree_name_' + index"  class="input input-bordered w-full shadow-none mr-5 mb-5" placeholder="สาขา" :disabled="!isEditing"/>
                    </div>
                </div>
                </div> 
             <!-- <div class="sm:col-span-full">
                  <label class="block text-sm font-medium leading-6 text-gray-900">วุฒิการศึกษา</label>
                  <div class="mt-2 flex items-center" v-for="(degree, degreeIndex) in author.degree" :key="degreeIndex" >
                      <input v-model="degree.degree_name" type="text" :id="'degree.degree_name_' + index + '_' + degreeIndex"  class="input input-bordered w-full shadow-none mr-5 mb-5" placeholder="ช่องละ 1 วุฒิการศึกษา"  :disabled="!isEditing"/>
                      <button @click="removeDegree(index, degreeIndex)" style="color: red; text-decoration: underline;">ลบ</button>
                  </div>
                  <div>
                      <button @click="addDegree(index)" class="btn btn-warning btn-sm rounded-md" :disabled="!isEditing">เพิ่มวุฒิการศึกษา</button>
                  </div>
              </div>  -->
              <!-- สาขาที่เชี่ยวชาญ -->
    
              <div class="sm:col-span-full">
                <div class="relative">
                  <label class="block text-sm font-medium leading-6 text-gray-900">สาขาที่เชี่ยวชาญ</label>
                  <button @click="toggleDropdown(index)" class="select select-bordered w-full text-black flex-grow bg-white relative z-10 items-center " :disabled="!isEditing">
                    {{ dropdownButtonText(index) }}
                  </button>
                
                  <div v-if="isOpen[index]" class="absolute inset-x-0 mt-1 py-1 px-2 bg-white text-black rounded shadow-lg z-20">
                    <label v-for="expertise in search_expertise" :key="expertise.id" class="flex items-center cursor-pointer" >
                      <input type="checkbox" :value="expertise.id" :checked="isSelected(index, expertise.n.expertise_name)" class="form-checkbox rounded" @change="handleExpertiseSelection(index, expertise.n.expertise_name)" :disabled="!isEditing"> <!-- ต้องการส่งindexauthor และชื่อ -->
                      <span class="ml-2 text-black">{{ expertise.n.expertise_name }}</span>
                    </label>
                  </div>
                </div>
              </div>
    
              <!-- อีเมล -->
              <div class="sm:col-span-full">
                  <label for="email" class="block text-sm font-medium leading-6 text-gray-900">อีเมล</label>
                  <div class="mt-2">
                      <input v-model="author.email" type="email" :id="'email_' + index" :name="'email_' + index"  class="input input-bordered w-full shadow-none" placeholder="example@gmail.com" :disabled="!isEditing" required/>
                  </div>
              </div>
              <!-- authorUrl -->
              <div class="sm:col-span-full">
                  <label for="authorUrl" class="block text-sm font-medium leading-6 text-gray-900">IEEE URL</label>
                  <div class="mt-2">
                      <input v-model="author.authorUrl" type="authorUrl" :id="'authorUrl_' + index" :name="'authorUrl_' + index"  class="input input-bordered w-full shadow-none" placeholder="https://ieeexplore.ieee.org/author/" :disabled="!isEditing"/>
                  </div>
              </div>
              <!-- website -->
              <div class="sm:col-span-full">
                  <label for="website" class="block text-sm font-medium leading-6 text-gray-900">เว็บไซต์</label>
                  <div class="mt-2">
                      <input v-model="author.website" type="website" :id="'website_' + index" :name="'website_' + index"  class="input input-bordered w-full shadow-none"  placeholder="https://www.example.com/" :disabled="!isEditing"/>
                  </div>
              </div>
    
              <p class="mt-1 text-sm leading-6 text-gray-600">ที่อยู่สำนักงาน</p>
              <!-- ชื่อสำนักงาน -->
              <div class="col-span-full">
                  <label class="block text-sm font-medium leading-6 text-gray-900">ชื่อสำนักงาน </label>
                  <div class="mt-2">
                      <input v-model="author.office" type="text" :id="'office_' + index" :name="'office_' + index"  class="input input-bordered w-full shadow-none" placeholder="silpakorn university" :disabled="!isEditing"/>
                  </div>
              </div>
  
              <!-- ประเทศสำนักงาน -->
              <div class="sm:col-span-3">
                <label class="block text-sm font-medium leading-6 text-gray-900">ประเทศ </label>
                <div class="mt-2">
                   <select v-model="author.country" @change="loadStates(index)" :id="'country_' + index" :name="'country_' + index" class="select select-bordered w-full" :disabled="!isEditing"><!--v-model="selectedCountry" -->
                    <option value="">กรุณาเลือก</option>
                    <option v-for="country in countries" :key="country.id" :value="country.name">{{ country.name }}</option>
                  </select>
                </div>
              </div>
  
              <!-- จังหวัดสำนักงาน -->
              <div class="sm:col-span-3">
                <label class="block text-sm font-medium leading-6 text-gray-900">จังหวัด/เมือง </label>
                <div class="mt-2">
                  <select  v-model="author.province" :id="'province_' + index" :name="'province_' + index" class="select select-bordered w-full" :disabled="!isEditing">
                    <option v-if="!author.country" value="">กรุณาเลือก</option>
                    <option v-if="author.country && states[index] && states[index].length > 0" value = ''>กรุณาเลือก</option>
                    <option v-for="state in states[index]" :key="state.id" :value="state.name">{{ state.name }}</option>
                  </select>
                </div>
              </div>
            
              <!-- ไฟล์รูปภาพ -->
            <div class="sm:col-span-full">
                <label class="block text-sm font-medium leading-6 text-gray-900">อัปโหลดรูปภาพนักวิจัย</label>
                <div class="mt-2">
                  <input ref="fileInput" type="file" @change="handleImageUpload(index, $event)" :id="'pic_name_' + index" class="file-input file-input-bordered w-full max-w-xs" :disabled="!isEditing"/>
                  <div v-if="author.pic_name" class="mt-3 relative max-w-xs h-36 w-36 flex flex-col items-center">
                    <img :src="author.pic_name" alt="Author Image" class="max-w-xs h-36 w-36 rounded-md" />
                    <!-- <button @click="removeImage(index)" class="text-red-500 text-xs btn btn-xs rounded-none mt-3" :disabled="!isEditing" >ลบรูปภาพ</button> -->
                  </div>
                  <div v-if="errorImageType[index]" class="text-red-500 mt-2">
                    {{ errorImageType[index] }}
                  </div>
                </div>
              </div> 
            </div>
            
         </div>
        </div>
      </div>
      </div>
      </form>
      <br>
        <div class="mt-6 flex items-center justify-end gap-x-6">
          <button  v-if="!isEditing" @click="enableEditing"   class="text-sm font-semibold leading-6 text-gray-900 ">แก้ไข</button>
          <button type="submit" v-if="!isEditing" @click="saveChanges" class=" mr-48 rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm ">ยืนยัน</button>
          <button v-if="isEditing" @click="saveChanges" class=" mr-48 rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm ">บันทึก</button>  
        </div>
  
    </div>
    <br>
    
       
</template>

<script setup>
import {ref, onMounted , computed , watch} from 'vue'
import axios from 'axios' //ใช้เพื่อยิงไปที่ตัว api

import Papa from 'papaparse';
import { useStore } from 'vuex';
import { useRouter ,useRoute} from 'vue-router';
const route = useRoute()

const store = useStore();
const router = useRouter();
const isEditing = ref(false);
// const formData = ref({
//   abstract_url: '',
//   keyword: '',
//   abstract: '',
//   title: '',
//   publication_year: '',
//   publication_title: '',
//   article_number: '',
//   content_type: '',
//   start_page: '',
//   end_page: '',
//   doi: '',
//   publisher: '',
//   authors: []
// });

// ใช้ ref() เพื่อเก็บข้อมูล formData ที่ได้จาก Vuex store
const formData = ref(store.state.formData);
console.log(formData.value)
console.log(formData.value.authors)
formData.value.authors.forEach((author) => {
    console.log(author.province)
});
    
  
// console.log(formData.value.authors[0].country)
// console.log(formData.value.authors[0].province)
const leveldegree = ref([]);



const author_indatabase = ref(store.state.authorIndatabase);
console.log(author_indatabase.value) //อันนี้เอาไปเช็กในรายชื่อนักวิจัยที่มีอยู่ในระบบ

const isAuthorFormVisible = ref(store.state.isAddAuthorFormVisible);
console.log(isAuthorFormVisible.value)

const otherPublisherInput = ref(store.state.otherPublisherInput);
console.log(otherPublisherInput.value)

const otherExpertise = ref(store.state.otherExpertise);
console.log(otherExpertise.value)

const oldExpertise = ref(store.state.oldExpertise);
console.log(oldExpertise.value)

// const saveFormData = () => {
//   store.dispatch('saveFormData', formData.value);
//   router.push('/addsuccess');
// };

const enableEditing = () => {
    isEditing.value = true;
};

// const saveChanges = () => {
//     isEditing.value = false;

//       // ทำการบันทึกค่าที่แก้ไขลงในระบบหรือทำอย่างอื่นตามต้องการ
// };

const countries = ref([]);
const states = ref({});


const loadCountries = () => {
  Papa.parse('/countries.csv', {
    download: true,
    header: true,
    complete: (results) => {
      countries.value = results.data;
      console.log(results.data)
    }
  });
  
};

const loadStates = (index) => {
    const selectedCountry = countries.value.find(country => country.name === formData.value.authors[index].country);
    const selectedCountryId = selectedCountry ? selectedCountry.id : null;
    console.log(selectedCountry)
    console.log(selectedCountryId)
    // const selectedCountryId = formData.value.authors[index].country;
    if (selectedCountryId) {
      Papa.parse('/states.csv', {
        download: true,
        header: true,
        complete: (results) => {
          states.value[index] = results.data.filter(state => state.country_id === selectedCountryId);
          console.log(states.value[index])
        }
      });
    } else {
        states.value = '';
    }
    
  };
  
onMounted(() => {
  fetch_all_author();
  fetch_search_expertise();
  loadCountries();

  formData.value.authors.forEach((author, index) => {
    const degreeName = author.degree[0].degree_name;
    const [level, ...nameParts] = degreeName.split(' ');

    // Ensure leveldegree has a ref for each author
    if (!leveldegree.value[index]) {
      leveldegree.value[index] = ref('');
    }

    // Update leveldegree and degree_name
    leveldegree.value[index] = level;
    author.degree[0].degree_name = nameParts.join(' ');

    console.log(leveldegree.value[index]);
    console.log(author.degree[0].degree_name);
    console.log("รักเพน");
  });

  formData.value.authors.forEach((index) => {
    isOpen.value[index] = false;
  });
//   loadCountries();
    // watch(() => formData.value.authors.country, loadStates);
    formData.value.authors.forEach((author, index) => {
        watch(() => author.country, () => loadStates(index));
    });
    // formData.value.authors.forEach((author, index) => {
    //     console.log(index)
    //     loadStates(index);
    //     console.log(author.province)
    // });

// formData.value.authors.forEach((author, index) => {
//     watch(() => author.country, () => {
//       loadStates(index);
//     });
//     // Load initial states
//     loadStates(index);
//     console.log(states.value[index])
//   });
  
});



const errorImageType = ref([]);

// --------------------โหลดรูปภาพ------------------
const handleImageUpload = (index, event) => {
    const file = event.target.files[0];
    const acceptedFileTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/jpg', 'image/raw', 'image/tif', 'image/psd', 'image/webp'];

    if (!acceptedFileTypes.includes(file.type)) {
      errorImageType.value[index] = 'อัปโหลดได้เฉพาะนามสกุลไฟล์ภาพ .jpeg, .png, .gif, .jpg, .raw, .tif, .psd, .webp ';
      formData.value.authors[index].pic_name = ''; // Clear pic_name if file type is invalid
      return;
    }


    const reader = new FileReader();

    reader.onload = () => {
      
      // เมื่อไฟล์ถูกโหลดเสร็จแล้ว ให้เก็บข้อมูลในรูปแบบ base64 string ลงในตัวแปร image
      formData.value.authors[index].pic_name = reader.result;
      errorImageType.value[index] = '';
    };
     // อ่านไฟล์รูปภาพเป็น base64 string
    reader.readAsDataURL(file);
};
const removeImage = (index) => {
 try {
   const isSure = confirm("คุณแน่ใจที่จะลบรูปภาพใช่ไหม?");
   if (isSure) {
     formData.value.authors[index].pic_name = '';
     errorImageType.value[index] = '';
     resetFileInputImage(index);
   } else {
     console.log("ไม่ลบรูปภาพ");
   }
 } catch (error) {
   console.log(error);
 }
};
const fileInput = ref([]);
const resetFileInputImage = (index) => {
  if (fileInput.value[index]) {
    fileInput.value[index].value = '';
  }
};
// -------------------------author-------------------

const isOpenOff = ref((false));// ประกาศ reactive ref สำหรับเก็บสถานะการเปิดหรือปิด dropdown
const all_author = ref({}); 
// const author_indatabase = ref([]); //เก็บรายชื่อนักวิจัยที่มีอยู๋ในระบบ

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
      author_indatabase.value = author_indatabase.value.filter(author => author.full_name !== authorName);
    } else {
        // หากชื่อนักวิจัยยังไม่ถูกเลือกให้เพิ่มเข้าไปในรายการ
        author_indatabase.value.push({ full_name: authorName});
    }
    console.log(author_indatabase.value);
};

// ฟังก์ชันที่ใช้สำหรับตรวจสอบว่านักวิจัยชื่อนี้ถูกเลือกหรือไม่ ในcheckbox
const isSelectedAuthor = (authorName) => {
    return author_indatabase.value.some(author => author.full_name === authorName);
};


const dropdownButtonTextAuthor = computed(() => {
if (author_indatabase.value && author_indatabase.value.length > 0) {
  return author_indatabase.value.map(author => author.full_name).join(', ');
} else {
  return "กรุณาเลือก";
}
});



// เพิ่มนักวิจัยร่วม
// const addAuthor = () => {
//   isAddAuthorFormVisible.value = true;
//   if (!formData.value.authors) {
//     // ถ้า formData.authors ยังไม่ได้ถูกกำหนดค่าให้เป็นอาร์เรย์ ให้กำหนดค่าเริ่มต้นเป็นอาร์เรย์ว่าง
//     formData.value.authors = [];
//   }

  
//   formData.value.authors.push({
//     authorUrl: '',
//     website: '',
//     pic_name: '',
//     full_name: '',
//     name_th: '', 
//     office: '',
//     expertise: [{expertise_name: ''}],
//     country: '',
//     email: '',
//     degree: [{degree_name: ''}],
//     id: '',
//     province: ''
//   });

//   console.log(formData.value)
  
// };
// ----------------- keyword----------------
// const temporaryKeywords = ref([''])
// const addKeyword = () => {
//   temporaryKeywords.value.push('');

//   console.log(temporaryKeywords.value)
// };
// const removeKeyword = index => {
//   temporaryKeywords.value.splice(index, 1);
// };

// ------------------------degree--------------------

// เพิ่มวุฒิการศึกษา
const addDegree = (authorIndex) => {

  formData.value.authors[authorIndex].degree.push({degree_name: '' });
  console.log(formData.value)
};

const removeDegree = (authorIndex, degreeIndex) => {
    formData.value.authors[authorIndex].degree.splice(degreeIndex, 1);
};

// ----------------------------form-------------------------




async function saveChanges() {
    isEditing.value = false; 
  let hasError = false;
  errorImageType.value.forEach((error) => {
    if (error) {
      hasError = true;
      // Display error for each invalid file
      alert("กรุณาใส่ไฟล์รูปภาพให้ถูกต้อง");
      console.log("error file")
    }
  });

  if (hasError) {
    return;
  }

   // ลบช่องว่างซ้ายและขวาของข้อความทุกอย่างที่กรอกลงฟอร์ม
   for (let field in formData.value) {
      if (typeof formData.value[field] === 'string') { // เป็น string หรือไม่ โดยใช้ typeof
          formData.value[field] = formData.value[field].trim();  // เป็นตัดช่องว่างซ้ายขวา
      }
  }



    formData.value.authors.forEach((author, authorIndex) => {
      const authorLevelDegree = leveldegree.value[authorIndex] || '';
        author.degree = author.degree.map(deg => ({
          degree_name: `${authorLevelDegree} ${deg.degree_name}`.trim()
          
        }));
      console.log(formData.value.authors.degree)
    });

try {
    console.log('formData.authors:', formData.value.authors);

    const authors = formData.value.authors.map(author => ({
        authorUrl: author.authorUrl,
        website: author.website,
        pic_name: author.pic_name,
        full_name: author.full_name,
        name_th: author.name_th,
        office: author.office,
        country: author.country,
        email: author.email,
        id: author.id === '' ? null : author.id,
        province: author.province,
        expertise: author.expertise.map(exp => ({
            expertise_name: exp.expertise_name
        })),
        degree: author.degree.map(deg => ({
            degree_name: deg.degree_name
        }))
    }));

    const response = await axios.put(`${import.meta.env.VITE_FASTAPI}/edit_many_user`, authors);
    edit_author_indatabase()
    search_idresearch()

    console.log(response.data);
    
    
} catch (error) {
    console.error("เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง API:", error);
    alert("ไม่สามารถแก้ไขข้อมูลได้");
}


console.log(formData.value.title)


}

async function edit_author_indatabase()  {



formData.value.authors.forEach((author) => {
    author.full_name_object = {"full_name": author.full_name}//แปลงชื่อ string เป็น object อยู่ใน full_name

    author_indatabase.value.push(author.full_name_object);
});    

console.log(author_indatabase.value);
try { 
        const response = await axios.put(`${import.meta.env.VITE_FASTAPI}/edit_author_indatabase`, {
            authors: author_indatabase.value,
            title: formData.value.title
            
        });
        console.log(response.data);
    } catch (error) {
        console.error("เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง API:", error);
        alert("ไม่สามารถแก้ไขข้อมูลได้");
    }
};


// const otherPublisherInput = ref('')
// ฟังก์ชันที่ใช้สำหรับตรวจสอบว่านักวิจัยชื่อนี้ถูกเลือกหรือไม่ ในcheckbox
async function search_idresearch  ()  {

    const publisher = () => {
        const PublisherInput = formData.value.publisher === 'อื่นๆ' ? otherPublisherInput.value : formData.value.publisher;
        return PublisherInput
    };

    const currentPublisher = publisher();
    console.log(currentPublisher);
    try {
            const name_research = formData.value.title;

            const response_id_research = await axios.get(`${import.meta.env.VITE_FASTAPI}/query_id_research`, {
                params: {
                    name_research: name_research
                }
            });
            console.log(response_id_research.data)

            const response = await axios.put(`${import.meta.env.VITE_FASTAPI}/edit_research/${response_id_research.data}`, {
                abstract: formData.value.abstract,
                title: formData.value.title,
                publication_year: formData.value.publication_year,
                publication_title: formData.value.publication_title,
                article_number: formData.value.article_number, 
                content_type: formData.value.content_type,
                start_page: formData.value.start_page ,
                end_page: formData.value.end_page ,
                doi: formData.value.doi ,
                publisher: currentPublisher,
                abstract_url: formData.value.abstract_url,
                keyword: formData.value.keyword
            });
            // console.log(edit_research.value);
            // console.log("แก้ไขสำเร็จ");
            // alert("แก้ไขสำเร็จ");
            // console.log(store.state.searchQueryResearch);
            // store.commit('setSearchQueryResearch', store.state.searchQueryResearch);
            // console.log(store.state.searchQueryResearch);
            // router.push({ name: 'showresearch', query: { search: store.state.searchQueryResearch } });
        
            console.log(response.data);
            alert("แก้ไขสำเร็จ");
        } catch (error) {
            console.error("เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง API:", error);
            alert("ไม่สามารถแก้ไขข้อมูลได้");
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

        if(otherExpertise.value && otherExpertise.value.length > 0){
             search_expertise.value = search_expertise.value.filter(expertise => {
             return !otherExpertise.value.some(other => other.otherExpertise_name === expertise);
        })
        console.log(search_expertise.value)
      };

      } catch (error) {
        console.log(error);
      }
    };

    // ฟังก์ชันสำหรับเปิดหรือปิด dropdown
    const toggleDropdown = (authorIndex) => {
      isOpen.value[authorIndex] = !isOpen.value[authorIndex];
    };


    

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
    }// else if (expertiseName === '') {
      //   // หากชื่อสาขาว่างเปล่า ให้แสดงข้อความแจ้งเตือน
      //   alert("กรุณาเลือกชื่อสาขาที่เชี่ยวชาญ");
      // }
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
  if (formData.value.authors[index] && formData.value.authors[index].expertise &&formData.value.authors[index].expertise.length > 0) {
    // ถ้ามี ให้สร้างข้อความแสดงสาขาที่ถูกเลือก
    return formData.value.authors[index].expertise.map(exp => exp.expertise_name).join(", ");
  } else {
    // ถ้าไม่มี ให้แสดงข้อความ "เลือก"
    return "กรุณาเลือก";
  }
}

</script>