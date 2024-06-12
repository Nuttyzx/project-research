
<template>
  <br><br>
  <div class="max-w-4xl mx-auto mt-12 pb-18 p-6 bg-white rounded-md shadow-md">
  <form class="flex items-center justify-center" @submit.prevent="submitForm">
    <div class="space-y-12 ">
      <div >
        <h2 class="text-xl text-center leading-7 text-gray-900">แก้ไขข้อมูลนักวิจัย</h2>

     <!-- ----------------------------------แบบฟอร์มแก้ไขข้อมูลนักวิจัย------------------------- -->
    
      <div v-if="edit_user.n" class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
          <!-- ชื่อ-นามสกุล (ภาษาอังกฤษ) -->
          <div class="sm:col-span-3">
              <label class="block text-sm font-medium leading-6 text-gray-900">ชื่อ-นามสกุล (ภาษาอังกฤษ)</label>
              <div class="mt-2">
                  <input v-model="edit_user.n.full_name" type="text" class="input input-bordered w-full shadow-none" placeholder="ชื่อ-นามสกุล ภาษาอังกฤษ" />
              </div>
          </div>
          <!-- ชื่อ-นามสกุล (ภาษาไทย) -->
          <div class="sm:col-span-3">
              <label class="block text-sm font-medium leading-6 text-gray-900">ชื่อ-นามสกุล (ภาษาไทย)</label>
              <div class="mt-2">
                  <input  v-model="edit_user.n.name_th" type="text"  class="input input-bordered w-full shadow-none" placeholder="ชื่อ-นามสกุล ภาษาไทย" />
              </div>
          </div>

          <!-- หมายเลขนักวิจัย -->
          <div class="sm:col-span-4">
              <label class="block text-sm font-medium leading-6 text-gray-900">หมายเลขนักวิจัย</label>
              <div class="mt-2">
                  <input  v-model="edit_user.n.id" type="number" class="input input-bordered w-full shadow-none" placeholder="หมายเลขนักวิจัย" />
              </div>
          </div>

          <!-- วุฒิการศึกษา -->
          <div class="sm:col-span-3 ">
                    <label class="block text-sm font-medium leading-6 text-gray-900">วุฒิการศึกษาสูงสุด</label>
                    <div class="flex items-center">
                    <div class="sm:col-span-1">
                        <div class="mt-2 mr-3">
                        <select v-model="leveldegree"  id="leveldegree" name="leveldegree" class="select select-bordered w-full " >
                            <option value="">กรุณาเลือก</option>
                            <option value="ปริญญาเอก">ปริญญาเอก</option>
                            <option value="ปริญญาโท">ปริญญาโท</option>
                            <option value="ปริญญาตรี">ปริญญาตรี</option>
                        </select>
                        </div>
                    </div>
                    <div class="mt-7" >
                        <input v-model="edit_user.degree[0].degree_name" type="text" :id="edit_user.id_degree"  class="input input-bordered w-full shadow-none mr-5 mb-5" placeholder="สาขา" />
                    </div>
                </div>
                </div>          

         <!-- <div class="sm:col-span-full">
              <label class="block text-sm font-medium leading-6 text-gray-900">วุฒิการศึกษา</label>
              <div class="mt-2" v-for="(degree, degreeIndex) in edit_user.degree" :key="degreeIndex" style="display: flex; align-items: center;">
                  <input v-model="degree.degree_name" type="text" :id="'degree.degree_name_' +  degreeIndex" :autocomplete="'degree.degree_name_' +  degreeIndex" class="input input-bordered w-full shadow-none mr-5 mb-5"  placeholder="ช่องละ 1 วุฒิการศึกษา" />
                  <button @click="removeDegree(degreeIndex)" style="color: red; text-decoration: underline;">ลบ</button>
              </div>
              <div>
                  <button @click="addDegree()" class="btn btn-warning btn-sm rounded-md">เพิ่มวุฒิการศึกษา</button>
              </div>
          </div>  -->
          <!-- สาขาที่เชี่ยวชาญ -->

          <div class="sm:col-span-full">
            <div class="relative">
              <label class="block text-sm font-medium leading-6 text-gray-900">สาขาที่เชี่ยวชาญ</label>
              <button @click="toggleDropdown()" class="select select-bordered w-full text-black flex-grow bg-white relative z-10 items-center">
                {{ dropdownButtonText() }}
              </button>

              <div v-if="!isOpen" class="absolute inset-x-0 mt-1 py-1 px-2 bg-white text-black rounded shadow-lg z-20">
                <label v-for="expertise in search_expertise" :key="expertise.id" class="flex items-center cursor-pointer">
                  <input  type="checkbox" :value="expertise.id" :checked="isSelected(expertise.n.expertise_name)" class="form-checkbox rounded" @change="handleExpertiseSelection(expertise.n.expertise_name)">
                  <span class="ml-2 text-black">{{ expertise.n.expertise_name }}</span>
                </label>
              </div>
            </div>
          </div>

          <div class="sm:col-span-full">
              <label class="text-sm font-medium  text-gray-900">อื่นๆ &nbsp;&nbsp; ระบุสาขาที่เชี่ยวชาญ: </label>
              <!-- <div v-for="(expertise, expertiseIndex) in author.expertise" :key="expertiseIndex">
                  <input  v-model="expertise.expertise_name" type="text" :id="'expertise.expertise_name_' + index" :name="'expertise.expertise_name_' + index+ '_' + expertiseIndex" class="input input-bordered w-98 ml-2" placeholder="สาขาที่เชี่ยวชาญ"/>
              </div> -->
              <div>
                <div v-for="(other, otherIndex) in otherExpertise" :key="`other-${otherIndex}`">
                  <input v-model="other.otherExpertise_name" type="text" :id="'otherExpertise_name_' +  otherIndex" :name="'otherExpertise_name_' +  otherIndex" class="input input-bordered w-98 ml-2 mt-2" placeholder="สาขาที่เชี่ยวชาญอื่นๆ"/>
                </div>

                <div class="mt-3 ml-2">
                    <button @click="addOtherExpertise()" class="btn btn-warning btn-sm rounded-md">เพิ่มสาขาที่เชี่ยวชาญ</button>
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
                  <input v-model="edit_user.n.email" type="email" class="input input-bordered w-full shadow-none" placeholder="example@gmail.com" required/>
              </div>
          </div>

          <!-- authorUrl -->
          <div class="sm:col-span-full">
                <label for="authorUrl" class="block text-sm font-medium leading-6 text-gray-900">IEEE URL</label>
                <div class="mt-2">
                    <input v-model="edit_user.n.authorUrl" type="authorUrl" class="input input-bordered w-full shadow-none" placeholder="https://ieeexplore.ieee.org/author/" />
                </div>
            </div>
            <!-- website -->
            <div class="sm:col-span-full">
                <label for="website" class="block text-sm font-medium leading-6 text-gray-900">เว็บไซต์</label>
                <div class="mt-2">
                    <input v-model="edit_user.n.website" type="website"  class="input input-bordered w-full shadow-none" placeholder="https://www.example.com/" />
                </div>
            </div>

          <p class="mt-1 text-sm leading-6 text-gray-600">ที่อยู่สำนักงาน</p>
          <!-- ชื่อสำนักงาน -->
          <div class="col-span-full">
              <label class="block text-sm font-medium leading-6 text-gray-900">ชื่อสำนักงาน</label>
              <div class="mt-2">
                  <input v-model="edit_user.n.office" type="text"  class="input input-bordered w-full shadow-none" placeholder="silpakorn university"/>
              </div>
          </div>
          <!-- จังหวัดสำนักงาน
          <div class="sm:col-span-3">
              <label class="block text-sm font-medium leading-6 text-gray-900">จังหวัด</label>
              <div class="mt-2">
                  <input  v-model="edit_user.n.province" type="text"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
          </div>
          ประเทศสำนักงาน
          <div class="sm:col-span-3">
              <label class="block text-sm font-medium leading-6 text-gray-900">ประเทศ</label>
              <div class="mt-2">
                  <input v-model="edit_user.n.country"  type="text"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
          </div> -->

           <!-- ประเทศสำนักงาน -->
           <div class="sm:col-span-3">
              <label class="block text-sm font-medium leading-6 text-gray-900">ประเทศ</label>
              <div class="mt-2">
                 <select v-model="edit_user.n.country" @change="loadStates()" id="country" name="country" class="select select-bordered w-full"><!--v-model="selectedCountry" -->
                  <option value="">กรุณาเลือก</option>
                  <option v-for="country in countries" :key="country.id" :value="country.name">{{ country.name }}</option>
                </select>
              </div>
            </div>

            <!-- จังหวัดสำนักงาน -->
            <div class="sm:col-span-3">
              <label class="block text-sm font-medium leading-6 text-gray-900">จังหวัด/เมือง</label>
              <div class="mt-2">
                <select  v-model="edit_user.n.province" id="province" name="province" class="select select-bordered w-full">
                  <option v-if="!edit_user.n.country" value="">กรุณาเลือก</option>
                  <option v-if="edit_user.n.country&&states && states.length > 0" value="">กรุณาเลือก</option>
                  <option v-for="state in states" :key="state.id" :value="state.name">{{ state.name }}</option>
                </select>
              </div>
            </div>

            <!-- ไฟล์รูปภาพ -->
        
            <div class="sm:col-span-full">
              <label class="block text-sm font-medium leading-6 text-gray-900">อัปโหลดรูปภาพนักวิจัย</label>
              <div class="mt-2 relative">
                <!-- หากไม่มีรูปภาพ -->
                <div v-if="!edit_user.n.pic_name">
                  <input type="file" @change="handleImageUpload($event)" id="pic_name" class="file-input file-input-bordered w-full max-w-xs"/>
                  <div v-if="errorImageType" class="text-red-500 mt-2">
                    {{errorImageType}}
                  </div>
                </div>
                <!-- หากมีรูปภาพแล้ว -->
                <div v-else>
                  <img :src="edit_user.n.pic_name" alt="Author Image" class="max-w-xs h-36 w-36 rounded-md mt-5" />
                  <div class="flex items-center mt-2" >
                    <button @click="InputUploadImage" class="text-gray-500 text-xs btn btn-xs rounded-none mr-2 mb-2">แก้ไขรูปภาพ</button><!--hover:text-indigo-500 -->
                    <button @click="removeImage" class="text-red-500 text-xs btn btn-xs rounded-none mb-2">ลบรูปภาพ</button>
                    <input ref="imageUpload" type="file" @change="handleImageUpload($event)" id="image" class="file-input file-input-bordered file-input-primary hidden"/>
                    <!-- <span v-if="edit_user.n.pic_name" class="text-gray-500 text-xs mt-3" >{{fileName}}</span>          -->
                  </div>
                  <span v-if="edit_user.n.pic_name" class="text-gray-500 text-xs" >{{fileName}}</span>         
                  <div v-if="errorImageType" class="text-red-500 mt-2">
                      {{errorImageType}}
                  </div>
                  <!-- ref = อ้างอิงไปยัง input -->
                </div>

              </div>
            </div>





      </div>
      
    </div>
  </div>
    

  </form>
  <br>
    <div class="mt-6 flex items-center justify-end gap-x-6">
        <button type="button" @click="cancelForm"   class="text-sm font-semibold leading-6 text-gray-900">ยกเลิก</button>
        <button type="submit" @click="editFormUser" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">บันทึก</button>
    </div>
  </div>

   
  <br>
</template>

  
<script setup>
import {ref, onMounted , watch , computed} from 'vue'
import axios from 'axios' //ใช้เพื่อยิงไปที่ตัว api
import routers from '../../router'

import Papa from 'papaparse';
import {useRouter,useRoute} from 'vue-router'
const route = useRoute()// ใช้ useRoute สำหรับการเข้าถึงพารามิเตอร์ของเส้นทางปัจจุบัน
const router = useRouter(); // ใช้ useRouter สำหรับการนำทาง

import { useStore } from 'vuex';
const store = useStore();

const edit_user = ref({
    authorUrl: '',
    website: '',
    pic_name: '',
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
console.log(route.params.id)


const countries = ref([]);
  const states = ref('');
 

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

  const loadStates = () => {
    const selectedCountry = countries.value.find(country => country.name === edit_user.value.n.country);
    const selectedCountryId = selectedCountry ? selectedCountry.id : null;
    console.log(selectedCountry)
    console.log(selectedCountryId)
    // const selectedCountryId = formData.value.authors[index].country;
    if (selectedCountryId) {
      Papa.parse('/states.csv', {
        download: true,
        header: true,
        complete: (results) => {
          states.value = results.data.filter(state => state.country_id === selectedCountryId);
          console.log(states.value)
        }
      });
    } else {
        states.value = '';
    }
    
  };
  
  const fileName = ref('');
  const errorImageType = ref('');

  // -------------อัปโหลดไฟล์รูป---------------
  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    const acceptedFileTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/jpg', 'image/raw', 'image/tif', 'image/psd', 'image/webp'];

    if (!acceptedFileTypes.includes(file.type)) {
      errorImageType.value = 'อัปโหลดได้เฉพาะนามสกุลไฟล์ภาพ เช่น .jpeg, .png, .gif, .jpg, .raw, .tif, .psd, .webp';
      edit_user.value.n.pic_name = '';
      return;
    }
    const reader = new FileReader();

    reader.onload = () => {
      edit_user.value.n.pic_name = reader.result;
      errorImageType.value = '';
    };
    fileName.value = file.name; // ตั้งค่าชื่อไฟล์ให้แสดง
    // อ่านไฟล์ภาพ
    reader.readAsDataURL(file);

    // // ตรวจสอบว่ามีการอัปโหลดรูปภาพหรือไม่
    // isImageUploaded.value = true;
  };
  const imageUpload = ref(null);
  const InputUploadImage = () => {
      imageUpload.value.click();
  };

  const removeImage = () => {
   
    try {
      const isSure = confirm("คุณแน่ใจที่จะลบรูปภาพใช่ไหม?");
      if (isSure) {
        edit_user.value.n.pic_name = '';
        fileName.value = '';
        errorImageType.value = '';
      } else {
        console.log("ไม่ลบรูปภาพ");
      }
    } catch (error) {
      console.log(error);
    }
  };
// -------------------------author-------------------


const fetch_single_user = async () => {
    await axios
        .get(`${import.meta.env.VITE_FASTAPI}/single_user/${route.params.id}`, {
            withCredentials: true,
        })
        .then((response) => {
          edit_user.value = response.data[0];
          console.log("นักวิจัยร่วม")
          console.log(edit_user.value);
          
           // ตรวจสอบว่ามีข้อมูลใน degree และไม่ว่างเปล่า
          if (edit_user.value.degree.length > 0) {
            console.log("รักเพน");
            console.log(edit_user.value.degree);
            const degreeName = edit_user.value.degree[0].degree_name;
            console.log(degreeName);
            const [level, ...nameParts] = degreeName.split(' ');

            // Update leveldegree and degree_name
            leveldegree.value = level;
            edit_user.value.degree[0].degree_name = nameParts.join(' ');

            console.log(leveldegree.value);
            
          } else {
            console.log("ไม่มีข้อมูลวุฒิการศึกษา");
          }
            })
        .catch((error) => {
            console.error("เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง API:", error);

  });
}

  // ------------------------degree--------------------
  
  // เพิ่มวุฒิการศึกษา
  const addDegree = () => {
  
  edit_user.value.degree.push({degree_name: '' });
  console.log(edit_user.value)
};

const removeDegree = (degreeIndex) => {
  edit_user.value.degree.splice(degreeIndex, 1);
  console.log(edit_user.value)
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
    const toggleDropdown = () => {
      isOpen.value = !isOpen.value;
    };

    const otherExpertise = ref([[]]); 

    const addOtherExpertise = () => {
      if (!otherExpertise.value) {
        otherExpertise.value = '';  
      }
      otherExpertise.value.push({ otherExpertise_name: '' }); // Add new expertise
      console.log(otherExpertise.value);
    };


    const leveldegree = ref('');
    onMounted(() => {
      fetch_search_expertise();
      fetch_single_user();
    
      
      

      loadCountries();
      console.log(store.state.searchQueryAuthor)
      watch(() => edit_user.value.country, loadStates);
      
  
    });
   


// เมื่อเลือกตัวเลือกสาขาที่เชี่ยวชาญ
const handleExpertiseSelection = (expertiseName) => { //expertiseId, 
    // ตัดช่องว่างซ้ายขวาก่อนเพิ่มสาขาที่เชี่ยวชาญ
    expertiseName = expertiseName.trim();
    // ตรวจสอบว่าสาขาที่เชี่ยวชาญนี้มีอยู่ในอาร์เรย์ expertise หรือไม่
    const expertiseIndex = edit_user.value.expertise.findIndex(exp => exp.expertise_name === expertiseName);
    if (expertiseIndex === -1 && expertiseName !== '') {
        // หากไม่พบสาขาที่เชี่ยวชาญนี้ในอาร์เรย์ expertise ให้เพิ่มลงไป
        edit_user.value.expertise.push({ expertise_name: expertiseName });
        console.log(edit_user.value)
      }// else if (expertiseName === '') {
      //   // หากชื่อสาขาว่างเปล่า ให้แสดงข้อความแจ้งเตือน
      //   alert("กรุณากรอกชื่อสาขาที่เชี่ยวชาญ");
      // }
      else {
        // หากพบสาขาที่เชี่ยวชาญนี้ในอาร์เรย์ expertise ให้ลบออก
        edit_user.value.expertise.splice(expertiseIndex, 1);
        console.log(edit_user.value)
    }
    // กรองค่าที่เป็นค่าว่างออกจากอาร์เรย์ expertise
    edit_user.value.expertise = edit_user.value.expertise.filter(exp => exp.expertise_name !== '');
};

// ฟังก์ชันเช็คสถานะของ checkbox ว่าถูกเลือกหรือไม่
const isSelected = (expertiseName) => {
    return edit_user.value.expertise.some(exp => exp.expertise_name === expertiseName);
};


// แก้ไขฟังก์ชัน dropdownButtonText เพื่อให้ทำงานกับ Vue.js โดยใช้ function declaration
function dropdownButtonText() {
  // ตรวจสอบว่ามีสาขาที่ถูกเลือกไว้หรือไม่
  if (edit_user.value && edit_user.value.expertise.length > 0) {
    // ถ้ามี ให้สร้างข้อความแสดงสาขาที่ถูกเลือก
    return edit_user.value.expertise.map(exp => exp.expertise_name).join(", ");
  } else {
    // ถ้าไม่มี ให้แสดงข้อความ "เลือก"
    return "กรุณาเลือก";
  }
}


async function editFormUser() {
    let hasError = false;
     
      if (errorImageType.value && errorImageType.value !== null) {
          hasError = true;
          // Display error for each invalid file
          alert("กรุณาใส่ไฟล์รูปภาพให้ถูกต้อง");
          console.log("error file")
      }
     

    if (hasError) {
      return;
    }

     // ลบช่องว่างซ้ายและขวาของข้อความทุกอย่างที่กรอกลงฟอร์ม
     for (let field in edit_user.value) {
        if (typeof edit_user.value[field] === 'string'|| typeof edit_user.value[field] === 'int') { // เป็น string หรือไม่ โดยใช้ typeof
            edit_user.value[field] = edit_user.value[field].trim();  // เป็นตัดช่องว่างซ้ายขวา
        }
     }

     if (edit_user.value.degree.length > 0) {
        const updatedDegreeName = `${leveldegree.value} ${edit_user.value.degree[0].degree_name}`.trim();
        edit_user.value.degree[0].degree_name = updatedDegreeName;
      } else {
        console.log("ไม่มีข้อมูลวุฒิการศึกษา");
      }

    otherExpertise.value.forEach((other) => {
    if (other.otherExpertise_name) {
      edit_user.value.expertise.push({ expertise_name: other.otherExpertise_name });
    }
  });

    try {
        const response = await axios.put(`${import.meta.env.VITE_FASTAPI}/edit_user/${route.params.id}`, {
            authorUrl: edit_user.value.n.authorUrl,
            website: edit_user.value.n.website,
            pic_name: edit_user.value.n.pic_name,
            full_name: edit_user.value.n.full_name,
            name_th: edit_user.value.n.name_th,
            office: edit_user.value.n.office,
            expertise: edit_user.value.expertise.map(exp => {
              return {
                expertise_name: exp.expertise_name
              };
            }),
            country: edit_user.value.n.country,
            email: edit_user.value.n.email,
            degree: edit_user.value.degree.map(deg => {
              return {
                degree_name: deg.degree_name
              };
            }),
            id: edit_user.value.n.id === '' ? null : edit_user.value.n.id,
            province: edit_user.value.n.province
        });
        console.log(edit_user.value);
        alert("แก้ไขสำเร็จ");
        // ตั้งค่าการค้นหาใน store
        console.log(store.state.searchQueryAuthor);
        store.commit('setSearchQueryAuthor', store.state.searchQueryAuthor);
        console.log(store.state.searchQueryAuthor);
        router.push({ name: 'showuser', query: { search: store.state.searchQueryAuthor } });
        console.log(response.data);
        
    } catch (error) {
        console.error("เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง API:", error);
        alert("ไม่สามารถแก้ไขข้อมูลได้");
    }
}
const cancelForm = () => {
  try {
    const isSure = confirm("คุณแน่ใจที่จะยกเลิกใช่ไหม?");
    if (isSure) {
      router.push("/showuser");
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