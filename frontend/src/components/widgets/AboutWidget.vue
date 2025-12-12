<script lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'AboutWidget',
  setup () {
    const aboutInput = ref<any[]>([])
    const error = ref<string | null>(null)
    const loading = ref(false)
    const expandedDevelopers = ref<Set<string>>(new Set())

    async function fetchAboutInput() {
      loading.value = true
      error.value = null
      
      // load token from env 
      const token = import.meta.env.VITE_JWT_TOKEN ?? ''

      try {
        console.log('Fetching licenses with token:', token)
        const res = await axios.get('http://localhost:5000/aboutUs/', {
          method: 'GET',
          headers: {
            Bearer: token,
            'Content-Type': 'application/json',
          },
        })
        const data = res.data
        if (Array.isArray(data)) {
          aboutInput.value = data
        } else if (data && typeof data === 'object') {
          // convert { "<id>": { ... } } -> [ { id: "<id>", ...fields }, ... ]
          aboutInput.value = Object.entries(data).map(([id, val]) => ({ id, ...(val as Record<string, any>) }))
        } else {
          aboutInput.value = []
        }
      } catch (e: any) {
        error.value =
          e?.response?.status === 401
            ? 'Unauthorized (401) — token missing or invalid.'
            : e?.response?.data?.message ?? e.message ?? 'Request failed'
      } finally {
        loading.value = false
      }
    }

    function toggleDeveloper(devKey: string) {
      if (expandedDevelopers.value.has(devKey)) {
        expandedDevelopers.value.delete(devKey)
      } else {
        expandedDevelopers.value.add(devKey)
      }
      // Force reactivity update
      expandedDevelopers.value = new Set(expandedDevelopers.value)
    }

    function isDeveloperExpanded(devKey: string) {
      return expandedDevelopers.value.has(devKey)
    }

    onMounted(() => {
      fetchAboutInput()
    })

    return { aboutInput, error, loading, fetchAboutInput, toggleDeveloper, isDeveloperExpanded }
  }
}
</script>

<template>
  <section class="about">
    <h1>We are S.A.L.T.S</h1>
    <div class="toolbar">
      <span class="status" v-if="loading">Loading…</span>
      <span class="error" v-if="error">{{ error }}</span>
    </div>
    <div v-for="(about, i) in aboutInput" :key="i">
      <p class="lead">{{ about.vision_statement || 'error' }}</p>

      <h2>Meet the Team</h2>

      <h4 @click="toggleDeveloper('dev1')" class="clickable">{{ about.developer1.name || 'error' }}</h4>
      <transition name="slide-fade">
        <div v-if="isDeveloperExpanded('dev1')" class="developer-info">
          <p class="title">{{ about.developer1.title || 'error' }}</p>
          <ul>
            <li>{{ about.developer1.bio || 'error' }}</li>
          </ul>
        </div>
      </transition>

      <h4 @click="toggleDeveloper('dev2')" class="clickable">{{ about.developer2.name || 'error' }}</h4>
      <transition name="slide-fade">
        <div v-if="isDeveloperExpanded('dev2')" class="developer-info">
          <p class="title">{{ about.developer2.title || 'error' }}</p>
          <ul>
            <li>{{ about.developer2.bio || 'error' }}</li>
          </ul>
        </div>
      </transition>

      <h4 @click="toggleDeveloper('dev3')" class="clickable">{{ about.developer3.name || 'error' }}</h4>
      <transition name="slide-fade">
        <div v-if="isDeveloperExpanded('dev3')" class="developer-info">
          <p class="title">{{ about.developer3.title || 'error' }}</p>
          <ul>
            <li>{{ about.developer3.bio || 'error' }}</li>
          </ul>
        </div>
      </transition>

      <h4 @click="toggleDeveloper('dev4')" class="clickable">{{ about.developer4.name || 'error' }}</h4>
      <transition name="slide-fade">
        <div v-if="isDeveloperExpanded('dev4')" class="developer-info">
          <p class="title">{{ about.developer4.title || 'error' }}</p>
          <ul>
            <li>{{ about.developer4.bio || 'error' }}</li>
          </ul>
        </div>
      </transition>

      <h4 @click="toggleDeveloper('dev5')" class="clickable">{{ about.developer5.name || 'error' }}</h4>
      <transition name="slide-fade">
        <div v-if="isDeveloperExpanded('dev5')" class="developer-info">
          <p class="title">{{ about.developer5.title || 'error' }}</p>
          <ul>
            <li>{{ about.developer5.bio || 'error' }}</li>
          </ul>
        </div>
      </transition>

      <h4 @click="toggleDeveloper('dev6')" class="clickable">{{ about.developer6.name || 'error' }}</h4>
      <transition name="slide-fade">
        <div v-if="isDeveloperExpanded('dev6')" class="developer-info">
          <p class="title">{{ about.developer6.title || 'error' }}</p>
          <ul>
            <li>{{ about.developer6.bio || 'error' }}</li>
          </ul>
        </div>
      </transition>

      <p class="copyright">{{ about.copyright || 'error' }}</p>
    </div>

    <p v-if="loading && !aboutInput.length" class="loading">Loading…</p>
  </section>
</template>

<style scoped>
.about {
  padding: 1.25rem;
}

.about > * {
  animation: fadeInDown 0.6s ease-out backwards;
}

.about > *:nth-child(1) { animation-delay: 0.1s; }
.about > *:nth-child(2) { animation-delay: 0.2s; }
.about > *:nth-child(3) { animation-delay: 0.3s; }
.about > *:nth-child(4) { animation-delay: 0.4s; }
.about > *:nth-child(5) { animation-delay: 0.5s; }
.about > *:nth-child(6) { animation-delay: 0.6s; }
.about > *:nth-child(7) { animation-delay: 0.7s; }
.about > *:nth-child(8) { animation-delay: 0.8s; }
.about > *:nth-child(9) { animation-delay: 0.9s; }
.about > *:nth-child(10) { animation-delay: 1s; }
.about > *:nth-child(11) { animation-delay: 1.1s; }
.about > *:nth-child(12) { animation-delay: 1.2s; }
.about > *:nth-child(13) { animation-delay: 1.3s; }
.about > *:nth-child(14) { animation-delay: 1.4s; }
.about > *:nth-child(15) { animation-delay: 1.5s; }

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

h4 {
  font-size: 1.35rem;
  font-weight: 600;
  color: #000;
  margin-top: 1.5rem;
  margin-bottom: 0.5rem;
  position: relative;
  padding-left: 1rem;
  letter-spacing: -0.2px;
}

h4.clickable {
  cursor: pointer;
  transition: color 0.3s ease;
}

h4.clickable:hover {
  color: rgba(139, 92, 246, 0.9);
}

h4::before {
  content: '▸';
  position: absolute;
  left: 0;
  color: rgba(139, 92, 246, 0.7);
  font-size: 1rem;
}

ul {
  margin-left: 1.1rem;
  color: #000;
  line-height: 1.8;
  font-weight: 400;
  margin-bottom: 1.5rem;
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

.title {
  text-decoration: underline;
  font-weight: 500;
}

.toolbar { 
  display: flex; 
  gap: 12px; 
  align-items: center; 
  margin-bottom: 12px;
  justify-content: flex-start;
}

.status { 
  color: rgba(15, 23, 42, 0.6);
  font-weight: 500;
}

.error { 
  color: #ef4444;
  font-weight: 500;
  padding: 1rem;
  background: rgba(239, 68, 68, 0.05);
  border-left: 3px solid #ef4444;
  border-radius: 4px;
}

.loading {
  text-align: left;
  color: rgba(15, 23, 42, 0.6);
  font-weight: 500;
  padding: 1rem;
}

.copyright {
  margin-top: 2rem;
  padding: 1rem;
  background: rgba(139, 92, 246, 0.05);
  border-left: 3px solid rgba(139, 92, 246, 0.6);
  border-radius: 4px;
  color: #000;
  font-weight: 500;
  text-align: left;
}

.developer-info {
  overflow: hidden;
}

/* Slide-fade transition */
.slide-fade-enter-active {
  transition: all 0.5s ease-out;
  max-height: 500px;
}

.slide-fade-leave-active {
  transition: all 0.4s ease-in;
  max-height: 500px;
}

.slide-fade-enter-from {
  transform: translateY(-20px);
  opacity: 0;
  max-height: 0;
}

.slide-fade-leave-to {
  transform: translateY(-20px);
  opacity: 0;
  max-height: 0;
}
</style>
