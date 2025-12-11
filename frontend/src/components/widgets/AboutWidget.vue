<script lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'AboutWidget',
  setup () {
    const aboutInput = ref<any[]>([])
    const error = ref<string | null>(null)
    const loading = ref(false)

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

    onMounted(() => {
      fetchAboutInput()
    })

    return { aboutInput, error, loading, fetchAboutInput }
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
    <li v-for="(about, i) in aboutInput" >
      <p class="lead">{{ about.vision_statement || 'error' }}</p>
      <br></br>
      <br></br>
      <h2>Meet the Team</h2>
      <br></br>
      <h4>{{ about.developer1.name || 'error' }}</h4>
      <p>{{ about.developer1.title || 'error' }}</p>
      <ul>
        <li>{{ about.developer1.bio || 'error' }}</li>
      </ul>
      <br></br>
      <h4>{{ about.developer2.name || 'error' }}</h4>
      <p>{{ about.developer2.title || 'error' }}</p>
      <ul>
        <li>{{ about.developer2.bio || 'error' }}</li>
      </ul>
      <br></br>
      <h4>{{ about.developer3.name || 'error' }}</h4>
      <p>{{ about.developer3.title || 'error' }}</p>
      <ul>
        <li>{{ about.developer3.bio || 'error' }}</li>
      </ul>
      <br></br>
      <h4>{{ about.developer4.name || 'error' }}</h4>
      <p>{{ about.developer4.title || 'error' }}</p>
      <ul>
        <li>{{ about.developer4.bio || 'error' }}</li>
      </ul>
      <br></br>
      <h4>{{ about.developer5.name || 'error' }}</h4>
      <p>{{ about.developer5.title || 'error' }}</p>
      <ul>
        <li>{{ about.developer5.bio || 'error' }}</li>
      </ul>
      <br></br>
      <h4>{{ about.developer6.name || 'error' }}</h4>
      <p>{{ about.developer6.title || 'error' }}</p>
      <ul>
        <li>{{ about.developer6.bio || 'error' }}</li>
      </ul>
      <br></br>
      <br></br>
      <p>{{ about.copyright || 'error' }}</p>
    </li>
    

    <p v-if="loading" class="loading">Loading…</p>
    <p v-if="error" class="error">{{ error }}</p>
  </section>
</template>

<style scoped>
.see-licenses { display:block }
.toolbar { display:flex; gap:12px; align-items:center; margin-bottom:12px }
.refresh { background:transparent; border:1px solid rgba(15,23,42,0.08); padding:6px 10px; border-radius:8px }
.status { color: rgba(15,23,42,0.6) }
.error { color:#ef4444 }

.license-list { list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:12px }
.license-card { background: var(--color-background-soft, #fff); border-radius:10px; padding:14px; box-shadow: 0 8px 18px rgba(15,23,42,0.04); border:1px solid rgba(15,23,42,0.04) }
.card-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:8px }
.title { font-weight:600; font-size:1rem }
.meta { font-size:0.85rem; color:rgba(15,23,42,0.55) }
.card-body { display:grid; grid-template-columns:repeat(2, 1fr); gap:8px; font-size:0.95rem }
.row { display:flex; gap:6px }
.label { color:rgba(15,23,42,0.6); min-width:70px }
.restrictions { grid-column: 1 / -1 }
.empty { color: rgba(15,23,42,0.6); padding:12px }


</style>
