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
      <li v-for="(license, i) in licenses" :key="license.id ?? i" class="license-card">
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
