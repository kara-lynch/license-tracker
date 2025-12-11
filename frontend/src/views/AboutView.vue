<script setup lang="ts">
import logo from '@/assets/salts_light.jpg'
import About from '@/components/About.vue';
import Taskbar from '@/components/Taskbar.vue';
</script>

<template>
  <Taskbar />
  <div class="about">
    <About />
  </div>
  <!-- simple, easy-to-edit inline logo placed top-right below header -->
  <img :src="logo" alt="S.A.L.T.S logo" 
  style="
  position:absolute; 
  top:220px; 
  right:20px; 
  width:200px; 
  height:auto;
  border: 4px solid rgba(139, 92, 246, 0.3);
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(139, 92, 246, 0.15), 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;" 
  />

</template>

<style>
</style>
