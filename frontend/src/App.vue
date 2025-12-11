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
/* Elegant white/silver gradient background with mesh and interactive hue */
.app-container {
  min-height: 100vh;
  width: 100%;
  position: relative;
  
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 25%, #e9ecef 50%, #f8f9fa 75%, #ffffff 100%);
  background-size: 500% 500%;
  background-attachment: fixed;
  animation: gradientShift 15s ease infinite;
}

/* Animated gradient shift for a living background */
@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Subtle mesh pattern overlay */
.app-container::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    repeating-linear-gradient(0deg, transparent, transparent 40px, rgba(139, 92, 246, 0.015) 40px, rgba(139, 92, 246, 0.015) 41px),
    repeating-linear-gradient(90deg, transparent, transparent 40px, rgba(139, 92, 246, 0.015) 40px, rgba(139, 92, 246, 0.015) 41px),
    radial-gradient(circle at 20% 30%, rgba(139, 92, 246, 0.03) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(192, 132, 252, 0.03) 0%, transparent 50%);
  pointer-events: none;
  z-index: 0;
}

/* Interactive hue change that follows the mouse */
.app-container::after {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(
    circle 600px at var(--mouse-x, 50%) var(--mouse-y, 50%),
    rgba(216, 180, 254, 0.12) 0%,
    rgba(192, 132, 252, 0.06) 30%,
    transparent 60%
  );
  pointer-events: none;
  z-index: 0;
  transition: opacity 0.3s ease;
}

/* Ensure content sits above the decorative overlays */
.app-container > * {
  position: relative;
  z-index: 1;
}
</style>

