<template>
    
        <div style="margin: 40px; ">
            <div v-if="authorName.length > 0" class="overflow-x-auto">
                <table class="table table-pin-rows table table-zebra ">
                    <thead>
                        <tr  class="text-center text-base text-white bg-gradient-to-r from-sky-500 to-indigo-500">
                            <th></th>
                            <th>ชื่อภาษาอังกฤษ</th>
                            <th>ชื่อภาษาไทย</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(author_name, index) in authorName" :key="index" class="hover text-base">
                            <th>{{ index + 1 }}</th>
                            <!-- <td>
                                <template v-if="author_name.n.full_name ">
                                    <router-link :to="{ name: 'graph_author', params: { id: author_name.n.id}}">
                                    <span class="hoverable">{{ author_name.n.full_name }}</span>
                                </router-link>
                                </template>
                                <template v-else>
                                    <span>-</span>
                                </template>
                            </td>
                            <td >
                                <template v-if="author_name.n.name_th">
                                    <router-link :to="{ name: 'graph_author', params: { id: author_name.n.id}}">
                                    <span class="hoverable">{{ author_name.n.name_th }}</span>
                                    </router-link>
                                </template>
                                <template v-else>
                                    <span>-</span>
                                </template>
                            </td> -->
                            <td>
                                <template v-if="author_name.n.full_name ">
                                    <router-link :to="{ name: 'graph_author', params: { id: author_name.id}}">
                                    <span class="hoverable">{{ author_name.n.full_name }}</span>
                                </router-link>
                                </template>
                                <template v-else>
                                    <span>-</span>
                                </template>
                            </td>
                            <td >
                                <template v-if="author_name.n.name_th">
                                    <router-link :to="{ name: 'graph_author', params: { id: author_name.id}}">
                                    <span class="hoverable">{{ author_name.n.name_th }}</span>
                                    </router-link>
                                </template>
                                <template v-else>
                                    <span>-</span>
                                </template>
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

// const authorName = computed(() => store.state.authorName); // เรียกใช้ state ที่ถูกจัดเก็บ
// console.log(authorName)
</script>
<style >
.hoverable:hover {
    color: blue; /* เปลี่ยนสีเป็นสีฟ้า */
    text-decoration: underline; /* เพิ่มขีดเส้นใต้ */
    cursor: pointer; /* เปลี่ยนรูปแบบของ cursor เมื่อวางเม้าส์ที่ element */
} 
/* .underline-white {
    text-decoration: underline;
    text-decoration-color: white;
} */

span {
    color: black; /* กำหนดสีข้อความเป็นสีดำ */
}
</style>