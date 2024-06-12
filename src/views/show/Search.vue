<template>

    <div class="hero image-background">
        <div class="hero-overlay bg-opacity-60"></div>
        <div class="hero-content text-left text-neutral-content">
            <div class="max-w-screen">
                <h1 class="mb-5 text-4xl font-bold">คุณต้องการค้นหาข้อมูลอะไร ?</h1>
                <div class="grid grid-cols-2">
                    <div class="grid grid-cols-2 rol-2 bg-black bg-opacity-50" style="margin: 20px; padding: 20px;">
                        <div class="label col-start-1 col-end-7">
                            <span class="label-text text-lg text-white">ค้นหาชื่อนักวิจัย</span>
                        </div>
                        <div class="input-container">
                            <input type="text" id="inputFieldAuthor" placeholder="ชื่อ - นามสกุล ของนักวิจัย"
                                class="input input-bordered w-full rounded-none text-black" v-model="search.queryName" />
                            <!-- textInputErrorAuthor คือ true , !textInputErrorAuthorRegex คือ false -->
                            <span v-if="textInputErrorAuthor && !textInputErrorAuthorRegex"
                                class="label-text-alt text-sm text-red-500">กรุณากรอกชื่อ-นามสกุล
                                เป็นภาษาอังกฤษหรือภาษาไทย เฉพาะตัวอักษร (a-z, A-Z ก-๙) ตัวเลข (0-9) ช่องว่าง และอักขระ .
                                - ' เท่านั้น</span>
                            <span v-if="textInputErrorAuthorRegex"
                                class="label-text-alt text-sm text-red-500">กรุณาอย่าใส่อักขระพิเศษที่ไม่ได้ระบุ
                                ใส่ได้เฉพาะตัวอักษร (a-z, A-Z ก-๙) ตัวเลข (0-9) ช่องว่าง และอักขระ . - ' เท่านั้น</span>
                        </div>
                        <div class="indicator ml-auto">
                            <button class="btn btn-warning rounded-none" v-on:click="handleSearch('author')">
                                <img :src="searchIcon" alt="Icon Search" class="h-6 w-6" />
                                ค้นหา
                            </button>
                        </div>
                    </div>

                    <div class="grid grid-cols-2 rol-2 bg-black bg-opacity-50" style="margin: 20px; padding: 20px;">
                        <div class="label col-start-1 col-end-7">
                            <span class="label-text text-lg text-white">ค้นหาชื่องานวิจัย</span>
                        </div>
                        <div class="input-container">
                            <input type="text" id="inputFieldResearch" placeholder="ชื่องานวิจัย"
                                class="input input-bordered w-full rounded-none text-black " v-model="search.queryResearch" />
                            <span v-if="textInputErrorResearch && !textInputErrorResearchRegex"
                                class="label-text-alt text-sm text-red-500">กรุณากรอกชื่องานวิจัย เฉพาะตัวอักษร (a-z,
                                A-Z ก-๙) ตัวเลข (0-9) ช่องว่าง และอักขระ . - : () เท่านั้น</span>
                            <span v-else-if="textInputErrorResearchRegex"
                                class="label-text-alt text-sm text-red-500">กรุณาอย่าใส่อักขระพิเศษที่ไม่ได้ระบุ
                                ใส่ได้เฉพาะตัวอักษร (a-z, A-Z ก-๙) ตัวเลข (0-9) ช่องว่าง และอักขระ . - : ()
                                เท่านั้น</span>
                        </div>

                        <div class="indicator ml-auto"><!--  ปุ่มชิดขวา -->
                            <button class="btn btn-warning rounded-none" v-on:click="handleSearch('research')">
                                <img :src="searchIcon" alt="Icon Search" class="h-6 w-6" />
                                ค้นหา
                            </button>
                        </div>
                    </div>
                    <div class="bg-black bg-opacity-50 grid grid-cols-2 rol-2 items-center" style="margin: 20px; padding: 20px;">
                        <div class="label col-start-1 col-end-7 ">
                            <span class="label-text text-lg text-white">ค้นหาสาขาที่เชี่ยวชาญ</span>
                        </div>

                        <div >
                            <select id="selectExpertise" v-model="selected"
                                class="select select-bordered w-full rounded-none text-black" @change="onExpertiseChange"
                                placeholder="เลือก">
                                <option v-if="!selected" disabled selected value="">เลือก</option>
                                <option v-for="expertise in search_expertise" :key="expertise.n.id_e"
                                    :value="expertise.n.id_e">
                                    {{ expertise.n.expertise_name }}
                                </option>
                                
                            </select>
                            <span v-if="textInputErrorExpertise"
                                class="label-text-alt text-sm text-red-500">กรุณาเลือกข้อมูลสาขาที่เชี่ยวชาญ</span>
                        </div>
                        <div class="indicator ml-auto">
                            <router-link v-if="selected"
                                :to="{ name: 'graph_expertise', params: { id: selected } }">
                                 <button class="btn btn-warning rounded-none">
                                    <img :src="searchIcon" alt="Icon Search" class="h-6 w-6" />
                                    ค้นหา
                                    </button>
                            </router-link>
                            <button v-else v-on:click="showErrorExpertise" class="btn btn-warning rounded-none">
                                <img :src="searchIcon" alt="Icon Search" class="h-6 w-6" />
                                ค้นหา
                            </button>
                        </div>
                        

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios"; //ใช้เพื่อยิงไปที่ตัว api
import router from "../../router";
import { useStore } from "vuex";
import searchIcon from "@/assets/icon/search.png";

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
const search = ref({
    queryName: "",
    queryResearch: "",
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
                inputErrorAuthor = false;
                textInputErrorAuthor.value = false;
                textInputErrorAuthorRegex.value = false;
                router.push({ name: "listauthorname" });

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
                inputErrorResearch = false;
                textInputErrorResearch.value = false;
                textInputErrorResearchRegex.value = false;
                router.push({ name: "listresearchname" });
            } catch (error) {
                console.error("Error:", error);
            }
        }
    } else {
        console.log("Please enter a valid data");
        if (buttonType === 'author') {
            inputErrorAuthor = true;
            textInputErrorAuthor.value = true; // ระบุข้อความ error
            textInputErrorAuthorRegex.value = false;
            if (inputErrorAuthor) {
                inputFieldAuthors.classList.add('input-error'); //ใส่border สีแดง
            } else {
                inputFieldAuthors.classList.remove('input-error');
            }
        } else if (buttonType === 'research') {
            inputErrorResearch = true;
            textInputErrorResearch.value = true;
            textInputErrorResearchRegex.value = false;
            if (inputErrorResearch) {
                inputFieldResearchs.classList.add('input-error');
            } else {
                inputFieldResearchs.classList.remove('input-error');
            }
        }
    }
};

const fetch_search_author = async (queryName) => {
    await axios
        .get(`${import.meta.env.VITE_FASTAPI}/search_author/${queryName}`, {
            withCredentials: true,
        })
        .then((response) => {
            author_name.value = response.data;
            store.commit("setAuthorName", author_name.value); // เรียกใช้ mutation เพื่อเปลี่ยนแปลง state
            console.log(author_name.value);
        })
        .catch((error) => {
            author_name.value = "";
            store.commit("setAuthorName", author_name.value);
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
            store.commit("setResearchName", research_name.value);
            console.log(research_name.value);
        })
        .catch((error) => {
            research_name.value = "";
            store.commit("setResearchName", research_name.value);
            console.log(error);
        });
};

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

onMounted(() => {
    fetch_search_expertise();

    // setTimeout(() => {
    //     console.log(selected.value);
    // }, 5000);
});
</script>

<style>
span {
    color: white;
}

.image-background {
    /* ส่วนขยายรูปภาพ */
    background-size: cover;
    /* จัดกลุ่มรูปภาพให้อยู่ตรงกลาง */
    background-position: center;
    /* ตัดรูปภาพที่เกินขอบออก */
    overflow: hidden;
    /* ทำให้ภาพเต็มขนาด */
    height: 89vh;
    background-image: url("@/assets/images/background_search.jpg");
}
</style>
