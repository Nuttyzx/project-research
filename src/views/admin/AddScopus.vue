<template>
    <br><br><br><br>
    <p class="text-center text-xl">เพิ่มข้อมูลงานวิจัยจากเว็บไซต์ Scopus</p>
    <br>
    <div class="flex items-center justify-center gap-2">  
        <input type="text" class="input input-bordered rounded-md w-96" placeholder="หมายเลข Scopus Author ID" v-model="insert_author_id_scopus"  /> 
         <button class="btn btn-warning rounded-md " v-on:click="sendDataToAPIScopue">
            ค้นหา
        </button>
    </div>
    
    <div v-if="json_scopus && json_scopus['search-results'] && json_scopus['search-results']['entry'].length > 0">
        <div v-for="(entry, index) in json_scopus['search-results']['entry']" :key="index" class="collapse collapse-arrow bg-base-200 w-auto mt-8 mb-8 ml-36 mr-36" >
            <input type="radio" name="my-accordion-2" /> 
            <div class="collapse-title text-xl font-medium">
                {{ entry['dc:title'] }} 
            </div>
            <div class="collapse-content" style="margin: 5px;"> 
                <pre>ชื่อวารสารหรือบทความ: {{ entry['prism:publicationName'] ? entry['prism:publicationName'] : '-'}}</pre>
                <pre>ปีที่เผยแพร่: {{ entry['prism:coverDisplayDate'] ? entry['prism:coverDisplayDate'] : '-'}}</pre>
                <pre>ประเภทงานวิจัย: {{ entry['prism:aggregationType'] ? entry['prism:aggregationType'] : '-'}}</pre>
                <pre>ชื่อนักวิจัยคนแรก: {{ entry['dc:creator'] ? entry['dc:creator'] : '-'}}</pre>
                <pre v-if="entry['affiliation'] && entry['affiliation'][0]">สำนักงาน: {{ entry['affiliation'][0]['affilname'] }}, {{ entry['affiliation'][0]['affiliation-city'] }}, {{ entry['affiliation'][0]['affiliation-country'] }}</pre>
                <pre v-else>สำนักงาน: - </pre>
                <pre>DOI: {{ entry['prism:doi'] ? entry['prism:doi'] : '-' }}</pre>
                <pre>หมายเลขหน้า: {{ entry['prism:pageRange'] ? entry['prism:pageRange'] : '-' }}</pre>
                <pre>แหล่งที่เผยแพร่: scopus</pre>
                <div class="flex items-center">
                    <pre>Abstract URL:  </pre>
                    <a :href="getScopusAbstractURL(entry)" target="_blank" class="link link-primary">{{ getScopusAbstractURL(entry) }}</a>
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
    <div v-else-if="json_scopus && json_scopus['search-results'] && json_scopus['search-results']['entry'].length === 0">
        <p style="color: red;" class="text-center">ไม่พบข้อมูล</p>
    </div>
    

</template>

 <script setup>
import {ref} from "vue";
import router from "../../router";

// import crypto from 'crypto';
// import { createHash } from 'hash.js';

// const insert_lastname_author = ref("");
// const insert_firstname_author = ref("");
const json_scopus = ref([]);
import axios from 'axios';
const insert_author_id_scopus = ref("");

// สร้างฟังก์ชันสำหรับส่งข้อมูลไปยัง API IEEE
async function sendDataToAPIScopue() {
   
   if(!insert_author_id_scopus.value || insert_author_id_scopus.value.trim() === ""){
        alert("กรุณากรอก นามสกุลนักวิจัย")
    
        json_scopus.value = "";
        
    }
        try {
            const response = await axios.get(`${import.meta.env.VITE_FASTAPI}/insert_author_scopus`, {
                params: {
                    scopus_id: insert_author_id_scopus.value.trim(),
                    // author: insert_lastname_author.value.trim(),
                    // firstname: insert_firstname_author.value.trim(),
                },
                headers: {
                    "ngrok-skip-browser-warning": "69420",
                    "Content-Type": "application/json",
                },  
            });
            // console.log(response.data);
            // json_ieee.value = response.data;
             // ตรวจสอบว่า response มีโครงสร้างข้อมูลที่ตรงกับโครงสร้าง Pydantic หรือไม่
             if (response.data["search-results"] && response.data["search-results"]["opensearch:totalResults"] !== "0"&& Array.isArray(response.data["search-results"].entry)) {
                json_scopus.value = response.data;
                console.log(json_scopus.value);
                console.log(json_scopus.value["search-results"].entry);
                console.log("เป็น")
            } else { // ไม่มีข้อมูลใน ieee record 0 
                alert("ไม่พบข้อมูล");
                console.log(response.data);
                json_scopus.value = "";
                scopus_article_data = [];
            }
        } catch (error) {
            console.error(error);
            json_scopus.value = "";
            // isState.value = false;
        }
    }
    
// }

const hasScopusRef = (entry) => {
      return entry.link.some(link => link['@ref'] === 'scopus');
};

// const getScopusAbstractURL = (entry) => {
//       const scopusLink = entry.link.find(link => link['@ref'] === 'scopus');
//       return scopusLink ? scopusLink['@href'] : '';
// };

const getScopusAbstractURL = (entry) => {
    // ตรวจสอบว่า entry.link เป็น array และมีค่าที่เป็น array ที่ไม่ใช่ null หรือ undefined
    if (Array.isArray(entry.link)) {
        const scopusLink = entry.link.find(link => link['@ref'] === 'scopus');
        return scopusLink ? scopusLink['@href'] : '';
    }
    return '';
};


async function importData() {
    if (!json_scopus.value || !json_scopus.value["search-results"] || !json_scopus.value["search-results"].entry) {
        alert("ไม่มีข้อมูลที่จะส่งไปยัง API");
        return;
    }

    try {
        // สร้าง array ของข้อมูลบทความ
        const scopus_article_data = json_scopus.value["search-results"].entry.map(entry => {
            // ตรวจสอบว่ามี link ที่เกี่ยวข้องกับ scopus หรือไม่
            // const scopusLink = entry.link.find(link => link['@ref'] === 'scopus');
            // ตรวจสอบว่า entry.link เป็น array และมีค่าที่เป็น array ที่ไม่ใช่ null หรือ undefined
            const scopusLink = Array.isArray(entry.link) ? entry.link.find(link => link['@ref'] === 'scopus') : '';
           
            return {
                abstract_url: scopusLink ? scopusLink['@href'] : '',
                article_number: entry['article-number'] || '',
                authors: [{
                    full_name: entry['dc:creator'] || '',
                    office: entry.affiliation && entry.affiliation[0]?.affilname || '',
                    province: entry.affiliation && entry.affiliation[0]?.['affiliation-city'] || '',
                    country: entry.affiliation && entry.affiliation[0]?.['affiliation-country'] || ''
                }],
                content_type: entry['prism:aggregationType'] || '',
                doi: entry['prism:doi'] || '',
                end_page: entry['prism:pageRange']?.split('-')[1] || '', // Extract end page from pageRange
                publication_title: entry['prism:publicationName'] || '',
                publication_year: (entry['prism:coverDisplayDate']) || '', // Parse string to integer for year
                publisher: scopusLink ? scopusLink['@ref'] : '',
                start_page: entry['prism:pageRange']?.split('-')[0] || '', // Extract start page from pageRange
                title: entry['dc:title'] || '', 
            };
        });
        console.log(scopus_article_data)
        // ส่งข้อมูลไปยัง API โดยใช้ Axios
        const response = await axios.post(`${import.meta.env.VITE_FASTAPI}/import_data`, { articles: scopus_article_data });
        console.log("เพิ่มสำเร็จ");
        await alert("เพิ่มข้อมูลสำเร็จ");
        await router.push('/showresearch');
        console.log(response.data);
    } catch (error) {
        alert("ไม่สามารถเพิ่มข้อมูลได้");
        console.error("เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง API:", error);
        
    }
}




 




</script> 