<script setup lang="ts">
import logo from '@/assets/salts_light_trimmed.jpg'
import About from '@/components/About.vue';
import { ref } from 'vue'

const isShaking = ref(false)
const saltParticles = ref<Array<{ id: number; left: number }>>([])
let particleId = 0

function handleLogoClick() {
  // Trigger shake animation
  isShaking.value = true
  setTimeout(() => {
    isShaking.value = false
  }, 500)

  // Create salt particles
  const numParticles = 15
  for (let i = 0; i < numParticles; i++) {
    const particle = {
      id: particleId++,
      left: Math.random() * 180 + 10 // Random position within logo width
    }
    saltParticles.value.push(particle)
    
    // Remove particle after animation
    setTimeout(() => {
      saltParticles.value = saltParticles.value.filter(p => p.id !== particle.id)
    }, 3000)
  }
}
</script>

<template>
  <div class="about">
    <About />
  </div>
  <!-- simple, easy-to-edit inline logo placed top-right below header -->
  <div class="logo-container">
    <img :src="logo" alt="S.A.L.T.S logo" 
    :class="{ 'shake': isShaking }"
    @click="handleLogoClick"
    class="logo-img" 
    />
    <div 
      v-for="particle in saltParticles" 
      :key="particle.id"
      class="salt-particle"
      :style="{ left: particle.left + 'px' }"
    ></div>
  </div>

</template>

<style>
.logo-container {
  position: absolute;
  top: 220px;
  right: 20px;
  width: 200px;
  height: 200px;
  z-index: 10;
}

.logo-img {
  width: 200px;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(139, 92, 246, 0.15), 0 2px 8px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  object-fit: cover;
  object-position: center;
  transition: all 0.3s ease;
}

.logo-img:hover {
  transform: scale(1.05);
  box-shadow: 0 12px 40px rgba(139, 92, 246, 0.25), 0 4px 12px rgba(0, 0, 0, 0.15);
}

.logo-img.shake {
  animation: shake 0.5s ease-in-out;
}

@keyframes shake {
  0%, 100% { transform: translateX(0) rotate(0deg); }
  10% { transform: translateX(-10px) rotate(-5deg); }
  20% { transform: translateX(10px) rotate(5deg); }
  30% { transform: translateX(-10px) rotate(-5deg); }
  40% { transform: translateX(10px) rotate(5deg); }
  50% { transform: translateX(-10px) rotate(-5deg); }
  60% { transform: translateX(10px) rotate(5deg); }
  70% { transform: translateX(-10px) rotate(-5deg); }
  80% { transform: translateX(10px) rotate(5deg); }
  90% { transform: translateX(-10px) rotate(-5deg); }
}

.salt-particle {
  position: absolute;
  top: 180px;
  width: 4px;
  height: 4px;
  background: white;
  border-radius: 50%;
  box-shadow: 0 0 3px rgba(255, 255, 255, 0.8);
  animation: fall 3s ease-in forwards;
  pointer-events: none;
}

@keyframes fall {
  0% {
    transform: translateY(0) rotate(0deg);
    opacity: 1;
  }
  100% {
    transform: translateY(500px) rotate(720deg);
    opacity: 0;
  }
}
</style>
