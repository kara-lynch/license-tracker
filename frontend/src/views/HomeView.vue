<script setup lang="ts">
import { RouterLink } from 'vue-router'
import logo from '@/assets/salts_light_trimmed.jpg'
import { ref } from 'vue'

const isShaking = ref(false)
const saltParticles = ref<Array<{ id: number; left: number }>>([])
let particleId = 0

const expandedFeature = ref<string | null>(null)

function toggleFeature(featureName: string) {
  if (expandedFeature.value === featureName) {
    expandedFeature.value = null
  } else {
    expandedFeature.value = featureName
  }
}

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
  <section class="home">
    <h1>Welcome to S.A.L.T.S</h1>

    <p class="lead">S.A.L.T.S helps your team track, assign and manage software licenses in one central place.</p>

    <h2>Getting started</h2>
    <ol>
      <li>Use the navigation at the top to move between pages.</li>
      <li>Click <RouterLink to="/view-licenses">View Licenses</RouterLink> to see all current licenses and try sorting them using the column controls.</li>
      <li>From the <em>View Licenses</em> page you can add a new license or delete an existing one using the buttons in the UI.</li>
      <li>Visit <RouterLink to="/assigned-to-me">Assigned to me</RouterLink> to see licenses specifically assigned to your account.</li>
      <li>For team information and contact details, visit the <RouterLink to="/about">About</RouterLink> page.</li>
    </ol>

    <h3>Features at a glance</h3>
    <ul>
      <li>View all licenses in database.</li>
      <li>Add new licenses (product, vendor, cost, renewal period, assignee).</li>
      <li>Delete licenses you no longer track.</li>
      <li>See license assignments.</li>
    </ul>

    <div class="feature-cards">
      <div class="feature-card" @click="toggleFeature('addDelete')">
        <h3 class="card-title">How to add or delete a license</h3>
        <div class="card-icon">
          <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <line x1="12" y1="5" x2="12" y2="19"/>
            <line x1="5" y1="12" x2="19" y2="12"/>
          </svg>
          <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <polyline points="3 6 5 6 21 6"/>
            <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
            <line x1="10" y1="11" x2="10" y2="17"/>
            <line x1="14" y1="11" x2="14" y2="17"/>
          </svg>
        </div>
        <transition name="expand">
          <p v-if="expandedFeature === 'addDelete'" class="card-content">
            From the <strong>View Licenses</strong> page click the <em>Add</em> button and fill out the form with the license details. To remove a license, select it and use the <em>Delete</em> action — most actions will prompt you to confirm before changing data.
          </p>
        </transition>
      </div>

      <div class="feature-card" @click="toggleFeature('sorting')">
        <h3 class="card-title">Sorting and searching</h3>
        <div class="card-icon">
          <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <circle cx="11" cy="11" r="8"/>
            <path d="m21 21-4.35-4.35"/>
          </svg>
          <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <line x1="12" y1="5" x2="12" y2="19"/>
            <polyline points="19 12 12 19 5 12"/>
            <polyline points="19 12 12 5 5 12"/>
          </svg>
        </div>
        <transition name="expand">
          <p v-if="expandedFeature === 'sorting'" class="card-content">
            Use the table headers or provided controls on the <strong>View Licenses</strong> page to sort by fields like cost, renewal date, or license type. Use the search or filter inputs to narrow results.
          </p>
        </transition>
      </div>

      <div class="feature-card" @click="toggleFeature('assigned')">
        <h3 class="card-title">Assigned Licenses</h3>
        <div class="card-icon">
          <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
            <circle cx="12" cy="7" r="4"/>
          </svg>
          <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
            <polyline points="14 2 14 8 20 8"/>
            <line x1="16" y1="13" x2="8" y2="13"/>
            <line x1="16" y1="17" x2="8" y2="17"/>
            <polyline points="10 9 9 9 8 9"/>
          </svg>
        </div>
        <transition name="expand">
          <p v-if="expandedFeature === 'assigned'" class="card-content">
            The <strong>Assigned Licenses</strong> page shows who licenses are assigned to. This makes it easy to find your responsibilities and upcoming renewals.
          </p>
        </transition>
      </div>
    </div>

    <h3>Quick actions</h3>
    <div class="actions">
      <RouterLink to="/view-licenses" class="btn">View Licenses</RouterLink>
      <RouterLink to="/assigned-to-me" class="btn">Assigned Licenses</RouterLink>
      <RouterLink to="/about" class="btn">About</RouterLink>
    </div>

    <h3>Tips & troubleshooting</h3>
    <ul>
      <li>If a page looks empty, make sure you are authenticated (some features may require login/permissions).</li>
      <li>Use the browser console or the backend logs for error details when an action fails.</li>
      <li>If sorting or filtering behaves unexpectedly, try refreshing the page — the app reads latest data from the API on load.</li>
    </ul>
    <h3>Permissions</h3>
    <ul>
      <li>Some actions like adding or deleting licenses may require specific user permissions. Ensure your account has the necessary rights.</li>
      <li>Contact your administrator if you encounter permission issues.</li>
    </ul>
    <p class="help">Questions or need help? Reach out to your project team via the About page or the repository maintainers.</p>
  </section>
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

<style scoped>
.home {
  padding: 1.25rem;
}

.home > * {
  animation: fadeInDown 0.6s ease-out backwards;
}

.home > *:nth-child(1) { animation-delay: 0.1s; }
.home > *:nth-child(2) { animation-delay: 0.2s; }
.home > *:nth-child(3) { animation-delay: 0.3s; }
.home > *:nth-child(4) { animation-delay: 0.4s; }
.home > *:nth-child(5) { animation-delay: 0.5s; }
.home > *:nth-child(6) { animation-delay: 0.6s; }
.home > *:nth-child(7) { animation-delay: 0.7s; }
.home > *:nth-child(8) { animation-delay: 0.8s; }
.home > *:nth-child(9) { animation-delay: 0.9s; }
.home > *:nth-child(10) { animation-delay: 1s; }
.home > *:nth-child(11) { animation-delay: 1.1s; }
.home > *:nth-child(12) { animation-delay: 1.2s; }
.home > *:nth-child(13) { animation-delay: 1.3s; }
.home > *:nth-child(14) { animation-delay: 1.4s; }
.home > *:nth-child(15) { animation-delay: 1.5s; }

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

h1 {
  font-size: 3rem;
  margin: 0 0 0.5rem 0;
  margin-left: calc(-50vw + 50%);
  margin-right: calc(-50vw + 50%);
  padding-left: calc(50vw - 50%);
  padding-right: calc(50vw - 50%);
  text-align: center;
  font-weight: 800;
  letter-spacing: 0.3em;
  font-family: 'Train One', 'Tahoma', 'Verdana', 'Geneva', sans-serif;
  text-transform: uppercase;
  color: #020202;
  position: relative;
  border-top: 3px solid rgba(0, 0, 0, 0.6);
  border-bottom: 3px solid rgba(0, 0, 0, 0.6);
  padding-top: 1rem;
  padding-bottom: 1rem;
  background: linear-gradient(90deg, 
    transparent 0%, 
    rgba(139, 92, 246, 0.03) 10%, 
    rgba(139, 92, 246, 0.05) 50%, 
    rgba(139, 92, 246, 0.03) 90%, 
    transparent 100%);
}

h1::before,
h1::after {
  content: '';
  position: absolute;
  width: 40px;
  height: 3px;
  background: linear-gradient(90deg, #8b5cf6, #a855f7);
}

h1::before {
  top: -3px;
  left: 50%;
  transform: translateX(-50%);
}

h1::after {
  bottom: -3px;
  left: 50%;
  transform: translateX(-50%);
}

.lead {
  text-align: left;
  color: #1a1a1a;
  margin-bottom: 2rem;
  margin-right: 240px;
  font-size: 1.35rem;
  font-weight: 500;
  letter-spacing: 0.3px;
}

h2 {
  margin-top: 2rem;
  font-size: 2rem;
  font-weight: 600;
  color: #000;
  border-left: 4px solid rgba(139, 92, 246, 0.6);
  padding-left: 1rem;
  letter-spacing: -0.3px;
}

h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #000;
  margin-top: 1.5rem;
  position: relative;
  padding-left: 1rem;
  letter-spacing: -0.2px;
}

h3::before {
  content: '▸';
  position: absolute;
  left: 0;
  color: rgba(139, 92, 246, 0.7);
  font-size: 1.2rem;
}

ol {
  margin-left: 1.1rem;
  color: #000;
  line-height: 1.8;
  font-weight: 400;
  font-size: 1.1rem;
}

ol li {
  margin-bottom: 0.5rem;
  padding-left: 0.5rem;
}

.actions {
  display: flex;
  gap: 0.75rem;
  margin: 1.5rem 0 2rem 0;
}

.btn {
  display: inline-block;
  padding: 0.7rem 1.2rem;
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.9), rgba(168, 85, 247, 0.9));
  color: #fff;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  letter-spacing: 0.3px;
  box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
  transition: all 0.3s ease;
  border: 1px solid rgba(139, 92, 246, 0.4);
}

.btn:hover {
  background: linear-gradient(135deg, rgba(168, 85, 247, 1), rgba(139, 92, 246, 1));
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(139, 92, 246, 0.4);
}

ul {
  margin-left: 1.1rem;
  color: #000;
  line-height: 1.8;
  font-weight: 400;
  font-size: 1.1rem;
}

ul li {
  margin-bottom: 0.5rem;
  padding-left: 0.5rem;
  position: relative;
}

ul li::marker {
  color: rgba(139, 92, 246, 0.7);
}

p {
  color: #000;
  line-height: 1.7;
  font-weight: 400;
  font-size: 1.1rem;
}

strong {
  font-weight: 700;
  color: #000;
}

em {
  font-style: italic;
  color: rgba(139, 92, 246, 0.9);
  font-weight: 500;
}

.help {
  margin-top: 2rem;
  padding: 1rem;
  background: rgba(139, 92, 246, 0.05);
  border-left: 3px solid rgba(139, 92, 246, 0.6);
  border-radius: 4px;
  color: #000;
  font-weight: 500;
}

.feature-cards {
  display: flex;
  gap: 1.5rem;
  margin: 2rem 0;
  justify-content: space-between;
}

.feature-card {
  flex: 1;
  min-height: 150px;
  padding: 1.5rem;
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(168, 85, 247, 0.15));
  border: 2px solid rgba(139, 92, 246, 0.3);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(139, 92, 246, 0.15);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(139, 92, 246, 0.25);
  border-color: rgba(139, 92, 246, 0.5);
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.25), rgba(168, 85, 247, 0.2));
}

.feature-card .card-title {
  margin: 0;
  padding: 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: rgba(139, 92, 246, 0.9);
}

.feature-card .card-title::before {
  content: '';
}

.feature-card .card-icon {
  margin-top: 0.75rem;
  display: flex;
  gap: 1rem;
  align-items: center;
  justify-content: center;
  opacity: 0.7;
  transition: all 0.3s ease;
  color: rgba(139, 92, 246, 0.9);
}

.feature-card .card-icon svg {
  transition: all 0.3s ease;
}

.feature-card:hover .card-icon {
  opacity: 1;
}

.feature-card:hover .card-icon svg {
  transform: scale(1.1);
}

.feature-card .card-content {
  margin-top: 1rem;
  font-size: 1rem;
  line-height: 1.6;
  text-align: left;
  color: #1a1a1a;
}

.expand-enter-active,
.expand-leave-active {
  transition: all 0.3s ease;
  max-height: 300px;
  overflow: hidden;
}

.expand-enter-from,
.expand-leave-to {
  opacity: 0;
  max-height: 0;
  margin-top: 0;
}

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

