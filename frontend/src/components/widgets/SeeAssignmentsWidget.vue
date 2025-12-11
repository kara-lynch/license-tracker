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
  <div class="see-assignments">
    <div class="toolbar">
      <button class="refresh" @click="fetchAssignments">Refresh</button>
      <span class="status" v-if="loading">Loading…</span>
      <span class="error" v-if="error">{{ error }}</span>
    </div>

    <ul class="assignment-list" v-if="!loading && !error">
      <li v-if="assignments.length === 0" class="empty">No assignments found.</li>
      <li v-for="(assignment, i) in assignments" :key="assignment.id ?? i" class="assignment-card">
        <div class="card-header">
          <div class="title">{{ assignment.first_name || 'Unknown Employee' }}</div>
          <div class="meta">EID: {{ assignment.employeeID ?? '—' }}</div>
        </div>

        <div class="card-body">
          <div class="row"><span class="label">License Name:</span> <span>{{ assignment.licenseName || '—' }}</span></div>
          <div class="row"><span class="label">License ID:</span> <span>{{ assignment.licenseID || '—' }}</span></div>
          <div class="row"><span class="label">Assigner ID:</span> <span>{{ assignment.assignerID || '—' }}</span></div>
        </div>
      </li>
    </ul>

    <p v-if="loading" class="loading">Loading…</p>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<style scoped>
.see-assignments { display:block }

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

.assignment-list { 
  list-style: none; 
  padding: 0; 
  margin: 0; 
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 20px;
}

.assignment-card { 
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.18), rgba(168, 85, 247, 0.12));
  border-radius: 12px;
  padding: 18px;
  box-shadow: 0 8px 24px rgba(139, 92, 246, 0.15), 0 2px 8px rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(139, 92, 246, 0.2);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.assignment-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background: linear-gradient(90deg, rgba(139, 92, 246, 0.8), rgba(168, 85, 247, 0.8));
}

.assignment-card:hover {
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
  min-width: 100px;
  font-weight: 600;
  letter-spacing: 0.2px;
}

.row span:not(.label) {
  color: #000;
  font-weight: 400;
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
