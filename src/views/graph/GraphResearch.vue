<template>
    <br><br><br>
    <p class="flex items-center text-xl" style="margin: 20px; ">ข้อมูลงานวิจัย &nbsp;</p>
    <div class="overflow-x-auto border border-slate-900 " style="margin: 20px; ">
        <table v-if="researchData && researchData.length > 0"
            class="table table-md table-pin-rows table-pin-cols text-center">
            <thead>
                <tr class="border-b border-black text-base text-white bg-gradient-to-r from-sky-500 to-indigo-500">
                    <td>ชื่องานวิจัย</td>
                    <td>ปีที่เผยแพร่</td>
                    <td>ชื่อวารสารหรือบทความ</td>
                    <td>หมายเลขงานวิจัย</td>
                    <td>ประเภทงานวิจัย</td>
                    <td>หมายเลขหน้า</td>
                    <td>Doi</td>
                    <td>แหล่งที่เผยแพร่</td>
                    <td>Abstract URL</td>
                    
                </tr>
            </thead>
            <tbody>
                <tr v-for="(article) in researchData" :key="article.id_article">
                    <td class="border-r border-black text-left align-top" :style="{textAlign: article.t.title ? 'left' : 'center'}">
                        <div class="w-72">{{article.t.title ? article.t.title : "-"}}</div>
                    </td> 
                    <td class="border-r border-black text-left align-top" :style="{textAlign: article.t.publication_year ? 'left' : 'center'}">
                        {{ article.t.publication_year ? article.t.publication_year: "-"}}
                    </td>
                    <td class="border-r border-black text-left align-top" :style="{textAlign: article.t.publication_title ? 'left' : 'center'}">
                        <div class="w-64">{{ article.t.publication_title ? article.t.publication_title: "-"}}</div>
                    </td>
                    <td class="border-r border-black text-left align-top" :style="{textAlign: article.t.article_number ? 'left' : 'center'}">
                        {{ article.t.article_number ? article.t.article_number: "-"}}
                    </td>
                    <td class="border-r border-black text-left align-top" :style="{textAlign: article.t.content_type ? 'left' : 'center'}">
                        {{ article.t.content_type ? article.t.content_type: "-" }}
                    </td>
                    <td class="border-r border-black text-left align-top" :style="{textAlign: (article.t.start_page && article.t.end_page) ? 'left' : 'center'}">
                        <div class="w-24">{{(article.t.start_page && article.t.end_page) ? article.t.start_page + ' - ' + article.t.end_page : "-"}}</div>
                    </td>
                    <td class="border-r border-black text-left align-top" :style="{ textAlign: article.t.doi ? 'left' : 'center' }">
                        {{ article.t.doi ? article.t.doi : "-" }}
                    </td>
                    <td class="border-r border-black text-left align-top" :style="{textAlign: article.t.publisher ? 'left' : 'center'}">
                        {{ article.t.publisher ? article.t.publisher : "-"}}</td>
                        <td class="text-left align-top" :style="{textAlign: article.t.abstract_url ? 'left' : 'center'}">
                            <template v-if="article.t.abstract_url &&article.t.abstract_url !== '-'">
                                <a :href="article.t.abstract_url" target="_blank" class="link link-primary">{{article.t.abstract_url}}</a>
                            </template>
                            <template v-else>
                                <span class="text-black">-</span>
                            </template>
                        </td>
                </tr>
            </tbody>
        </table>
    </div>
  
    <p class="flex items-center text-xl" style="margin: 20px; ">ข้อมูลนักวิจัย &nbsp;</p>

    <div class="overflow-x-auto border border-slate-900" style="margin: 20px; ">
        <table v-if="researchData && researchData.length > 0" class="table table-md table-pin-rows table-pin-cols text-center table table-zebra">
            <thead>
                <tr class="border-b border-black text-base text-white bg-gradient-to-r from-sky-500 to-indigo-500">
                    <td>ชื่อภาษาอังกฤษ</td>
                    <td>ชื่อภาษาไทย</td>
                    <td>วุฒิการศึกษาสูงสุด</td>
                    <td>สาขาที่เชี่ยวชาญ</td>
                    <td>อีเมล</td>
                    <td>หน่วยงาน</td>
                    <td>จังหวัด/เมือง</td>
                    <td>ประเทศ</td>
                    <td>IEEE URL</td>
                    <td>เว็บไซต์</td>
                    <td></td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="author in researchData[0].authors_w_degrees_w_expertises" :key="author.author.id">
                    <td class="border-r border-black text-left align-top" :style="{ textAlign: author.author.full_name ? 'left' : 'center' }">
                        <div class="w-44">{{ author.author.full_name ? author.author.full_name: "-"}}</div>
                    </td>
                    <td class="border-r border-black align-top"
                        :style="{ textAlign: author.author.name_th ? 'left' : 'center' }">
                        <div class="w-44">{{ author.author.name_th ? author.author.name_th : "-" }}</div><!--ternary operator-->
                    </td>
                    <!--มีค่าให้ขึ้นชื่อ ใข้:style attribute ใน Vue.js เพื่อกำหนด CSS inline style-->
                    <td class="border-r border-black align-top" :style="{ textAlign: author.degree.length > 0  ? 'left' : 'center' }">
                        <template v-if="author.degree.length > 0">
                            <template v-for="degree in author.degree" :key="degree.id">
                                <div class="w-48" :style="{ textAlign: degree.degrees != null && degree.degrees.degree_name !== null  ? 'left' : 'center' }">  
                                    {{degree.degrees != null && degree.degrees.degree_name !== null ? "- " + degree.degrees.degree_name : "-" }}
                                    <br><br>
                                </div>
                            </template>
                        </template>
                        <template v-else>-</template>
                    </td>
                    <td class="border-r border-black align-top" :style="{ textAlign: author.expertise.length > 0 ? 'left' : 'center' }">
                        <template v-if="author.expertise.length > 0">
                            <template v-for="expertise in author.expertise" :key="expertise.id">
                                <div class="w-44" :style="{ textAlign: expertise.expertises !== null && expertise.expertises.expertise_name !== null ? 'left' : 'center' }">    
                                    {{ expertise.expertises !== null && expertise.expertises.expertise_name !== null ? "- " + expertise.expertises.expertise_name : "-" }}
                                    <br><br>
                                </div> 
                            </template>
                        </template>
                        <template v-else>-</template>
                    </td>
                    <td class="border-r border-black align-top" :style="{ textAlign: author.author.email ? 'left' : 'center' }">
                        {{ author.author.email ? author.author.email : "-" }}
                    </td>
                    <td class="border-r border-black align-top" :style="{ textAlign: author.author.office ? 'left' : 'center' }">
                        <div class="w-40">{{ author.author.office ? author.author.office : "-" }}</div>
                    </td>
                    <td class="border-r border-black align-top" :style="{ textAlign: author.author.province ? 'left' : 'center' }">
                        <div class="w-28">{{ author.author.province ? author.author.province : "-" }}</div>
                    </td>
                    <td class="border-r border-black align-top" :style="{ textAlign: author.author.country ? 'left' : 'center' }">
                        <div class="w-22">{{ author.author.country ? author.author.country : "-" }}</div>
                    </td>
                    <td class="border-r border-black align-top" :style="{ textAlign: author.author.authorUrl ? 'left' : 'center' }">
                        <template v-if="author.author.authorUrl && author.author.authorUrl !== '-'">
                            <a :href="author.author.authorUrl" target="_blank" class="link link-primary">{{author.author.authorUrl }}</a>
                        </template>
                        <template v-else>
                            <span class="text-black">-</span>
                        </template>
                        <!-- ใช้ :href และผูกค่ากับ author.properties.authorUrl ทำให้ลิงก์ทำงานได้โดยอัตโนมัติ-->
                    </td>
                    <td class="border-r border-black align-top " :style="{ textAlign: author.author.website ? 'left' : 'center' }">
                        <template v-if="author.author.website && author.author.website !== '-'">
                            <a :href="author.author.website" target="_blank" class="link link-primary">{{author.author.website}}</a>
                        </template>
                        <template v-else>
                            <span class="text-black">-</span>
                        </template>
                    </td>
                    <td class="align-top link link-info" >
                      <div class="w-14">
                        <router-link :to="{ name: 'graph_author', params: { id: author.author.id}}">
                              ดูเพิ่มเติม
                          </router-link>
                       </div> 
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <br>
    <!-- <div>
        <p class="flex items-center text-xl" style="margin: 20px; ">
            <img :src="nodeIconRedSrc" alt="Node Red" class="h-4 w-4" />&nbsp;  = &nbsp; ข้อมูลนักจัย &nbsp; , &nbsp;
            <img :src="nodeIconOrangeSrc" alt="Node Orange" class="h-4 w-4" />&nbsp;  = &nbsp; ข้อมูลงานวิจัย &nbsp; , &nbsp;
            <img :src="nodeIconBlueSrc" alt="Node Green" class="h-4 w-4" />&nbsp;  = &nbsp; วุฒิการศึกษา &nbsp; , &nbsp;
            <img :src="nodeIconGreenSrc" alt="Node Blue" class="h-4 w-4" />&nbsp;  = &nbsp; สาขาที่เชี่ยวชาญ 
        </p>
    </div> -->
    <!-- <div>
        <div id="graph"></div>
    </div> -->

</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import {useRoute} from 'vue-router'
const router = useRoute()
const researchData = ref({});

onMounted(() => {
  fetchData();
 
});

const fetchData = () => {
  const id_research = router.params.id;
  if (!id_research) {
    console.error("id_research is undefined or null");
    return;
  }
  axios
    .get(`${import.meta.env.VITE_FASTAPI}/single_research_graph/${id_research}`, {
      withCredentials: true,
    })
    .then((response) => {
        researchData.value = response.data;
        console.log(researchData.value);
        // console.log(response.data)
      
    });
};



// import * as d3 from "d3";
// import { ref } from "vue";
// import nodeIconRed from "@/assets/icon/red.png";
// import nodeIconOrange from "@/assets/icon/orange.png";
// import nodeIconGreen from "@/assets/icon/green.png";
// import nodeIconBlue from "@/assets/icon/blue.jpg";
// export default {
//     data() {
//         return {
//             force: null,
//             svg: null,
//         };
//     },
//     setup() {
//         const authorNodes = ref({});
//         const articleNodes = ref({});
//         const nodeIconRedSrc = ref(nodeIconRed);
//         const nodeIconOrangeSrc = ref(nodeIconOrange);
//         const nodeIconGreenSrc = ref(nodeIconGreen);
//         const nodeIconBlueSrc = ref(nodeIconBlue);

//         return {
//             authorNodes,
//             articleNodes,
//             nodeIconRedSrc, nodeIconOrangeSrc, nodeIconGreenSrc, nodeIconBlueSrc,
//         };
//     },
//     mounted() {
//         //สร้าง SVG container สำหรับกราฟ
//         this.svg = d3
//             .select("#graph")
//             .append("svg")
//             .attr("width", "100%")
//             .attr("height", "100%")
//             .attr("pointer-events", "all");

//         window.addEventListener("resize", this.resizeGraph); //ถูกเรียกเมื่อหน้าจอถูกปรับขนาด ซึ่งจะทำการปรับ force center และ SVG ใหม่.
//         this.fetchGraphData();
//     },
//     methods: {
//         fetchGraphData() {
//             const idNodeArticle = this.$route.params.id;
//             console.log(idNodeArticle);
//             if (!idNodeArticle) {
//                 console.error("id_author is undefined or null");
//                 return;
//             }

//             axios
//                 .get(`${import.meta.env.VITE_FASTAPI}/graph_data_article/${idNodeArticle}`, {
//                     withCredentials: true,
//                 })
//                 .then((response) => {
//                     console.log(response);
//                     const graphData = response.data.graph_data;
//                     // กรององค์ประกอบที่มี label เป็น "Author"
//                     this.authorNodes.value = graphData.nodes.filter((node) =>
//                         node.labels.includes("Author")
//                     );
//                     console.log(this.authorNodes.value);

//                     this.articleNodes.value = graphData.nodes.filter((node) =>
//                         node.labels.includes("Article")
//                     );
//                     console.log(this.articleNodes.value);

//                     this.force = d3
//                         .forceSimulation(graphData.nodes)
//                         .force("charge", d3.forceManyBody().strength(-100))
//                         .force("link", d3.forceLink(graphData.links).id((d) => d.id).distance(150).strength(2))
//                         .force("center", d3.forceCenter(window.innerWidth / 2, window.innerHeight / 2).strength(0.1))
//                         .on("tick", this.ticked);

//                     // ล้างข้อมูลเดิม
//                     this.force.nodes([]);
//                     this.force.force("link").links([]);

//                     // สร้างเส้น link
//                     const link = this.svg
//                         .selectAll("link")
//                         .data(graphData.links)
//                         .enter()
//                         .append("line")
//                         .attr("class", "link")
//                         .style("stroke", "#999")
//                         .attr("stroke-opacity", 0.6)
//                         .attr("stroke-width", (d) => Math.sqrt(d.value));

//                     // สร้างโหนด node
//                     const node = this.svg
//                         .selectAll(".node")
//                         .data(graphData.nodes)
//                         .enter()
//                         .append("circle")
//                         .attr("class", (d) => "node " + d.labels.join(" "))
//                         .attr("r", 20)
//                         .style("fill", (d) => {
//                             if (d.labels.includes("Author")) {
//                                 return "red";
//                             } else if (d.labels.includes("Article")) {
//                                 return "orange";
//                             } else if (d.labels.includes("Degree")) {
//                                 return "blue";
//                             } else if (d.labels.includes("Expertise")) {
//                                 return "green";
//                             } else {
//                                 return "gray";
//                             }
//                         })

//                         .call(
//                             d3
//                                 .drag()
//                                 .on("start", (event, d) => this.dragstarted(event, d))
//                                 .on("drag", (event, d) => this.dragged(event, d))
//                                 .on("end", (event, d) => this.dragended(event, d))
//                         ); // ทำให้โหนดเลื่อนได้


//                     // เพิ่มข้อมูลใหม่
//                     this.force
//                         .nodes(graphData.nodes)
//                         .force("link")
//                         .links(graphData.links);
//                     this.force.alpha(1).restart();

//                     // Set node title attribute
//                     node.append("title").text(function (d) {
//                         if (d.labels.includes("Author")) {
//                             var full_name = d.properties.full_name ?  d.properties.full_name : "-";
//                             var name_th = d.properties.name_th ?  d.properties.name_th : "-";
//                             var email =  d.properties.email ? d.properties.email : "-";
//                             var office = d.properties.office ? d.properties.office : "-";
//                             var province = d.properties.province ? d.properties.province : "-";
//                             var country = d.properties.country ? d.properties.country : "-";
//                             return  "ชื่อภาษาอังกฤษ:  " + full_name + "\n" +
//                                     "ชื่อภาษาไทย:  " + name_th + "\n" +
//                                     "อีเมล:  " + email + "\n" +
//                                     "สำนักงาน:  " + office + "\n" +
//                                     "จังหวัด:  " + province + "\n" +
//                                     "ประเทศ:  " + country;
//                         } else if (d.labels.includes("Article")) {
//                             var country = d.properties.title  ? d.properties.title  : "-" ;
//                             var publication_year = d.properties.publication_year  ? d.properties.publication_year  : "-" ;
//                             var publication_title = d.properties.publication_title  ? d.properties.publication_title  : "-" ;
//                             var content_type = d.properties.content_type  ? d.properties.content_type : "-" ;
//                             var doi = d.properties.doi  ? d.properties.doi : "-" ;
//                             var page = "";
//                             if(d.properties.start_page && d.properties.end_page){
//                                 page = d.properties.start_page + " - " + d.properties.end_page;
//                             }
//                             else if(d.properties.start_page && d.properties.end_page == ""){
//                                 page = d.properties.start_page;
//                             }
//                             else{
//                                 page = "-";
//                             }
//                             return  "ชื่องานวิจัย:  " + country + "\n" +
//                                     "ปีที่เผยแพร่:  " + publication_year+ "\n" +
//                                     "ชื่อวารสารหรือบทความ:  " + publication_title + "\n" +
//                                     "ประเภทงานวิจัย:  " + content_type + "\n" +
//                                     "หมายเลขหน้า:  " + page + "\n" +
//                                     "doi:  " + doi ;
//                         } else if (d.labels.includes("Degree")){
//                             return d.properties.degree_name ? d.properties.degree_name : "-";

//                         } else if (d.labels.includes("Expertise")){
//                             return d.properties.expertise_name ? d.properties.expertise_name  : "-";          
//                         } else {
//                             return JSON.stringify(d.properties, null, 2).replace(/,/g, ",\n");
//                         }
//                     });


//                     // Force simulation ticks อัปเดตตำแหน่งของลิงก์และโหนด
//                     this.force.on("tick", () => {
//                         link
//                             .attr("x1", (d) => d.source.x)
//                             .attr("y1", (d) => d.source.y)
//                             .attr("x2", (d) => d.target.x)
//                             .attr("y2", (d) => d.target.y);

//                         node.attr("cx", (d) => d.x).attr("cy", (d) => d.y);
//                     });
//                 })
//                 .catch((error) => {
//                     console.log("Error fetching graph data:", error);
//                 });
//         },
//         resizeGraph() {
//             // คำสั่งในการปรับ force center ใหม่โดยกำหนดให้โหนดบทความอยู่ตรงกลางของหน้าจอ
//             const centerForceX = window.innerWidth / 2;
//             const centerForceY = window.innerHeight / 2;
//             this.force.force("center", d3.forceCenter(centerForceX, centerForceY));

//             // คำนวณพิกัดใหม่ของโหนด label "Article" เพื่อให้อยู่ตรงกลางของหน้าจอ
//             const articleNodes = this.svg.selectAll(".node")
//                 .filter(d => d.labels.includes("Article")); // เลือกเฉพาะโหนดที่เป็น label "Article"

//             const articleNodeX = window.innerWidth / 2;
//             const articleNodeY = window.innerHeight / 2;
//             articleNodes.attr("cx", articleNodeX)
//                 .attr("cy", articleNodeY);

//             this.svg
//                 .attr("width", window.innerWidth)
//                 .attr("height", window.innerHeight); // ปรับขนาด SVG
//             this.force.restart(); // รีสตาร์ท force
//         },


//         dragstarted(event, d) {
//             if (!event.active) this.force.alphaTarget(0.3).restart();
//             d.fx = d.x;
//             d.fy = d.y;
//         },
//         dragged(event, d) {
//             d.fx = event.x;
//             d.fy = event.y;
//         },
//         dragended(event, d) {
//             if (!event.active) this.force.alphaTarget(0);
//             d.fx = null;
//             d.fy = null;
//         },
//     },
// };
</script>
<style scoped>
body {
    margin: 0;
}

#graph {
    width: 90vw;
    height: 100vh;
}

/* svg {
    width: 100%;
    height: 100%;
    max-width: 100vw;
    max-height: 100vh; 
} */
</style>