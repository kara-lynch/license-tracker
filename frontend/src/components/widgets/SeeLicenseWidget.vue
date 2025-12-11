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
      const token = document.cookie

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
  <div>
    <button @click="fetchLicenses">Refresh</button>

    <p v-if="loading">Loading…</p>
    <p v-if="error" style="color: red">{{ error }}</p>

    <ul v-else>
        <li v-for="(license, i) in licenses" :key="license.id ?? i">
          <div> {{ license.name }} </div>
          <div>License ID: {{ license.id }}</div>
          <div>License Type: {{ license.type }}</div>
          <div>Version: {{ license.ver }}</div>
          <div>License Cost: {{ license.cost }}</div>
          <div>Currency: {{ license.curr }}</div>
          <div>Renewal Date: {{ license.date_of_renewal }}</div>
          <div>Expiration Date: {{ license.expiration_date }}</div>
          <div>Restrictions: {{ license.restrictions }}</div>
        </li>
    </ul>
  </div>
</template>
