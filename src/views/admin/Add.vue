<template>
    <br><br><br><br>
    <p class="text-center text-xl">เพิ่มข้อมูลงานวิจัยจากเว็บไซต์ IEEE Xplore</p>
    <br>
    
        <div class="flex items-center justify-center gap-2">
            <input type="text" class="input input-bordered rounded-md" style="width: 40%;" placeholder="ชื่อ - นามสกุล นักวิจัยเป็นภาษาอังกฤษ เช่น Michael Gribbons" v-model="insert_author" /> <!-- กำหนดความกว้างและความสูง -->
            <button class="btn btn-warning rounded-md " v-on:click="sendDataToAPIIEEE">
                ค้นหา
            </button>
        </div>
        <!-- <label class="block text-sm leading-6 text-red-500">ตัวอย่าง  Michael Gribbons </label> -->

   
    <div v-if="json_ieee && json_ieee.articles && json_ieee.total_records > 0">
        <div v-for="(jsonAuthor , index) in json_ieee.articles" :key="index" class="collapse collapse-arrow bg-base-200 w-auto mt-8 mb-8 ml-36 mr-36" >
            <input type="radio" name="my-accordion-2" /> 
            <div class="collapse-title text-xl font-medium">
                {{ jsonAuthor.title }} 
            </div>
            <div class="collapse-content" style="margin: 5px;"> 
                <pre>ชื่อวารสารหรือบทความ: {{jsonAuthor.publication_title ? jsonAuthor.publication_title : '-'}}</pre>
                <!-- <pre class="text-balance indent-8">{{ jsonAuthor.publication_title }}</pre> -->
                <pre>ปีที่เผยแพร่: {{jsonAuthor.publication_year ? jsonAuthor.publication_year : '-'}}</pre>
                <pre>ประเภทงานวิจัย: {{jsonAuthor.content_type ? jsonAuthor.content_type : '-'}}</pre>
                <pre>ชื่อนักวิจัย: <span class="text-black" v-html="concatAuthorNames(jsonAuthor.authors.authors)"></span></pre>
                <pre>แหล่งที่เผยแพร่: {{jsonAuthor.publisher ? jsonAuthor.publisher : '-'}}</pre>
                <pre>doi: {{jsonAuthor.doi ? jsonAuthor.doi:"-"}}</pre>
                <pre>หมายเลขหน้า: {{ jsonAuthor.start_page }} - {{ jsonAuthor.end_page }} </pre>
                <div class="flex items-center">
                    <pre>Abstract_URL:  </pre>
                    <a :href="jsonAuthor.abstract_url" target="_blank" class="link link-primary">{{ jsonAuthor.abstract_url }}</a>
                </div>
            </div>
        </div>
        <div class="flex items-center justify-center">
           
                <button class="btn btn-primary text-white rounded-md" v-on:click="importData">
                    เพิ่มข้อมูล
                </button>
            
           
        </div>
        <br>
    </div>
    <div v-else-if="json_ieee && json_ieee.total_records === 0">
        <p style="color: red;" class="text-center">ไม่พบข้อมูล</p>
    </div>


</template>

<script setup>
import {ref} from "vue";
import router from "../../router";
const insert_author = ref("");
const json_ieee = ref([]);

import axios from 'axios';

// สร้างฟังก์ชันสำหรับส่งข้อมูลไปยัง API IEEE
async function sendDataToAPIIEEE() {
    if(insert_author.value.trim() === ""){
        alert("กรุณากรอก ชื่อ-นามสกุล ของนักวิจัย")
    
        json_ieee.value = "";
        
    }
    else{
        try {
            const response = await axios.get(`${import.meta.env.VITE_FASTAPI}/insert_author_ieee`, {
                params: {
                    author: insert_author.value.trim(),
                },
                headers: {
                    "ngrok-skip-browser-warning": "69420",
                    "Content-Type": "application/json",
                }, 
            });
            // console.log(response.data);
            // json_ieee.value = response.data;
             // ตรวจสอบว่า response มีโครงสร้างข้อมูลที่ตรงกับโครงสร้าง Pydantic หรือไม่
            if (response.data.articles && Array.isArray(response.data.articles)) {
                json_ieee.value = response.data;
                console.log(json_ieee.value);
                console.log("เป็น")
            } else { // ไม่มีข้อมูลใน ieee record 0 
                alert("ไม่พบข้อมูล");
                console.log(response.data);
                articleData = [];
            }
        } catch (error) {
            console.error(error);
            json_ieee.value = "";
            // isState.value = false;
        }
    }
    
}

const concatAuthorNames = (authors) => {
    if (!authors || authors.length === 0) return '-';

      // แบ่งผู้เขียนออกเป็นกลุ่ม ๆ ละ 6 คน
    const lines = [];
    for (let i = 0; i < authors.length; i += 6) {
        let chunk;
        if (i + 6 < authors.length) {
            // ถ้ามากกว่า 6 คน ให้ ใส่ , ต่อท้าย
            chunk = authors.slice(i, i + 6).map((author, index) => {
                if (index === 5) return author.full_name + ',';
                return author.full_name;
            }).join(', ');
        } else {
            // ถ้าน้อยกว่า 6 คนไม่ต้องใส่ , ท้าย
            chunk = authors.slice(i, i + 6).map(author => author.full_name).join(', ');
        }
        lines.push(chunk);
    }

      // รวมกลุ่มที่ได้เข้าด้วยกันโดยใช้เครื่องหมายบรรทัดใหม่
    return lines.join('<br>');
    
}

async function importData() {
        // ตรวจสอบว่า json_ieee มีค่าหรือไม่
    if (!json_ieee.value) {
        alert("ไม่มีข้อมูลที่จะส่งไปยัง API");
        return;
    }
    try {
        // ฟังก์ชันเพื่อรวมคำที่ไม่ซ้ำจากทั้ง ieee_terms
        const extractKeywords = (article) => {
            const ieeeTerms = Array.isArray(article.index_terms?.ieee_terms?.terms) ? article.index_terms.ieee_terms.terms.filter(term => term) : [];
            return ieeeTerms.join(', ');
        };

        // แปลงรูปแบบ JSON ให้เป็นโครงสร้างที่ถูกต้องสำหรับ FastAPI
        //ใช้ || เราสามารถกำหนดค่าเริ่มต้นให้กับ property ที่มีค่า undefined ได้ โดยให้ค่าเป็น ''
        const articleData = json_ieee.value.articles.map(article => ({        
            abstract_url: article.abstract_url || '',
            article_number: article.article_number || '',
            authors: Array.isArray(article.authors.authors) ? article.authors.authors.map(author => ({
                authorUrl: author.authorUrl || '',
                full_name: author.full_name || '',
                id: author.id || ''
            })) : [],
            content_type: article.content_type || '',
            doi: article.doi || '',
            end_page: article.end_page || '',
            publication_title: article.publication_title || '',
            publication_year: article.publication_year.toString() || '',
            publisher: article.publisher || '',
            start_page: article.start_page || '',
            title: article.title || '',
            abstract: article.abstract || '',
            keyword: extractKeywords(article)
        }));
        
        // ส่งข้อมูลไปยัง API โดยใช้ Axios
        // console.log(articleData)
        const response = await axios.post(`${import.meta.env.VITE_FASTAPI}/import_data`, { articles: articleData });
        console.log("เพิ่มสำเร็จ");
        await alert("เพิ่มข้อมูลสำเร็จ");
        await router.push('/showresearch');
      
    } catch (error) {
        console.error("เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง API:", error);
        alert("ไม่สามารถเพิ่มข้อมูลได้");
        
    }
}




// async function importData() {
//     // ตรวจสอบว่า json_ieee มีค่าหรือไม่
//     if (!json_ieee.value) {
//         alert("ไม่มีข้อมูลที่จะส่งไปยัง API");
//         return;
//     }

//     try {
//         const response = await axios.post(`${import.meta.env.VITE_FASTAPI}/import_data`, json_ieee.value);
//         console.log("เพิ่มสำเร็จ");
//         console.log(response.data);
//         // ตรวจสอบว่า response มีโครงสร้างข้อมูลที่ตรงกับโครงสร้าง Pydantic หรือไม่
//         if (response.data.message) {
//             alert(response.data.message);
//         } else {
//             alert("ข้อมูลที่ได้รับไม่ถูกต้อง");
//         }
//     } catch (error) {
//         console.error(error);
//         alert("เกิดข้อผิดพลาดในการส่งข้อมูล");
//     }
// }
</script>