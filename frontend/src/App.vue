<script setup lang="ts">
import Taskbar from './components/Taskbar.vue'
import logo from './assets/salts_light.jpg'
import { ref, onMounted, onUnmounted } from 'vue'

const mouseX = ref(50)
const mouseY = ref(50)

function handleMouseMove(e: MouseEvent) {
  mouseX.value = (e.clientX / window.innerWidth) * 100
  mouseY.value = (e.clientY / window.innerHeight) * 100
}

onMounted(() => {
  window.addEventListener('mousemove', handleMouseMove)
})

onUnmounted(() => {
  window.removeEventListener('mousemove', handleMouseMove)
})
</script>

<template>
  <div 
    class="app-container"
    :style="{
      '--mouse-x': mouseX + '%',
      '--mouse-y': mouseY + '%'
    }"
  >
    <header>
      <div class="wrapper">
        <Taskbar />
      </div>
    </header>

    <!-- simple, easy-to-edit inline logo placed top-right below header -->
    <!-- <img :src="logo" alt="S.A.L.T.S logo" 
    style="
    position:absolute; 
    top:140px; 
    right:20px; 
    width:200px; 
    height:auto;" 
    /> -->

    <RouterView />
  </div>
</template>

<style>
/* Simple solid background with honeycomb pattern */
.app-container {
  min-height: 100vh;
  width: 100%;
  position: relative;
  
  background: #f8f9fa;
}

/* Honeycomb pattern overlay */
.app-container::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    /* Honeycomb hexagon pattern - more visible */
    repeating-linear-gradient(60deg, transparent, transparent 20px, rgba(139, 92, 246, 0.15) 20px, rgba(139, 92, 246, 0.15) 21px),
    repeating-linear-gradient(120deg, transparent, transparent 20px, rgba(139, 92, 246, 0.15) 20px, rgba(139, 92, 246, 0.15) 21px),
    repeating-linear-gradient(0deg, transparent, transparent 20px, rgba(139, 92, 246, 0.15) 20px, rgba(139, 92, 246, 0.15) 21px);
  background-size: 
    35px 60px,
    35px 60px,
    35px 60px;
  background-position:
    0 0,
    0 0,
    0 0;
  pointer-events: none;
  z-index: 0;
}

/* Ensure content sits above the decorative overlays */
.app-container > * {
  position: relative;
  z-index: 1;
}
</style>

