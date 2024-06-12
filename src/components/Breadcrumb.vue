<!-- <template>
  <nav class="breadcrumb bg-Slate-50" aria-label="breadcrumbs">
    <ul>
      <li v-for="(crumb, index) in crumbs" :key="index">
        <router-link :to="crumb.to">{{ crumb.label }}</router-link>
      </li>
    </ul>
  </nav>
</template> -->
<!--   
<script>
export default {
  computed: {
    crumbs() {
      const route = this.$route;
      const matched = route.matched; -->

      // เพิ่ม breadcrumb สำหรับ Home
      <!-- const crumbs = [{ label: 'Home', to: '/' }]; -->

      // เพิ่ม breadcrumb สำหรับแต่ละเส้นทางที่ตรงกัน
      <!-- for (let i = 0; i < matched.length; i++) {
        const match = matched[i];
        const label = match.meta && match.meta.breadcrumb ? match.meta.breadcrumb : match.name;
        const to = match.path;
        crumbs.push({ label, to });
      }

      return crumbs;
      
    }
  },
   -->
<!-- 

};
</script>
  
<style>
.breadcrumb {
  background-color: #f4f4f4;
  padding: 10px;
  padding-left: 50px;
  margin-bottom: 10px;
}

.breadcrumb ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

.breadcrumb li {
  display: inline;
  margin-right: 5px;
  position: relative;
  /* เพิ่มบรรทัดนี้เพื่อทำให้สามารถใส่เส้นใต้ได้ */
}

.breadcrumb li::after {
  content: '>';
  margin-left: 5px;
  margin-right: 5px;
}

.breadcrumb li:hover {
  color: blue;
  /* สีตัวหนังสือเมื่อ hover */
  text-decoration: underline;
  /* เส้นใต้เมื่อ hover */

}</style>
   -->
<template>
  
</template>
<script>

</script>