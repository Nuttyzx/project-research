<template>
  <Navbar/>
  <!-- <Breadcrumb /> -->
  <div>
    <router-view />
  </div>
</template>

<script setup>
  import Navbar from './components/Navbar.vue';
  import Breadcrumb from './components/Breadcrumb.vue';
</script>

<style lang="scss" scoped>

</style>