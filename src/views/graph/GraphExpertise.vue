<template>
    <!-- <template v-for="author in authorNodes.value" :key="author.id">
        <div v-for="expertise in author.properties.expertises" :key="expertise.id_e">    
            <p class="flex items-center">รายชื่อนักวิจัยที่เชี่ยวชาญสาขา &nbsp; {{expertise.expertise_name ? expertise.expertise_name : "-"}} </p>
        </div> 
    </template> -->
    <br><br><br>
    <p class="flex items-center text-xl " style="margin: 20px; ">รายชื่อนักวิจัยที่เชี่ยวชาญสาขานี้</p>

    <div class="overflow-x-auto border border-slate-900" style="margin: 20px; ">
        <table v-if="expertiseData && expertiseData.length > 0" class="table table-md table-pin-rows table-pin-cols text-center  table table-zebra">
            <thead>
                <tr class="border-b border-black text-base  text-white bg-gradient-to-r from-sky-500 to-indigo-500">
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
                <tr v-for="author in expertiseData" :key="author.authors_w_degrees_w_expertises[0].author.id">
                    <td class="border-r border-black text-left align-top" :style="{ textAlign: author.authors_w_degrees_w_expertises[0].author.full_name ? 'left' : 'center' }" >
                      <div class="w-44">{{ author.authors_w_degrees_w_expertises[0].author.full_name ? author.authors_w_degrees_w_expertises[0].author.full_name:"-"}}</div>
                    </td>
                    <td class="border-r border-black align-top"
                        :style="{ textAlign: author.authors_w_degrees_w_expertises[0].author.name_th ? 'left' : 'center' }">
                        <div class="w-44">{{ author.authors_w_degrees_w_expertises[0].author.name_th ? author.authors_w_degrees_w_expertises[0].author.name_th : "-" }}</div>
                    </td>
                    
                    <td class="border-r border-black align-top" :style="{ textAlign: author.authors_w_degrees_w_expertises[0].degree.length > 0 ? 'left' : 'center' }">
                        <template v-if="author.authors_w_degrees_w_expertises[0].degree.length > 0">
                            <template v-for="degree in author.authors_w_degrees_w_expertises[0].degree" :key="degree.id">
                                <div class="w-48" :style="{ textAlign: degree.degrees != null && degree.degrees.degree_name !== null  ? 'left' : 'center' }">
                                  {{degree.degrees != null && degree.degrees.degree_name !== null ? "- " + degree.degrees.degree_name : "-" }}
                                    <br><br>
                                </div>
                            </template>
                        </template>
                        <template v-else>-</template>
                    </td>
                    <td class="border-r border-black align-top" :style="{ textAlign: author.authors_w_degrees_w_expertises[0].expertise.length > 0 ? 'left' : 'center' }">
                        <template v-if="author.authors_w_degrees_w_expertises[0].expertise.length > 0">
                            <template v-for="expertise in author.authors_w_degrees_w_expertises[0].expertise" :key="expertise.id">
                                <div class="w-44">    
                                    {{ "- " + (expertise.expertises.expertise_name ? expertise.expertises.expertise_name : "-") }} 
                                    <br> <br>
                                </div> 
                            </template>
                        </template>
                        <template v-else>-</template>
                    </td>
                    <td class="border-r border-black align-top" :style="{ textAlign: author.authors_w_degrees_w_expertises[0].author.email ? 'left' : 'center' }">
                        {{ author.authors_w_degrees_w_expertises[0].author.email ? author.authors_w_degrees_w_expertises[0].author.email : "-" }}
                    </td>
                    <td class="border-r border-black align-top" :style="{ textAlign: author.authors_w_degrees_w_expertises[0].author.office ? 'left' : 'center' }">
                      <div class="w-42">{{ author.authors_w_degrees_w_expertises[0].author.office ? author.authors_w_degrees_w_expertises[0].author.office : "-" }}</div>
                    </td>
                    <td class="border-r border-black align-top" :style="{ textAlign: author.authors_w_degrees_w_expertises[0].author.province ? 'left' : 'center' }">
                      <div class="w-28">{{ author.authors_w_degrees_w_expertises[0].author.province ? author.authors_w_degrees_w_expertises[0].author.province : "-" }}</div>
                    </td>
                    <td class="border-r border-black align-top" :style="{ textAlign: author.authors_w_degrees_w_expertises[0].author.country ? 'left' : 'center' }">
                      <div class="w-22">{{ author.authors_w_degrees_w_expertises[0].author.country ? author.authors_w_degrees_w_expertises[0].author.country : "-" }}</div>
                    </td>
                    <td class="border-r border-black align-top" :style="{ textAlign: author.authors_w_degrees_w_expertises[0].author.authorUrl ? 'left' : 'center' }">
                        <template v-if="author.authors_w_degrees_w_expertises[0].author.authorUrl && author.authors_w_degrees_w_expertises[0].author.authorUrl !== '-'">
                            <a :href="author.authors_w_degrees_w_expertises[0].author.authorUrl" target="_blank" class="link link-primary">{{author.authors_w_degrees_w_expertises[0].author.authorUrl }}</a>
                        </template>
                        <template v-else>
                            <span class="text-black">-</span>
                        </template>
                       
                    </td>
                    <td class="border-r border-black align-top" :style="{ textAlign: author.authors_w_degrees_w_expertises[0].author.website ? 'left' : 'center' }">
                        <template v-if="author.authors_w_degrees_w_expertises[0].author.website && author.authors_w_degrees_w_expertises[0].author.website !== '-'">
                            <a :href="author.authors_w_degrees_w_expertises[0].author.website" target="_blank" class="link link-primary">{{author.authors_w_degrees_w_expertises[0].author.website}}</a>
                        </template>
                        <template v-else>
                            <span class="text-black">-</span>
                        </template>
                    </td>
                    <td class="align-top link link-info">
                      <div class="w-14">
                        <router-link :to="{ name: 'graph_author', params: { id: author.authors_w_degrees_w_expertises[0].author.id}}">
                              ดูเพิ่มเติม
                          </router-link>
                       </div> 
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <br>
    <div>
        <p class="flex items-center text-xl" style="margin: 20px; ">
            <img :src="nodeIconRedSrc" alt="Node Red" class="h-6 w-6" />&nbsp;  = &nbsp; นักวิจัย &nbsp; , &nbsp;
            <img :src="nodeIconGreenSrc" alt="Node Green" class="h-6 w-6" />&nbsp;  = &nbsp; สาขาที่เชี่ยวชาญที่ค้นหา &nbsp; , &nbsp;
            <img :src="nodeIconBlueSrc" alt="Node Blue" class="h-6 w-6" />&nbsp;  = &nbsp; สาขาที่เชี่ยวชาญอื่นๆ 
        </p>
    </div>
    <div>
        <div id="graph"></div>
    </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute } from 'vue-router';
import * as d3 from "d3";
import nodeIconRed from "@/assets/icon/red.png";
import nodeIconGreen from "@/assets/icon/green.png";
import nodeIconBlue from "@/assets/icon/blue.jpg";

const force = ref(null);
const svg = ref(null);
const nodeIconRedSrc = ref(nodeIconRed);
const nodeIconGreenSrc = ref(nodeIconGreen);
const nodeIconBlueSrc = ref(nodeIconBlue);


const router = useRoute();
const expertiseData = ref({});

onMounted(() => {
  fetchData();

  svg.value = d3
    .select("#graph")
    .append("svg")
    .attr("width", window.innerWidth)
    .attr("height", window.innerHeight)
    .attr("pointer-events", "all")
    .append("g")
    .attr("transform", "scale(1)"); // ย่อขนาดกราฟ

  fetchGraphData();

  window.addEventListener("resize", resizeGraph);

});

const fetchData = async () => {
  const id_expertise = router.params.id;
  console.log(id_expertise);
  if (!id_expertise) {
    console.error("id_expertise is undefined or null");
    return;
  }
  try {
    const response = await axios.get(`${import.meta.env.VITE_FASTAPI}/single_expertise_graph/${id_expertise}`, {
      withCredentials: true,
    });

    expertiseData.value = response.data;
    console.log(expertiseData.value);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
  
};



const fetchGraphData = async () => {
  const id_expertise = router.params.id;
  console.log(id_expertise);
  if (!id_expertise) {
    console.error("id_expertise is undefined or null");
    return;
  }

  // ตรวจสอบข้อมูลที่แคชไว้ใน LocalStorage
//   const cachedData = localStorage.getItem(`graph_data_expertise_${id_expertise}`);
//   if (cachedData) {
//     const graphData = JSON.parse(cachedData);
//     if (svg.value) {
//       createGraph(graphData);
//     } else {
//       console.error("svg.value is not defined");
//     }
//     return;
//   }
    // ดึงข้อมูลจาก API
    try {
    const response = await axios.get(`${import.meta.env.VITE_FASTAPI}/graph_data_expertise/${id_expertise}`, {
      withCredentials: true,
    });
    const graphData = response.data.graph_data;

    if (!graphData || !graphData.nodes || !graphData.links) {
      console.error("Graph data is missing or incomplete", graphData);
      return;
    }

    // แคชข้อมูลที่ได้รับใน LocalStorage
    // localStorage.setItem(`graph_data_expertise_${id_expertise}`, JSON.stringify(graphData));

    if (svg.value) {
      createGraph(graphData);
    } else {
      console.error("svg.value is not defined");
    }
  } catch (error) {
    console.log("Error fetching graph data:", error);
  }
}


const createGraph = (graphData) => {
  if (!svg.value) {
    console.error("svg.value is not defined");
    return;
  }
  force.value = d3
    .forceSimulation(graphData.nodes)
    .force("charge", d3.forceManyBody().strength(-300))
    .force("link",d3.forceLink(graphData.links).id((d) => d.id).distance(80).strength(0.5))
    .force("center",d3.forceCenter(window.innerWidth / 2, window.innerHeight/2))
    .force("collide", d3.forceCollide().radius(25).strength(1)) // ป้องกันการซ้อนทับของโหนด
    
    .on("tick", () => {
      svg.value
        .selectAll("line")
        .attr("x1", (d) => d.source.x)
        .attr("y1", (d) => d.source.y)
        .attr("x2", (d) => d.target.x)
        .attr("y2", (d) => d.target.y);

      svg.value
        .selectAll(".node")
        .attr("cx", (d) => d.x)
        .attr("cy", (d) => d.y);
    });

  // ล้างข้อมูลเดิม
  force.value.nodes([]);
  force.value.force("link").links([]);

  // สร้างเส้น link
  const link = svg.value
    .selectAll("line")
    .data(graphData.links)
    .enter()
    .append("line")
    .attr("class", "link")
    .style("stroke", "#999")
    .attr("stroke-opacity", 0.6)
    .attr("stroke-width", (d) => Math.sqrt(d.value));

  // สร้างโหนด node
  const node = svg.value
    .selectAll(".node")
    .data(graphData.nodes)
    .enter()
    .append("circle")
    .attr("class", (d) => "node " + d.labels.join(" "))
    .attr("r", 15)
    .style("fill", (d) => {
      if (d.labels.includes("Author")) {
        return "red";
      } else if (d.labels.includes("Expertise")) {
        return "green";
      }else if (d.labels.includes("Expertises")) {
        return "blue";
      } else {
        return "gray";
      }
    })
    .call(
      d3
        .drag()
        .on("start", (event, d) => dragstarted(event, d))
        .on("drag", (event, d) => dragged(event, d))
        .on("end", (event, d) => dragended(event, d))
    ); // ทำให้โหนดเลื่อนได้

  // เพิ่มข้อมูลใหม่
  force.value.nodes(graphData.nodes);
  force.value.force("link").links(graphData.links);
  force.value.alpha(1).restart();

  console.log(graphData.nodes)
  console.log(graphData.links)

          // Set node title attribute
  node.append("title").text(function (d) {
            if (d.labels.includes("Author")) {
                var full_name = d.properties.full_name ?  d.properties.full_name : "-";
                var name_th = d.properties.name_th ?  d.properties.name_th : "-";
                var email =  d.properties.email ? d.properties.email : "-";
                var office = d.properties.office ? d.properties.office : "-";
                var province = d.properties.province ? d.properties.province : "-";
                var country = d.properties.country ? d.properties.country : "-";
                return  "ชื่อภาษาอังกฤษ:  " + full_name + "\n" +
                    "ชื่อภาษาไทย:  " + name_th + "\n" +
                    "อีเมล:  " + email + "\n" +
                    "สำนักงาน:  " + office + "\n" +
                    "จังหวัด:  " + province + "\n" +
                    "ประเทศ:  " + country;
            }else if (d.labels.includes("Expertise")){
                  return d.properties.expertise_name ? d.properties.expertise_name  : "-";       
            }else if (d.labels.includes("Expertises")){
                  return d.properties.expertise_name ? d.properties.expertise_name  : "-";       
            }else {
                  return JSON.stringify(d.properties, null).replace(/,/g, ",\n"); // (/,/g) ค้นหาทุกตัวอักษร , เพื่อแทนที่ด้วย , ตามด้วย \n
            }
            
          });
          
  };

  const resizeGraph = () => {
    if(force.value){

      force.value.force("center",d3.forceCenter(window.innerWidth / 2, window.innerHeight / 2)); // ปรับ force center ใหม่เมื่อหน้าจอถูกปรับขนาด
      
      svg.value
        .attr("width", window.innerWidth)
        .attr("height", window.innerHeight) // ปรับขนาด SVG
      force.value.restart(); // รีสตาร์ท force
    } 
  };
 
  const dragstarted = (event, d) => {
      if (!event.active) force.value.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
  };
  const dragged = (event, d) => {
      d.fx = event.x;
      d.fy = event.y;
  };
  const dragended = (event, d) => {
      if (!event.active) force.value.alphaTarget(0);
      d.fx = null;
      d.fy = null;
  };






</script>







// import axios from "axios";
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
//         // const articleNodes = ref({});
//         const nodeIconRedSrc = ref(nodeIconRed);
//         const nodeIconOrangeSrc = ref(nodeIconOrange);
//         const nodeIconGreenSrc = ref(nodeIconGreen);
//         const nodeIconBlueSrc = ref(nodeIconBlue);

//         return {
//             authorNodes,
//             // articleNodes,
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
//             const id_e = this.$route.params.id;
//             console.log(id_e);
//             if (!id_e) {
//                 console.error("id_author is undefined or null");
//                 return;
//             }

//             axios
//                 .get(`${import.meta.env.VITE_FASTAPI}/graph_data_expertise/${id_e}`, {
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

//                     // this.articleNodes.value = graphData.nodes.filter((node) =>
//                     //     node.labels.includes("Article")
//                     // );
//                     // console.log(this.articleNodes.value);

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
//                         var full_name = d.properties.full_name ?  d.properties.full_name : "-";
//                         var name_th = d.properties.name_th ?  d.properties.name_th : "-";
//                         var email =  d.properties.email ? d.properties.email : "-";
//                         var office = d.properties.office ? d.properties.office : "-";
//                         var province = d.properties.province ? d.properties.province : "-";
//                         var country = d.properties.country ? d.properties.country : "-";
//                         return  "ชื่อภาษาอังกฤษ:  " + full_name + "\n" +
//                                 "ชื่อภาษาไทย:  " + name_th + "\n" +
//                                 "อีเมล:  " + email + "\n" +
//                                 "สำนักงาน:  " + office + "\n" +
//                                 "จังหวัด:  " + province + "\n" +
//                                 "ประเทศ:  " + country;
//                         } else if (d.labels.includes("Article")) {
//                             var country = d.properties.title  ? d.properties.title  : "-" ;
//                             var publication_year = d.properties.publication_year  ? d.properties.publication_year  : "-" ;
//                             var publication_title = d.properties.publication_title  ? d.properties.publication_title  : "-" ;
//                             var content_type = d.properties.content_type  ? d.properties.content_type : "-" ;
//                             var doi = d.properties.doi  ? d.properties.doi : "-" ;
//                             var page = "";
//                             if(d.properties.start_page && d.properties.end_page){
//                             page = d.properties.start_page + " - " + d.properties.end_page;
//                             }
//                             else if(d.properties.start_page && d.properties.end_page == ""){
//                             page = d.properties.start_page;
//                             }
//                             else{
//                             page = "-";
//                             }
//                             return  "ชื่องานวิจัย:  " + country + "\n" +
//                                     "ปีที่เผยแพร่:  " + publication_year+ "\n" +
//                                     "ชื่อวารสารหรือบทความ:  " + publication_title + "\n" +
//                                     "ประเภทงานวิจัย:  " + content_type + "\n" +
//                                     "หมายเลขหน้า:  " + page + "\n" +
//                                     "doi:  " + doi ;
//                             } else if (d.labels.includes("Degree")){
//                                 return d.properties.degree_name ? d.properties.degree_name : "-";
//                             } else if (d.labels.includes("Expertise")){
//                             return d.properties.expertise_name ? d.properties.expertise_name  : "-";       
//                             } else {
//                             return JSON.stringify(d.properties, null).replace(/,/g, ",\n"); // (/,/g) ค้นหาทุกตัวอักษร , เพื่อแทนที่ด้วย , ตามด้วย \n
//                             }
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
//             const expertiseNodes = this.svg.selectAll(".node")
//                 .filter(d => d.labels.includes("Expertise")); // เลือกเฉพาะโหนดที่เป็น label "Article"

//             const expertiseNodeX = window.innerWidth / 2;
//             const expertiseNodeY = window.innerHeight / 2;
//             expertiseNodes.attr("cx", expertiseNodeX)
//                           .attr("cy", expertiseNodeY);

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
<!-- </script> -->
<style scoped>
body {
    margin: 0;
}

#graph {
    width: 90vw;
    height: 100vh;
}    
</style>