<script setup lang="ts">
import Taskbar from './components/Taskbar.vue'
import logo from './assets/salts_light.jpg'
</script>

<template>
  <header>
    <div class="wrapper">
      <Taskbar />
    </div>
  </header>

  <!-- simple, easy-to-edit inline logo placed top-right below header -->
  <img :src="logo" alt="S.A.L.T.S logo" 
  style="
  position:absolute; 
  top:140px; 
  right:20px; 
  width:240px; 
  height:auto;" 
  />

  <RouterView />
</template>

