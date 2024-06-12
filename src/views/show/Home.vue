
<template>
    <div>
        <div class="hero image-background items-center">
            <div class="hero-overlay bg-opacity-15 "></div>
            <div class="hero-content text-center text-neutral-content">
                <div class="max-w-md">
                    <h1 class="mb-5 text-6xl font-bold ">ยินดีต้อนรับ</h1>
                    <p class="mb-5 text-xl">เว็บไซต์ที่ช่วยให้คุณสามารถค้นหา เพื่อแสดงข้อมูลและกราฟที่มีความสัมพันธ์ระหว่างนักวิจัยและงานวิจัย</p>
                    <router-link to="/search" >
                        <button class="btn btn-warning rounded-none">เริ่มใช้งาน</button>
                    </router-link>
                    
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>

</script>

<style scoped>
.image-background {
    /* ส่วนขยายรูปภาพ */
    background-size: cover;
    /* จัดกลุ่มรูปภาพให้อยู่ตรงกลาง */
    background-position: center;
    /* ตัดรูปภาพที่เกินขอบออก */
    overflow: hidden;
    /* ทำให้ภาพเต็มขนาด */
    height: 89vh;
    background-image: url("@/assets/images/background_home.jpg");
}

/* .navbar {
    background-color: (rgba(13, 5, 241, 0.882)); */
    /* background: linear-gradient(rgba(31, 4, 233, 0.336), rgba(194, 177, 177, 0.456)), url("@/assets/images/background_home.jpg"); */
    /* สีดำโปร่งใส */
    /* เปลี่ยนรูปแบบการใส่ภาพและสีดำโปร่งใสตามความต้องการ */
    /* background-size: cover;
    background-position: center;
    background-blend-mode: overlay;
} */

</style>
