
<script lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'SeeLicenseWidget',
  setup () {
    const licenses = ref<any[]>(['No licenses found'])
    const error = ref<string | null>(null)
    const loading = ref(false)

    // hardcoded JWT for testing
    const token = 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBdXRoIFNlcnZpY2UiLCJsYXN0X25hbWUiOiJGaXNoYmllIiwibG9jYXRpb24iOiJKYXBhbiIsImlkIjo2NTgsImRlcGFydG1lbnQiOiJMZWdhbCIsInRpdGxlIjoiTWFuYWdlciIsImZpcnN0X25hbWUiOiJKb2xlZW4iLCJzdWIiOiJKb2xlZW4gRmlzaGJpZSIsImlhdCI6MTc2NTIzMTUzOCwiZXhwIjoxNzY1MjM1MTM4fQ.0tY3O-7-7memUGUf3FqcOftfqPP7xi0xHaGVJ09Mcbo'

    async function fetchLicenses() {
      loading.value = true
      error.value = null

      try {
        console.log('Fetching licenses with token:', token)
        const res = await axios.get('http://localhost:5000/seeLicenses/', {
          headers: {
            Bearer: token,
            'Content-Type': 'application/json',
          },
        })
        licenses.value = res.data
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
        <li v-for="(license, i) in licenses" :key="license.id">
          <div>License Name: {{ license.name }}</div>
          <div>License ID: {{ license.id }}</div>
          <div>Version: {{ license.version }}</div>
          <div>License Cost: {{ license.cost }}</div>
          <div>Currency: {{ license.curr }}</div>
          <div>License Type: {{ license.type }}</div>
          <div>Renewal Date: {{ license.date_of_renewal }}</div>
          <div>Expiration Date: {{ license.expiration_date }}</div>
          <div>Restrictions: {{ license.restrictions }}</div>
        </li>
    </ul>
  </div>
</template>
