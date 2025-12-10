<script lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'SeeAssignmentsWidget',
  setup () {
    const assignments = ref<any[]>([])
    const error = ref<string | null>(null)
    const loading = ref(false)

    async function fetchAssignments() {
      loading.value = true
      error.value = null
      
      // load token from env 
      const token = import.meta.env.VITE_JWT_TOKEN ?? ''

      try {
        console.log('Fetching licenses with token:', token)
        const res = await axios.get('http://localhost:5000/seeAllAssignments/', {
          method: 'GET',
          headers: {
            Bearer: token,
            'Content-Type': 'application/json',
          },
        })
        const data = res.data
        if (Array.isArray(data)) {
          assignments.value = data
        } else if (data && typeof data === 'object') {
          // convert { "<id>": { ... } } -> [ { id: "<id>", ...fields }, ... ]
          assignments.value = Object.entries(data).map(([id, val]) => ({ id, ...(val as Record<string, any>) }))
        } else {
          assignments.value = []
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
      fetchAssignments()
    })

    return { assignments, error, loading, fetchAssignments }
  }
}
</script>

<template>
  <div>
    <button @click="fetchAssignments">Refresh</button>

    <p v-if="loading">Loading…</p>
    <p v-if="error" style="color: red">{{ error }}</p>

    <ul v-else>
        <li v-for="(assignment, i) in assignments" :key="assignment.id ?? i">
          <div> {{ assignment.id }} </div>
          <div>Employee ID: {{ assignment.employeeID }}</div>
          <div>License ID: {{ assignment.licenseID }}</div>
          <div>Assigner ID: {{ assignment.assignerID }}</div>
        </li>
    </ul>
  </div>
</template>
