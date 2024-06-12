<template>
    <!-- <span class="box-decoration-clone bg-gradient-to-r from-indigo-600 to-pink-500 text-white px-96 py-48 ...">
                     Hello<br>
                     World
                </span> -->
    <div class="container bg-gradient-to-r from-sky-500 to-indigo-500 h-64 pt-12 text-white min-w-full  px-24 font-black flex justify-center items-center">
        <p class="text-5xl tracking-wider">กราฟแสดงความสัมพันธ์ระหว่างงานวิจัยและผู้วิจัย</p> 
    </div>
    <br>
    <div>
    <div class="nav-button  flex justify-start"   style="margin-left: 100px;">
        <button class="btn button_menu rounded-none " @click="showLoginForm" :class="{ 'active': showLogin }">ค้นหาชื่อนักวิจัย</button>
        <button class="btn button_menu rounded-none " @click="showRegisterForm" :class="{ 'active': showRegister }">ค้นหาชื่องานวิจัย</button>
        <button class="btn button_menu rounded-none " @click="showSubjectForm" :class="{ 'active': showSubject }">ค้นหาสาขาที่เชี่ยวชาญ</button>
    </div>
            <div class=" max-w-screen mx-auto">
                
                <!-- <div class="flex flex-col"> -->
                    <!-- ----------------------------นักวิจัย----------------------- -->
                    <div  v-if="showLogin" class="login-container active" id="login" ref="loginForm">
                        <div class="label col-start-1 col-end-7">
                            <span class="label-text text-lg mr-5">ชื่อนักวิจัย</span>
                        </div>
                        <br>
                        <div class="input-container relative w-full">
                            <input type="text" id="inputFieldAuthor" placeholder="ชื่อ - นามสกุล นักวิจัยเป็นภาษาอังกฤษหรือภาษาไทย"
                                class="input input-bordered w-full rounded-md text-black flex-grow" v-model="search.queryName" >
                            <!-- textInputErrorAuthor คือ true , !textInputErrorAuthorRegex คือ false -->
                            <span v-if="textInputErrorAuthor && !textInputErrorAuthorRegex"
                                class="label-text-alt text-sm text-red-500 mx-auto">กรุณากรอกชื่อ-นามสกุล
                                เป็นภาษาอังกฤษหรือภาษาไทย เฉพาะตัวอักษร (a-z, A-Z ก-๙) ตัวเลข (0-9) ช่องว่าง และอักขระ .
                                - ' เท่านั้น</span>
                            <span v-if="textInputErrorAuthorRegex"
                                class="label-text-alt text-sm text-red-500">กรุณาอย่าใส่อักขระพิเศษที่ไม่ได้ระบุ
                                ใส่ได้เฉพาะตัวอักษร (a-z, A-Z ก-๙) ตัวเลข (0-9) ช่องว่าง และอักขระ . - ' เท่านั้น</span>
                        
                            <div v-if="author_name.length > 0" class="autocomplete-results w-full " >
                                    <ul class="w-full">
                                        <li v-for="author in filteredAuthors" :key="author.id">
                                            <router-link :to="{ name: 'graph_author', params: { id: author.id }}" class="flex items-center">
                                                <img :src="searchIcon" alt="Icon Search" class="h-2 w-2" />&nbsp; &nbsp; {{author.displayName }}
                                            </router-link>
                                        </li>
                                    </ul>
                            </div>
                        </div>
                        <br>
                        <div v-if="notFoundSearch" class="flex justify-center">ไม่พบข้อมูล</div>
                        
                        <!-- <div class="indicator">
                            <button class="btn btn-warning rounded-md" v-on:click="handleSearch('author')">
                                <img :src="searchIcon" alt="Icon Search" class="h-6 w-6" />
                                ค้นหา
                            </button>
                        </div> -->
                       
                        
                    </div>

                    <!-- ----------------------------งานวิจัย----------------------- -->
                    <div v-if="showRegister" class="register-container active" id="register" ref="registerForm">
                        <div class="label col-start-1 col-end-7">
                            <span class="label-text text-lg mr-5">ชื่องานวิจัย</span>
                        </div>
                        <br>
                        <div class="input-container relative  w-full">
                            <input type="text" id="inputFieldResearch" placeholder="ชื่องานวิจัย"
                                class="input input-bordered w-full rounded-md text-black flex-grow" v-model="search.queryResearch" >
                            <span v-if="textInputErrorResearch && !textInputErrorResearchRegex"
                                class="label-text-alt text-sm text-red-500 mx-auto">กรุณากรอกชื่องานวิจัย เฉพาะตัวอักษร (a-z,
                                A-Z ก-๙) ตัวเลข (0-9) ช่องว่าง และอักขระ . - : () เท่านั้น</span>
                            <span v-else-if="textInputErrorResearchRegex"
                                class="label-text-alt text-sm text-red-500">กรุณาอย่าใส่อักขระพิเศษที่ไม่ได้ระบุ
                                ใส่ได้เฉพาะตัวอักษร (a-z, A-Z ก-๙) ตัวเลข (0-9) ช่องว่าง และอักขระ . - : ()
                                เท่านั้น</span>
                            
                            <div v-if="research_name.length > 0" class="autocomplete-results w-full">
                                <ul class="w-full">
                                    <li v-for="research in research_name" :key="research.id">
                                        <router-link :to="{ name: 'graph_research', params: { id: research.id} }" class="flex items-center">
                                            <img :src="searchIcon" alt="Icon Search" class="h-2 w-2" />&nbsp;&nbsp; {{research.n.title }}
                                        </router-link>
                                    </li>
                                </ul>
                            </div>    
                        </div>
                        <br>

                        
                        <div v-if="notFoundSearch" class="flex justify-center">ไม่พบข้อมูล</div>

                        <!-- แสดงผลลัพธ์การค้นหา -->
                        
                        <!-- <div class="indicator">
                            <button class="btn btn-warning rounded-md" v-on:click="handleSearch('research')">
                                <img :src="searchIcon" alt="Icon Search" class="h-6 w-6" />
                                ค้นหา
                            </button>
                        </div> -->
                    </div>
                    <!-- ----------------------------สาขาที่เชี่ยวชาญ----------------------- -->
                    <div v-if="showSubject" class="subject-container active" id="subject" ref="subjectForm">
                        <div class="label col-start-1 col-end-7 ">
                            <span class="label-text text-lg mr-5">สาขาที่เชี่ยวชาญ</span>
                        </div>
                        <br>
                        <div class="flex justify-center">
                            <div class="w-full mr-5">
                                <select id="selectExpertise" v-model="selected"
                                    class="select select-bordered w-full rounded-md text-black flex-grow" @change="onExpertiseChange"
                                    placeholder="เลือก">
                                    <option v-if="!selected" disabled selected value="">กรุณาเลือก</option>
                                    <option v-for="expertise in search_expertise" :key="expertise.id"
                                        :value="expertise.id">
                                        {{ expertise.n.expertise_name }}
                                    </option>
                                </select>
                                <span v-if="textInputErrorExpertise"
                                    class="label-text-alt text-sm text-red-500">กรุณาเลือกข้อมูลสาขาที่เชี่ยวชาญ</span>
                            </div>
                            <br>
                            <div class="indicator">
                                <router-link v-if="selected"
                                    :to="{ name: 'graph_expertise', params: { id: selected } }">
                                    <button class="btn btn-warning rounded-md">
                                        <div class="flex justify-center px-1">
                                            <img :src="searchIcon" alt="Icon Search" class="h-4 w-4 mr-2" />
                                            ค้นหา
                                        </div>
                                        </button>
                                </router-link>
                                <button v-else v-on:click="showErrorExpertise" class="btn btn-warning rounded-md">
                                    <img :src="searchIcon" alt="Icon Search" class="h-4 w-4" />
                                    ค้นหา
                                </button>
                            </div> 
                        </div>
                    </div>
                <!-- </div> -->
            </div>
        </div>
</template>

<script setup>
import { ref, onMounted ,watch , computed} from "vue";
import axios from "axios"; //ใช้เพื่อยิงไปที่ตัว api
import router from "../../router";
import { useStore } from "vuex";
import searchIcon from "@/assets/icon/search-icon.png";

const store = useStore(); // เรียกใช้ store
const selected = ref(""); //เพื่อเก็บค่าที่ถูกเลือกจาก dropdown
const author_name = ref({});
const research_name = ref({});
const search_expertise = ref({});
let inputErrorResearch = false;
let inputErrorAuthor = false;
const textInputErrorResearch = ref(false); // ใช้ ref เพราะต้องเชื่อมโยงกับการแสดงผลใน DOM
const textInputErrorResearchRegex = ref(false);
const textInputErrorAuthor = ref(false);
const textInputErrorAuthorRegex = ref(false);
const textInputErrorExpertise = ref(false);
const notFoundSearch = ref(false);

const search = ref({
    queryName: "",
    queryResearch: "",
});
const showLogin = ref(true);
const showRegister = ref(false);
const showSubject = ref(false);

const filteredAuthors = computed(() => {
      const isThai = /[\u0E00-\u0E7F]/.test(search.value.queryName); //ไทย = true
      return author_name.value.map(author => ({
        ...author,
        displayName: isThai ? author.n.name_th : author.n.full_name
      }));
      
});

const handleSearch = (buttonType) => {
    var inputFieldResearchs = document.getElementById("inputFieldResearch");
    var inputFieldAuthors = document.getElementById("inputFieldAuthor");
    const regexAuthor = /^[a-zA-Z0-9\s-.ก-๙']+$/;// กำหนด Regex เพื่อตรวจสอบอักขระที่ยอมรับ (ตัวอักษรอังกฤษ ไทย ตัวเลข ช่องว่างและอักขระ .-')
    const regexResearch = /^[a-zA-Z0-9\s-.ก-๙:()]+$/;// กำหนด Regex เพื่อตรวจสอบอักขระที่ยอมรับ (ตัวอักษรอังกฤษ ไทย ตัวเลข ช่องว่างและอักขระ .-')
    if (search.value.queryName.trim() !== "" && buttonType === 'author') {
        // เริ่มต้นด้วยเงื่อนไขว่า queryName ไม่เป็นช่องว่าง  

        if (!regexAuthor.test(search.value.queryName.trim())) { //เป็น true เมื่อ search.value.queryName.trim() ไม่ตรงกับเงื่อนไขของ Regex และ false เมื่อตรงกันตามเงื่อนไข
            // ถ้ามีอักขระพิเศษ
            textInputErrorAuthorRegex.value = true; //ระบุข้อความ error อักขระ
            inputFieldAuthors.classList.add('input-error');
            console.log("Please do not enter special characters");

        } else {
            try {
                fetch_search_author(search.value.queryName);
                inputFieldAuthors.classList.remove('input-error');
                inputErrorAuthor = false;
                textInputErrorAuthor.value = false;
                textInputErrorAuthorRegex.value = false;
                // router.push({ name: "listauthorname" });

            } catch (error) {
                console.error("Error:", error);
            }
        }
    } else if (search.value.queryResearch.trim() !== "" && buttonType === 'research') {
        if (!regexResearch.test(search.value.queryResearch.trim())) {
            textInputErrorResearchRegex.value = true;
            inputFieldResearchs.classList.add('input-error');
            console.log("Please do not enter special characters");
        } else {
            try {
                fetch_search_research(search.value.queryResearch);
                inputFieldResearchs.classList.remove('input-error');
                inputErrorResearch = false;
                textInputErrorResearch.value = false;
                textInputErrorResearchRegex.value = false;
                // router.push({ name: "listresearchname" });
            } catch (error) {
                console.error("Error:", error);
            }
        }
    // } else {
    //     console.log("Please enter a valid data");
    //     if (buttonType === 'author') {
    //         inputErrorAuthor = true;
    //         textInputErrorAuthor.value = true; // ระบุข้อความ error
    //         textInputErrorAuthorRegex.value = false;
    //         if (inputErrorAuthor) {
    //             inputFieldAuthors.classList.add('input-error'); //ใส่border สีแดง
    //         } else {
    //             inputFieldAuthors.classList.remove('input-error');
    //         }
    //     } else if (buttonType === 'research') {
    //         inputErrorResearch = true;
    //         textInputErrorResearch.value = true;
    //         textInputErrorResearchRegex.value = false;
    //         if (inputErrorResearch) {
    //             inputFieldResearchs.classList.add('input-error');
    //         } else {
    //             inputFieldResearchs.classList.remove('input-error');
    //         }
    //     }
    }
};

const fetch_search_author = async (queryName) => {
    await axios
        .get(`${import.meta.env.VITE_FASTAPI}/search_author/${queryName}`, {
            withCredentials: true,
        })
        .then((response) => {
            author_name.value = response.data;
            notFoundSearch.value = false;
            // store.commit("setAuthorName", author_name.value); // เรียกใช้ mutation เพื่อเปลี่ยนแปลง state
            console.log(author_name.value);
        })
        .catch((error) => {
            notFoundSearch.value = true;
            author_name.value = '';
            
            // store.commit("setAuthorName", author_name.value);
            console.log(error);
        });
};
const fetch_search_research = async (queryResearch) => {
    await axios
        .get(`${import.meta.env.VITE_FASTAPI}/search_research/${queryResearch}`, {
            withCredentials: true,
        })
        .then((response) => {
            research_name.value = response.data;
            notFoundSearch.value = false;
            // store.commit("setResearchName", research_name.value);
            console.log(research_name.value);
        })
        .catch((error) => {
            notFoundSearch.value = true;
            research_name.value = '';
            
            // store.commit("setResearchName", research_name.value);
            console.log(error);
        });
};

watch(() => search.value.queryName, (newQueryName) => {
    if (newQueryName.trim() !== "") {
        fetch_search_author(newQueryName);
        // handleSearch('author');
    }else {
        author_name.value = ''; // Clear the results if the input is empty
        
    }
});

watch(() => search.value.queryResearch, (newQueryResearch) => {
    if (newQueryResearch.trim() !== "") {
        // handleSearch('research');
        fetch_search_research(newQueryResearch);
    }
    else{
        research_name.value = '';
    }
});
const fetch_search_expertise = async () => {
    await axios
        .get(`${import.meta.env.VITE_FASTAPI}/search_expertise`, {
            withCredentials: true,
        })
        .then((response) => {
            search_expertise.value = response.data;
            console.log(search_expertise.value);
        })
        .catch((error) => {
            console.log(error);
        });
};

const showErrorExpertise = () => {
    var selectExpertises = document.getElementById("selectExpertise");

    if (selected) { // null
        textInputErrorExpertise.value = true;
        selectExpertises.classList.add('select-error');
    } else {
        textInputErrorExpertise.value = false;
        selectExpertises.classList.remove('select-error');
    }
};

// const onExpertiseChange = () => {
//     console.log(selected.value);
// };


// ฟังก์ชันแสดงฟอร์ม login
const showLoginForm = () => {
      showLogin.value = true;
      showRegister.value = false;
      showSubject.value = false;
    };

    // ฟังก์ชันแสดงฟอร์ม register
    const showRegisterForm = () => {
      showLogin.value = false;
      showRegister.value = true;
      showSubject.value = false;
    };

    // ฟังก์ชันแสดงฟอร์ม subject
    const showSubjectForm = () => {
      showLogin.value = false;
      showRegister.value = false;
      showSubject.value = true;
    };

onMounted(() => {
    fetch_search_expertise();
});
</script>

<style>

.active {
    /* position: relative; */
    background-color: rgba(237, 237, 237, 0.901);
    border: black;
    /* display: flex;
    flex-direction: column; */
    width: auto;
    height: auto;
}

/* .btn-login.active {
    background-color: rgba(237, 237, 237, 0.808);
    border: black;
    width: auto;
    height: auto;
}

.btn-register.active {
    background-color: rgba(237, 237, 237, 0.721);
    border: black;
    width: auto;
    height: auto;
}

.btn-subject.active {
    background-color: rgba(237, 237, 237, 0.503);
    border: black;
    width: auto;
    height: auto;
} */


.button_menu.active {
    background-color: rgba(237, 237, 237, 0.901);
    color: blue;
    font-size: 18px;
}

.button_menu:not(.active) {
    background-color: white;
    color: black; 
    font-size: 18px;
}

.login-container.active,
.register-container.active,
.subject-container.active {
    flex-grow: 1;
    margin-right: 100px;
    margin-left: 100px;

    padding-left: 150px;
    padding-right: 150px;

    padding-top: 80px;
    padding-bottom: 80px;
    border: black;
    display: flex;
    flex-direction: column;
    position: relative;

    /* box-sizing: border-box; ป้องกันการเพิ่มขนาดของฟอร์ม */
}
.text-5xl {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* เพิ่มเอฟเฟ็กต์เงา */
  -webkit-text-stroke-width: 1px; /* เพิ่มเส้นขอบ */
  -webkit-text-stroke-color: white; /* สีขอบ */
}

.input {
    padding: 10px;
    font-size: 16px;
    border: 1px solid #dfe1e5;
    border-radius: 24px;
    outline: none;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.2s ease-in-out;
}

.input:focus {
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

/* สไตล์ของรายการผลลัพธ์ */
.autocomplete-results {
    background-color: white;
    border: 1px solid #dfe1e5;
    border-top: none;
    max-height: 300px;
    overflow-y: auto;
    box-shadow: 0 4px 6px rgba(32, 33, 36, 0.28);
    z-index: 1000;
    border-radius: 0 0 24px 24px;
}

.autocomplete-results ul {
    list-style-type: none;
    padding: 0;
    flex: 1;
    list-style-type: none;
}



.autocomplete-results li {
    padding: 10px 20px;
    cursor: pointer;
    font-size: 16px;
    color: #202124;
}

.autocomplete-results li:hover {
    background-color: #f1f3f4;
}

/* สไตล์ของข้อความข้อผิดพลาด */
.label-text-alt {
    display: block;
    margin-top: 5px;
}

.input-error {
    border-color: #d93025;
    box-shadow: none;
}

</style>
