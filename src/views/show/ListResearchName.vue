<template>
    
        <div style="margin: 40px; ">
            <div v-if="researchName.length > 0" class="overflow-x-auto">
                <table class="table table-pin-rows table table-zebra">
                    <thead>
                        <tr class="text-center text-base text-white bg-gradient-to-r from-sky-500 to-indigo-500">
                            <th></th>
                            <th>ชื่องานวิจัย</th>
                            <th>ปีที่เผยแพร่</th>
                            <th>ประเภทงานวิจัย</th>
                        </tr>
                    </thead>
                    <!-- <tbody>
                        <tr v-for="(research_name, index) in researchName" :key="index" class="hover text-base">
                            <th>{{ index + 1 }}</th>
                            <td><router-link
                                    :to="{ name: 'graph_research', params: { id: research_name.n.article_number } }">
                                        <span class="hoverable underline-white">{{ research_name.n.title }}</span>
                                </router-link>
                            </td>
                            <td><router-link
                                    :to="{ name: 'graph_research', params: { id: research_name.n.article_number } }">
                                        <span class="hoverable underline-white">{{ research_name.n.publication_year }}</span>
                                </router-link>
                            </td>
                            <td><router-link
                                    :to="{ name: 'graph_research', params: { id: research_name.n.article_number } }">
                                        <span class="hoverable underline-white">{{ research_name.n.content_type }}</span>
                                </router-link>
                            </td>
                        </tr>
                    </tbody> -->
                    <tbody>
                        <tr v-for="(research_name, index) in researchName" :key="index" class="hover text-base">
                            <th>{{ index + 1 }}</th>
                            <td><router-link
                                    :to="{ name: 'graph_research', params: { id: research_name.id} }">
                                        <span class="hoverable underline-white">{{ research_name.n.title }}</span>
                                </router-link>
                            </td>
                            <td><router-link
                                    :to="{ name: 'graph_research', params: { id: research_name.id} }">
                                        <span class="hoverable underline-white">{{ research_name.n.publication_year }}</span>
                                </router-link>
                            </td>
                            <td><router-link
                                    :to="{ name: 'graph_research', params: { id: research_name.id} }">
                                        <span class="hoverable underline-white">{{ research_name.n.content_type }}</span>
                                </router-link>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div v-else class="text-center mt-8">
                <p class="text-lg">ไม่พบข้อมูล</p>
            </div>
        </div>
    
</template>
<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex'; // เพิ่ม import

const store = useStore(); // เพิ่มนี้เพื่อให้เรียกใช้ store

const researchName = computed(() => store.state.researchName); // เรียกใช้ state ที่ถูกจัดเก็บ


</script>
<style>
 .hoverable:hover {
    color: blue; /* เปลี่ยนสีเป็นสีฟ้า */
    text-decoration: underline; /* เพิ่มขีดเส้นใต้ */
    cursor: pointer; /* เปลี่ยนรูปแบบของ cursor เมื่อวางเม้าส์ที่ element */
}
span {
    color: black; /* กำหนดสีข้อความเป็นสีดำ */
}
   
</style>