<script lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'SeeLicenseWidget',
  setup () {
    const licenses = ref<any[]>([])
    const error = ref<string | null>(null)
    const loading = ref(false)

    async function fetchLicenses() {
      loading.value = true
      error.value = null
      
      // load token from env 
      const token = import.meta.env.VITE_JWT_TOKEN ?? ''

      try {
        console.log('Fetching licenses with token:', token)
        const res = await axios.get('http://localhost:5000/seeLicenses/', {
          method: 'GET',
          headers: {
            Bearer: token,
            'Content-Type': 'application/json',
          },
        })
        const data = res.data
        if (Array.isArray(data)) {
          licenses.value = data
        } else if (data && typeof data === 'object') {
          // convert { "<id>": { ... } } -> [ { id: "<id>", ...fields }, ... ]
          licenses.value = Object.entries(data).map(([id, val]) => ({ id, ...(val as Record<string, any>) }))
        } else {
          licenses.value = []
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
      fetchLicenses()
    })

    return { licenses, error, loading, fetchLicenses }
  }
}
</script>

<template>
  <div class="see-licenses">
    <div class="toolbar">
      <button class="refresh" @click="fetchLicenses">Refresh</button>
      <span class="status" v-if="loading">Loading…</span>
      <span class="error" v-if="error">{{ error }}</span>
    </div>

    <ul class="license-list" v-if="!loading && !error">
      <li v-if="licenses.length === 0" class="empty">No licenses found.</li>
      <li v-for="(license, i) in licenses" 
          :key="license.id ?? i" 
          class="license-card"
          :style="{ animationDelay: `${i * 0.1}s` }">
        <div class="card-header">
          <div class="title">{{ license.name || 'Untitled License' }}</div>
          <div class="meta">ID: {{ license.id ?? '—' }}</div>
        </div>

        <div class="card-body">
          <div class="row"><span class="label">Type:</span> <span>{{ license.type || '—' }}</span></div>
          <div class="row"><span class="label">Version:</span> <span>{{ license.ver || '—' }}</span></div>
          <div class="row"><span class="label">Cost:</span> <span>{{ license.cost ?? '—' }} {{ license.curr || '' }}</span></div>
          <div class="row"><span class="label">Renewal:</span> <span>{{ license.date_of_renewal || '—' }}</span></div>
          <div class="row"><span class="label">Expiration:</span> <span>{{ license.expiration_date || '—' }}</span></div>
          <div class="row restrictions"><span class="label">Restrictions:</span> <span>{{ license.restrictions || 'None' }}</span></div>
        </div>
      </li>
    </ul>

    <p v-if="loading" class="loading">Loading…</p>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<style scoped>
.see-licenses { display:block }

.toolbar { 
  display:flex; 
  gap:12px; 
  align-items:center; 
  margin-bottom:20px;
  padding-bottom: 12px;
  border-bottom: 2px solid rgba(139, 92, 246, 0.15);
}

.refresh { 
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.9), rgba(168, 85, 247, 0.9));
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
  transition: all 0.3s ease;
  letter-spacing: 0.3px;
  margin-top: 6px;
  margin-left: 20px;
  animation: fadeInDown 0.6s ease-out;
}

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.refresh:hover {
  background: linear-gradient(135deg, rgba(168, 85, 247, 1), rgba(139, 92, 246, 1));
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(139, 92, 246, 0.4);
}

.status { 
  color: #000;
  font-weight: 500;
  font-size: 0.95rem;
}

.error { 
  color: #ef4444;
  font-weight: 500;
}

.license-list { 
  list-style: none; 
  padding: 0; 
  margin: 0; 
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 20px;
}

.license-card { 
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.18), rgba(168, 85, 247, 0.12));
  border-radius: 12px;
  padding: 18px;
  box-shadow: 0 8px 24px rgba(139, 92, 246, 0.15), 0 2px 8px rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(139, 92, 246, 0.2);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  animation: slideInUp 0.6s ease-out backwards;
}

@keyframes slideInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.license-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background: linear-gradient(90deg, rgba(139, 92, 246, 0.8), rgba(168, 85, 247, 0.8));
}

.license-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(139, 92, 246, 0.25), 0 4px 12px rgba(0, 0, 0, 0.08);
  border-color: rgba(139, 92, 246, 0.4);
}

.card-header { 
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(139, 92, 246, 0.15);
}

.title { 
  font-weight: 700;
  font-size: 1.1rem;
  color: #000;
  letter-spacing: -0.2px;
}

.meta { 
  font-size: 0.85rem;
  color: rgba(139, 92, 246, 0.8);
  font-weight: 600;
  background: rgba(139, 92, 246, 0.1);
  padding: 4px 10px;
  border-radius: 6px;
  letter-spacing: 0.3px;
}

.card-body { 
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  font-size: 0.95rem;
}

.row { 
  display: flex;
  gap: 8px;
  align-items: flex-start;
}

.label { 
  color: rgba(139, 92, 246, 0.9);
  min-width: 85px;
  font-weight: 600;
  letter-spacing: 0.2px;
}

.row span:not(.label) {
  color: #000;
  font-weight: 400;
}

.restrictions { 
  grid-column: 1 / -1;
  padding-top: 8px;
  border-top: 1px solid rgba(139, 92, 246, 0.1);
}

.empty { 
  color: #000;
  padding: 20px;
  text-align: center;
  font-weight: 500;
  grid-column: 1 / -1;
}

.loading {
  text-align: center;
  color: #000;
  font-weight: 500;
  padding: 20px;
}
</style>
