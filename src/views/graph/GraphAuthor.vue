<template>
  <br><br><br>
  <p class="flex items-center text-xl" style="margin: 20px; ">ข้อมูลนักวิจัย</p> 
  <div class="overflow-x-auto border border-slate-900" style="margin: 20px; ">
    <table v-if="authorData&& authorData.length > 0"
      class="table table-md table-pin-rows table-pin-cols text-center ">
      <thead>
        <tr class="border-b border-black text-base text-white bg-gradient-to-r from-sky-500 to-indigo-500">
          <td>ชื่อภาษาอังกฤษ</td>
          <td>ชื่อภาษาไทย</td>
          <td>วุฒิการศึกษาสูงสุด</td>
          <td>สาขาที่เชี่ยวชาญ</td>
          <td>อีเมล</td>
          <td>สำนักงาน</td>
          <td>จังหวัด/เมือง</td>
          <td>ประเทศ</td>
          <td>IEEE URL</td>
          <td>เว็บไซต์</td>       
        </tr>
      </thead>
      <tbody>
        <tr  v-for="author in authorData" :key="author.id_author" class="text-sm">       
          <td class="border-r border-black text-left align-top" >
            <div class="w-44">{{ author.n.full_name ? author.n.full_name: "-"}}</div>
          </td>
          <td class="border-r border-black align-top" :style="{textAlign: author.n.name_th ? 'left' : 'center'}">
            <div class="w-44">{{ author.n.name_th ? author.n.name_th : "-" }}</div>
          </td>

          <td class="border-r border-black align-top" :style="{textAlign: author.degree.length > 0 ? 'left' : 'center'}">
            <template v-if="author.degree.length > 0">
              <template v-for="degree in author.degree" :key="degree.id" >
                <div class="w-52">
                  {{ "- " + (degree.degree_name ? degree.degree_name : "-") }} 
                  <br><br>
                </div>
              </template>
            </template>
            <template v-else>-</template>
          </td>
          <td class="border-r border-black align-top" :style="{textAlign: author.expertise.length > 0 ? 'left' : 'center'}">
            <template v-if = "author.expertise.length > 0">
              <template v-for="expertise in author.expertise" :key="expertise.id">
                <div class="w-44">{{"- " + (expertise.expertise_name ? expertise.expertise_name : "-") }} </div>
                <br>
              </template>
            </template>
            <template v-else>-</template>
          </td>
          <td class="border-r border-black align-top" :style="{ textAlign: author.n.email ? 'left' : 'center' }">
            {{ author.n.email ? author.n.email : "-" }}
          </td>
          <td class="border-r border-black align-top" :style="{ textAlign: author.n.office ? 'left' : 'center' }">
            <div class="w-44">{{ author.n.office ? author.n.office : "-" }}</div>
          </td>
          <td class="border-r border-black align-top" :style="{textAlign: author.n.province ? 'left' : 'center'}">
            <div class="w-28">{{ author.n.province ? author.n.province : "-" }}</div>
          </td>
          <td class="border-r border-black align-top" :style="{textAlign: author.n.country ? 'left' : 'center'}">
            <div class="w-24">{{ author.n.country ? author.n.country : "-" }}</div>
          </td>
          <td class="border-r border-black align-top" :style="{textAlign: author.n.authorUrl ? 'left' : 'center'}">
            <template v-if="author.n.authorUrl &&author.n.authorUrl !== '-'">
              <a :href="author.n.authorUrl" target="_blank" class="link link-primary">{{ author.n.authorUrl}}</a>
            </template>
            <template v-else>
              <span class="text-black">-</span>
            </template> 
            <!-- ใช้ :href และผูกค่ากับ author.properties.authorUrl ทำให้ลิงก์ทำงานได้โดยอัตโนมัติ-->
            <!-- เปิดลิงค์แท็บใหม่ target="_blank" -->
         </td>
          <td class="align-top" :style="{textAlign: author.n.website ? 'left' : 'center'}">
            <template v-if="author.n.website && author.n.website !== '-'">
              <a :href="author.n.website" target="_blank" class="link link-primary">{{author.n.website}}</a>
            </template>
            <template v-else>
              <span class="text-black">-</span>
            </template>
          </td>
        </tr>
      </tbody>
    </table>
  </div> 
  <!-- เป็นอาร์เรย์ของอ็อบเจกต์ ซึ่งอาจเป็นได้หลายคน ดังนั้นจำเป็นต้องใช้การเข้าถึงข้อมูลแต่ละตัวที่อยู่ในอาร์เรย์ -->
  <div class="flex items-center text-xl" style="margin: 20px; "> 
    <p v-for="author in authorData" :key="author.id">
      งานวิจัยของ {{ author.n.full_name }} 
    </p>
  </div>

  <div class="overflow-x-auto border border-slate-900" style="margin: 20px; ">
    <table v-if="authorData && authorData.length > 0" class="table table-md table-pin-rows table-pin-cols text-center table table-zebra">
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
          <td></td>
        </tr>
      </thead> 
      <tbody>
        <tr v-for="(article , index) in authorData[0].article" :key="index">
          <td class="border-r border-black text-left align-top" :style="{textAlign: article.title ? 'left' : 'center'}">
            <div class="w-72">{{article.title ? article.title : "-"}}</div>
          </td> 
          <td class="border-r border-black text-center align-top" :style="{textAlign: article.publication_year ? 'left' : 'center'}">
            {{article.publication_year ? article.publication_year : "-"}}
          </td> 
          <td class="border-r border-black text-left align-top" :style="{textAlign: article.publication_title ? 'left' : 'center'}">
            <div class="w-64">{{article.publication_title ? article.publication_title : "-"}}</div>
          </td> 
          <td class="border-r border-black text-left align-top" :style="{textAlign: article.article_number ? 'left' : 'center'}">
            {{article.article_number ? article.article_number: "-"}}
          </td>
          <td class="border-r border-black text-center align-top" :style="{textAlign: article.content_type ? 'left' : 'center'}">
            {{article.content_type ? article.content_type : "-"}}
          </td>  
          <td class="border-r border-black text-center align-top" :style="{textAlign: (article.start_page && article.end_page) ? 'left' : 'center'}">
            <div class="w-24">{{(article.start_page && article.end_page) ? article.start_page + ' - ' + article.end_page : "-"}}</div>
          </td> 
          <td class="border-r border-black text-center align-top" :style="{textAlign: article.doi ? 'left' : 'center'}">
            {{article.doi ? article.doi : "-"}}
          </td> 
          <td class="border-r border-black text-center align-top" :style="{textAlign: article.publisher ? 'left' : 'center'}">
            {{article.publisher ? article.publisher : "-"}}
          </td> 
          <td class="border-r border-black text-left align-top" :style="{textAlign: article.abstract_url ? 'left' : 'center'}">
            <template v-if="article.abstract_url &&article.abstract_url !== '-'">
              <a :href="article.abstract_url" target="_blank" class="link link-primary">{{article.abstract_url}}</a>
            </template>
            <template v-else>
              <span class="text-black">-</span>
            </template>
          </td> 
          <td class="align-top link link-info">
            <div class="w-14">
              <router-link :to="{ name: 'graph_research', params: { id:  article.id}}">
                  ดูเพิ่มเติม
              </router-link>
            </div>
          </td>
        </tr>
      </tbody> 
    </table>
  </div>
  <br>
  <div style="margin: 20px; ">
    <p class="flex items-center text-md" style="margin: 20px; ">
      <img :src="nodeIconPinkSrc" alt="Node Pink" class="h-6 w-6" />&nbsp;  = &nbsp; นักวิจัยที่ค้นหา &nbsp; , &nbsp;
      <img :src="nodeIconYellowSrc" alt="Node Yellow" class="h-6 w-6" />&nbsp;  = &nbsp; งานวิจัยของนักวิจัยที่ค้นหา &nbsp; , &nbsp;  
      <img :src="nodeIconGreenlightSrc" alt="Node Greenlight" class="h-6 w-6" />&nbsp;  = &nbsp; สาขาที่นักวิจัยที่ค้นหาเชี่ยวชาญ &nbsp; , &nbsp;
      <img :src="nodeIconRedSrc" alt="Node Red" class="h-6 w-6" />&nbsp;  = &nbsp; นักวิจัยที่มีความสัมพันธ์ &nbsp; , &nbsp;
      <img :src="nodeIconOrangeSrc" alt="Node Orange" class="h-6 w-6" />&nbsp;  = &nbsp; งานวิจัยที่มีความสัมพันธ์ &nbsp; , &nbsp;
      <img :src="nodeIconGreenSrc" alt="Node green" class="h-6 w-6" />&nbsp;  = &nbsp; สาขาที่เชี่ยวชาญที่มีความสัมพันธ์
    </p>
  </div>
  <!-- <div style="margin: 20px; ">
    
      <img :src="nodeIconPinkSrc" alt="Node Pink" class="h-6 w-6" />&nbsp;  = &nbsp; นักวิจัยที่ค้นหา <br>
      <img :src="nodeIconRedSrc" alt="Node Red" class="h-6 w-6" />&nbsp;  = &nbsp; นักวิจัยที่มีความสัมพันธ์ <br>
      <img :src="nodeIconYellowSrc" alt="Node Yellow" class="h-6 w-6" />&nbsp;  = &nbsp; งานวิจัยของนักวิจัยที่ค้นหา <br>
      <img :src="nodeIconOrangeSrc" alt="Node Orange" class="h-6 w-6" />&nbsp;  = &nbsp; งานวิจัยที่มีความสัมพันธ์ <br>
      <img :src="nodeIconGreenlightSrc" alt="Node Greenlight" class="h-6 w-6" />&nbsp;  = &nbsp; สาขาที่นักวิจัยที่ค้นหาเชี่ยวชาญ <br>
      <img :src="nodeIconGreenSrc" alt="Node green" class="h-6 w-6" />&nbsp;  = &nbsp; สาขาที่เชี่ยวชาญที่มีความสัมพันธ์
    
  </div> -->

  <div id="graph"></div>
</template>

<!-- <script>
import axios from "axios";
import * as d3 from "d3";
import { ref} from "vue";
import nodeIconRed from "@/assets/icon/red.png";
import nodeIconOrange from "@/assets/icon/orange.png";
import nodeIconGreen from "@/assets/icon/green.png";
import nodeIconBlue from "@/assets/icon/blue.jpg";

export default {
  data() {
    return {
      force: null,
      svg: null,
    };
  },
  setup() {
    const authorData = ref({});

    const nodeIconRedSrc = ref(nodeIconRed);
    const nodeIconOrangeSrc = ref(nodeIconOrange);
    const nodeIconGreenSrc = ref(nodeIconGreen);
    const nodeIconBlueSrc = ref(nodeIconBlue);

    return {
      authorData,
      nodeIconRedSrc,nodeIconOrangeSrc,nodeIconGreenSrc,nodeIconBlueSrc,
    };
  },
  mounted() {
    //สร้าง SVG container สำหรับกราฟ
    this.fetchData();
    this.fetchGraphData();

    this.svg = d3
      .select("#graph")
      .append("svg")
      .attr("width", "100%")
      .attr("height", "100%")
      .attr("pointer-events", "all");

    window.addEventListener("resize", this.resizeGraph); //ถูกเรียกเมื่อหน้าจอถูกปรับขนาด ซึ่งจะทำการปรับ force center และ SVG ใหม่.
    
  },
  methods: {
    fetchData(){
      const id_author = this.$route.params.id;
      if (!id_author) {
        console.error("id_author is undefined or null");
        return;
      }
      axios
        .get(`${import.meta.env.VITE_FASTAPI}/single_user/${id_author}`, {
          withCredentials: true,
        })
        .then((response) => {
          authorData.value = response.data;
          console.log(authorData.value);
        }
      )

    },

    fetchGraphData() {
      const id_author = this.$route.params.id;
      console.log(id_author);
      if (!id_author) {
        console.error("id_author is undefined or null");
        return;
      }
      

      axios
        .get(`${import.meta.env.VITE_FASTAPI}/graph_data_author/${id_author}`, {
          withCredentials: true,
        })
        .then((response) => {
          console.log(response.data);
          const graphData = response.data.graph_data;

          if (!graphData || !graphData.nodes || !graphData.links) {
            console.error("Graph data is missing or incomplete", graphData);
            return;
          }
          
          this.createGraph(graphData);
        })
           
        .catch((error) => {
          console.log("Error fetching graph data:", error);
        });
    },

    createGraph(graphData) {
      this.force = d3
            .forceSimulation(graphData.nodes)
            .force("charge", d3.forceManyBody().strength(-400))
            .force("link",d3.forceLink(graphData.links).id((d) => d.id).distance(150).strength(1))
            .force("center",d3.forceCenter(window.innerWidth / 2, window.innerHeight / 2).strength(0.1))
            .force("collide", d3.forceCollide().radius(20).strength(1)) // ป้องกันการซ้อนทับของโหนด
            .on("tick", () => {
              this.svg
                .selectAll("line")
                .attr("x1", (d) => d.source.x)
                .attr("y1", (d) => d.source.y)
                .attr("x2", (d) => d.target.x)
                .attr("y2", (d) => d.target.y);

              this.svg
                .selectAll(".node")
                .attr("cx", (d) => d.x)
                .attr("cy", (d) => d.y);
            });

          // ล้างข้อมูลเดิม
          this.force.nodes([]);
          this.force.force("link").links([]);

          // สร้างเส้น link
          const link = this.svg
            .selectAll("line")
            .data(graphData.links)
            .enter()
            .append("line")
            .attr("class", "link")
            .style("stroke", "#999")
            .attr("stroke-opacity", 0.6)
            .attr("stroke-width", (d) => Math.sqrt(d.value))
            
          // สร้างโหนด node
          const node = this.svg
            .selectAll(".node")
            .data(graphData.nodes)
            .enter()
            .append("circle")
            .attr("class", (d) => "node " + d.labels.join(" "))
            .attr("r", 20)
            .style("fill", (d) => {
              if (d.labels.includes("Author")) {
                //ตรวจสอบว่า Array นั้น ๆ มีค่าคืน true
                return "red";
              } else if (d.labels.includes("Article")) {
                return "orange";
              } else if (d.labels.includes("Degree")) {
                return "blue";
              } else if (d.labels.includes("Expertise")) {
                return "green";
              } else {
                return "gray";
              }
            })
            
            .call(
              d3
                .drag()
                .on("start", (event, d) => this.dragstarted(event, d))
                .on("drag", (event, d) => this.dragged(event, d))
                .on("end", (event, d) => this.dragended(event, d))
            ); // ทำให้โหนดเลื่อนได้
            

          // เพิ่มข้อมูลใหม่
          this.force
            .nodes(graphData.nodes)
            .force("link")
            .links(graphData.links);
          this.force.alpha(1).restart();

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
              } else if (d.labels.includes("Article")) {
                var country = d.properties.title  ? d.properties.title  : "-" ;
                var publication_year = d.properties.publication_year  ? d.properties.publication_year  : "-" ;
                var publication_title = d.properties.publication_title  ? d.properties.publication_title  : "-" ;
                var content_type = d.properties.content_type  ? d.properties.content_type : "-" ;
                var doi = d.properties.doi  ? d.properties.doi : "-" ;
                var page = "";
                if(d.properties.start_page && d.properties.end_page){
                  page = d.properties.start_page + " - " + d.properties.end_page;
                }
                else if(d.properties.start_page && d.properties.end_page == ""){
                  page = d.properties.start_page;
                }
                else{
                  page = "-";
                }
                return  "ชื่องานวิจัย:  " + country + "\n" +
                        "ปีที่เผยแพร่:  " + publication_year+ "\n" +
                        "ชื่อวารสารหรือบทความ:  " + publication_title + "\n" +
                        "ประเภทงานวิจัย:  " + content_type + "\n" +
                        "หน้าเลขหน้า:  " + page + "\n" +
                        "doi:  " + doi ;
                } else if (d.labels.includes("Degree")){
                    return d.properties.degree_name ? d.properties.degree_name : "-";
                } else if (d.labels.includes("Expertise")){
                  return d.properties.expertise_name ? d.properties.expertise_name  : "-";       
                } else {
                  return JSON.stringify(d.properties, null).replace(/,/g, ",\n"); // (/,/g) ค้นหาทุกตัวอักษร , เพื่อแทนที่ด้วย , ตามด้วย \n
                }
          });

          // Force simulation ticks อัปเดตตำแหน่งของลิงก์และโหนด
          // this.force.on("tick", () => {
          //   link
          //     .attr("x1", (d) => d.source.x)
          //     .attr("y1", (d) => d.source.y)
          //     .attr("x2", (d) => d.target.x)
          //     .attr("y2", (d) => d.target.y);

          //     node.attr("cx", (d) => d.x).attr("cy", (d) => d.y);
          // });
    },

    resizeGraph() {
      this.force.force(
        "center",
        d3.forceCenter(window.innerWidth / 2, window.innerHeight / 2)
      ); // ปรับ force center ใหม่เมื่อหน้าจอถูกปรับขนาด
      this.svg
        .attr("width", window.innerWidth)
        .attr("height", window.innerHeight); // ปรับขนาด SVG
      this.force.restart(); // รีสตาร์ท force
    },
    dragstarted(event, d) {
      if (!event.active) this.force.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    },
    dragged(event, d) {
      d.fx = event.x;
      d.fy = event.y;
    },
    dragended(event, d) {
      if (!event.active) this.force.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    },
  },
}; -->

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import * as d3 from "d3";
import nodeIconRed from "@/assets/icon/red.png";
import nodeIconOrange from "@/assets/icon/orange.png";
import nodeIconGreen from "@/assets/icon/green.png";
import nodeIconBlue from "@/assets/icon/blue.jpg";
import nodeIconPink from "@/assets/icon/pink.jpg";
import nodeIconYellow from "@/assets/icon/yellow.jpg";
import nodeIconGreenlight from "@/assets/icon/greenlight.jpg";
import {useRoute} from 'vue-router'

const force = ref(null);
const svg = ref(null);
const authorData = ref({});
const nodeIconRedSrc = ref(nodeIconRed);
const nodeIconOrangeSrc = ref(nodeIconOrange);
const nodeIconGreenSrc = ref(nodeIconGreen);
const nodeIconBlueSrc = ref(nodeIconBlue);
const nodeIconPinkSrc = ref(nodeIconPink);
const nodeIconYellowSrc = ref(nodeIconYellow);
const nodeIconGreenlightSrc = ref(nodeIconGreenlight);

const router = useRoute()

onMounted(() => {
  fetchData();
  
  svg.value = d3
    .select("#graph")
    .append("svg")
    .attr("width", window.innerWidth)
    .attr("height", window.innerHeight*1.5)
    .attr("pointer-events", "all")
    .append("g")
    .attr("transform", "scale(1)"); // ย่อขนาดกราฟ

  fetchGraphData();

  window.addEventListener("resize", resizeGraph);
});

const fetchData = () => {
  const id_author = router.params.id;
  if (!id_author) {
    console.error("id_author is undefined or null");
    return;
  }
  axios
    .get(`${import.meta.env.VITE_FASTAPI}/single_author_graph/${id_author}`, {
      withCredentials: true,
    })
    .then((response) => {
      authorData.value = response.data;
      console.log(authorData.value);
      
    });
};

const fetchGraphData = async () => {
  const id_author = router.params.id;
  console.log(id_author);
  if (!id_author) {
    console.error("id_author is undefined or null");
    return;
  }

  // // ตรวจสอบข้อมูลที่แคชไว้ใน LocalStorage
  // const cachedData = localStorage.getItem(`graph_data_${id_author}`);
  // if (cachedData) {
  //   const graphData = JSON.parse(cachedData);
  //   if (svg.value) {
  //     createGraph(graphData);
  //   } else {
  //     console.error("svg.value is not defined");
  //   }
  //   return;
  // }


  // ดึงข้อมูลจาก API
  try {
    const response = await axios.get(`${import.meta.env.VITE_FASTAPI}/graph_data_author/${id_author}`, {
      withCredentials: true,
    });
    const graphData = response.data.graph_data;
    console.log(graphData)
    if (!graphData || !graphData.nodes || !graphData.links) {
      console.error("Graph data is missing or incomplete", graphData);
      return;
    }

    // // แคชข้อมูลที่ได้รับใน LocalStorage
    // localStorage.setItem(`graph_data_${id_author}`, JSON.stringify(graphData));

    if (svg.value) {
      createGraph(graphData);
    } else {
      console.error("svg.value is not defined");
    }
  } catch (error) {
    console.log("Error fetching graph data:", error);
  }
};


const createGraph = (graphData) => {
  if (!svg.value) {
    console.error("svg.value is not defined");
    return;
  }
  force.value = d3
    .forceSimulation(graphData.nodes)
    .force("charge", d3.forceManyBody().strength(-300))
    .force("link",d3.forceLink(graphData.links).id((d) => d.id).distance(60).strength(0.7))
    .force("center",d3.forceCenter(window.innerWidth / 2, window.innerHeight/1.3))
    .force("collide", d3.forceCollide().radius(30).strength(1)) // ป้องกันการซ้อนทับของโหนด
    
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
    // .attr("r", 15)
    .attr("r", (d) => {
    // กำหนดขนาดตามเงื่อนไข
    if (d.labels.includes("Author")) {
      return 15; // ขนาดใหญ่ขึ้นสำหรับ Author
    } else if (d.labels.includes("Authors")) {
      return 22; // ขนาดใหญ่ขึ้นสำหรับ Authors
    } else if (d.labels.includes("Articles")) {
      return 22; // ขนาดใหญ่ขึ้นสำหรับ Articles
    } else if (d.labels.includes("Article")) {
      return 15; // ขนาดใหญ่ขึ้นสำหรับ Article
    } else if (d.labels.includes("Expertises")) {
      return 22; // ขนาดใหญ่ขึ้นสำหรับ Expertises
    } else if (d.labels.includes("Expertise")) {
      return 15; // ขนาดใหญ่ขึ้นสำหรับ Expertise
    } else {
      return 15; // ขนาดเริ่มต้นสำหรับโหนดอื่น ๆ
    }
  })
    .style("fill", (d) => {
      if (d.labels.includes("Author")) {
        return "red";
      }else if (d.labels.includes("Authors")) {
        return "#FF00FF";
      }else if (d.labels.includes("Articles")) {
        return "#FFF40B";
      }else if (d.labels.includes("Article")) {
        return "orange";
      } else if (d.labels.includes("Expertises")) {
        return "#00FF00";
      }else if (d.labels.includes("Expertise")) {
        return "green";
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
          } else if (d.labels.includes("Authors")){
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
          } else if (d.labels.includes("Article")) {
                var country = d.properties.title  ? d.properties.title  : "-" ;
                var publication_year = d.properties.publication_year  ? d.properties.publication_year  : "-" ;
                var publication_title = d.properties.publication_title  ? d.properties.publication_title  : "-" ;
                var content_type = d.properties.content_type  ? d.properties.content_type : "-" ;
                var doi = d.properties.doi  ? d.properties.doi : "-" ;
                var page = "";
                if(d.properties.start_page && d.properties.end_page){
                  page = d.properties.start_page + " - " + d.properties.end_page;
                }
                else if(d.properties.start_page && d.properties.end_page == ""){
                  page = d.properties.start_page;
                }
                else{
                  page = "-";
                }
                return  "ชื่องานวิจัย:  " + country + "\n" +
                        "ปีที่เผยแพร่:  " + publication_year+ "\n" +
                        "ชื่อวารสารหรือบทความ:  " + publication_title + "\n" +
                        "ประเภทงานวิจัย:  " + content_type + "\n" +
                        "หน้าเลขหน้า:  " + page + "\n" +
                        "doi:  " + doi ;
                }else if (d.labels.includes("Articles")) {
                var country = d.properties.title  ? d.properties.title  : "-" ;
                var publication_year = d.properties.publication_year  ? d.properties.publication_year  : "-" ;
                var publication_title = d.properties.publication_title  ? d.properties.publication_title  : "-" ;
                var content_type = d.properties.content_type  ? d.properties.content_type : "-" ;
                var doi = d.properties.doi  ? d.properties.doi : "-" ;
                var page = "";
                if(d.properties.start_page && d.properties.end_page){
                  page = d.properties.start_page + " - " + d.properties.end_page;
                }
                else if(d.properties.start_page && d.properties.end_page == ""){
                  page = d.properties.start_page;
                }
                else{
                  page = "-";
                }
                return  "ชื่องานวิจัย:  " + country + "\n" +
                        "ปีที่เผยแพร่:  " + publication_year+ "\n" +
                        "ชื่อวารสารหรือบทความ:  " + publication_title + "\n" +
                        "ประเภทงานวิจัย:  " + content_type + "\n" +
                        "หน้าเลขหน้า:  " + page + "\n" +
                        "doi:  " + doi ;
                } else if (d.labels.includes("Expertise")){
                  return d.properties.expertise_name ? d.properties.expertise_name  : "-";       
                }else if (d.labels.includes("Expertises")){
                  return d.properties.expertise_name ? d.properties.expertise_name  : "-";       
                } else {
                  return JSON.stringify(d.properties, null).replace(/,/g, ",\n"); // (/,/g) ค้นหาทุกตัวอักษร , เพื่อแทนที่ด้วย , ตามด้วย \n
                }
          });
          
  };

  const resizeGraph = () => {
    if(force.value){

      force.value.force("center",d3.forceCenter(window.innerWidth / 2, window.innerHeight/1.3)); // ปรับ force center ใหม่เมื่อหน้าจอถูกปรับขนาด
      
      svg.value
        .attr("width", window.innerWidth)
        .attr("height", window.innerHeight*2) // ปรับขนาด SVG
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

<style scoped>
body {
  margin: 0;
  
}

#graph {
  width: 90vw;
  height: 100vh;
}



</style> 
