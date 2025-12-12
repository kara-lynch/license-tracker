<script setup lang="ts">
import Taskbar from './components/Taskbar.vue'
import logo from './assets/salts_light.jpg'
import { ref, onMounted, onUnmounted } from 'vue'

const mouseX = ref(50)
const mouseY = ref(50)

const volt1X = ref(0)
const volt1Y = ref(0)
const volt1Angle = ref(0)
const volt1Key = ref(0)

const volt2X = ref(0)
const volt2Y = ref(0)
const volt2Angle = ref(0)
const volt2Key = ref(0)

const volt3X = ref(0)
const volt3Y = ref(0)
const volt3Angle = ref(0)
const volt3Key = ref(0)

function handleMouseMove(e: MouseEvent) {
  mouseX.value = (e.clientX / window.innerWidth) * 100
  mouseY.value = (e.clientY / window.innerHeight) * 100
}

function animateVolt1() {
  const angles = [0, 60, 120]
  const randomAngle = angles[Math.floor(Math.random() * angles.length)]
  volt1Angle.value = randomAngle ?? 0
  volt1X.value = Math.random() * 100
  volt1Y.value = Math.random() * 100
  volt1Key.value++
  setTimeout(animateVolt1, 4000 + Math.random() * 2000)
}

function animateVolt2() {
  const angles = [0, 60, 120]
  const randomAngle = angles[Math.floor(Math.random() * angles.length)]
  volt2Angle.value = randomAngle ?? 0
  volt2X.value = Math.random() * 100
  volt2Y.value = Math.random() * 100
  volt2Key.value++
  setTimeout(animateVolt2, 4000 + Math.random() * 2000)
}

function animateVolt3() {
  const angles = [0, 60, 120]
  const randomAngle = angles[Math.floor(Math.random() * angles.length)]
  volt3Angle.value = randomAngle ?? 0
  volt3X.value = Math.random() * 100
  volt3Y.value = Math.random() * 100
  volt3Key.value++
  setTimeout(animateVolt3, 4000 + Math.random() * 2000)
}

onMounted(() => {
  window.addEventListener('mousemove', handleMouseMove)
  animateVolt1()
  setTimeout(animateVolt2, 1000) // Start second volt after 1 second
  setTimeout(animateVolt3, 2000) // Start third volt after 2 seconds
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

    <!-- three traveling volt effects -->
    <div 
      :key="volt1Key"
      class="volt"
      :style="{
        left: volt1X + '%',
        top: volt1Y + '%',
        '--volt-angle': volt1Angle + 'deg'
      }"
    ></div>

    <div 
      :key="volt2Key"
      class="volt"
      :style="{
        left: volt2X + '%',
        top: volt2Y + '%',
        '--volt-angle': volt2Angle + 'deg'
      }"
    ></div>

    <div 
      :key="volt3Key"
      class="volt"
      :style="{
        left: volt3X + '%',
        top: volt3Y + '%',
        '--volt-angle': volt3Angle + 'deg'
      }"
    ></div>

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
  
  background: #e4e1e1;
  overflow: hidden;
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
    /* Honeycomb hexagon pattern - lighter opacity */
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

/* Single traveling volt */
.volt {
  position: fixed;
  width: 150px;
  height: 3px;
  background: linear-gradient(90deg, 
    transparent 0%,
    rgba(139, 92, 246, 0.3) 20%,
    rgba(168, 85, 247, 0.9) 40%,
    rgba(168, 85, 247, 1) 50%,
    rgba(168, 85, 247, 0.9) 60%,
    rgba(139, 92, 246, 0.3) 80%,
    transparent 100%);
  box-shadow: 
    0 0 10px rgba(168, 85, 247, 0.8),
    0 0 20px rgba(168, 85, 247, 0.5),
    0 0 30px rgba(168, 85, 247, 0.3);
  pointer-events: none;
  z-index: 0;
  animation: voltTravel 2s linear forwards;
  transform-origin: left center;
  will-change: transform, opacity;
  opacity: 0;
}

@keyframes voltTravel {
  0% {
    opacity: 0;
    transform: rotate(var(--volt-angle)) translateX(-150px) scale(0.8);
  }
  15% {
    opacity: 1;
    transform: rotate(var(--volt-angle)) translateX(0) scale(1);
  }
  85% {
    opacity: 1;
    transform: rotate(var(--volt-angle)) translateX(1200px) scale(1);
  }
  100% {
    opacity: 0;
    transform: rotate(var(--volt-angle)) translateX(1350px) scale(0.8);
  }
}

/* Ensure content sits above the decorative overlays */
header {
  position: relative;
  z-index: 10;
}

main,
section,
div[class*="widget"],
div[class*="about"] {
  position: relative;
  z-index: 5;
}

.volt {
  z-index: 0 !important;
}
</style>

