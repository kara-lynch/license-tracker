<!-- Spencer will work on this component -->

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const apiBase = 'http://localhost:5000'
const token = ref<string>(localStorage.getItem('api_token') || '')
const licenses = ref<any[]>([])
const loading = ref(false)
const error = ref<string | null>(null)

function saveToken() {
  localStorage.setItem('api_token', token.value || '')
}

async function fetchLicenses() {
  loading.value = true
  error.value = null
  licenses.value = []

  try {
    const headers: Record<string, string> = { 'Content-Type': 'application/json' }
    if (token.value) headers['Bearer'] = token.value

    const res = await fetch(`${apiBase}/seeLicenses/`, { headers })
    if (res.status === 401) {
      error.value = 'Unauthorized (401) — token missing or invalid.'
      return
    }
    if (!res.ok) {
      error.value = `Request failed: ${res.status} ${res.statusText}`
      return
    }

    const data = await res.json()
    if (Array.isArray(data)) {
      licenses.value = data
    } else if (data && typeof data === 'object') {
      licenses.value = Object.keys(data).map(k => ({ id: k, ...(data as any)[k] }))
    } else {
      error.value = 'Unexpected response shape'
    }
  } catch (e: any) {
    error.value = e.message || String(e)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  // try auto-fetch if a token is already present
  if (token.value) fetchLicenses()
})
</script>

<template>
  <main style="padding:1rem; max-width:900px;">
    <div style="margin-bottom:1rem;">
      <label style="display:block;margin-bottom:.5rem;">Paste mock SSO token (optional):</label>
      <input v-model="token" placeholder="Paste token here" style="width:100%;max-width:600px;padding:.4rem" />
      <div style="margin-top:.5rem;">
        <button @click="saveToken" style="margin-right:.5rem;">Save token</button>
        <button @click="fetchLicenses" :disabled="loading">{{ loading ? 'Loading…' : 'Refresh licenses' }}</button>
      </div>
      <div style="font-size:0.85rem;color:#666;margin-top:.5rem;">
        Token is stored in localStorage under "api_token" for convenience.
      </div>
    </div>

    <div v-if="error" style="color:#b00020;margin-bottom:1rem">{{ error }}</div>

    <ul v-if="licenses.length" style="list-style:none;padding:0;">
      <li v-for="lic in licenses">{{ lic.curr }}</li>
      <li v-for="lic in licenses" :key="lic.id || lic.name || JSON.stringify(lic)" style="margin-bottom:1rem;padding:0.5rem;border:1px solid #eee;">
        <div style="font-weight:600">{{ lic.name || lic.id }}</div>
        <div v-if="lic.version">Version: {{ lic.version }}</div>
        <div v-if="lic.type">Type: {{ lic.type }}</div>
        <div v-if="lic.cost">Cost: {{ lic.cost }}</div>
        <div v-if="lic.expiration">Expiration: {{ lic.expiration }}</div>
      </li>
    </ul>

    <div v-else-if="!loading && !error">No licenses found.</div>
  </main>
</template>