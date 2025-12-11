<script setup lang="ts">
import { ref } from 'vue'
import CostInputBox from '../inputs/CostInputBox.vue';
import LicenseTypeBox from '../inputs/LicenseTypeBox.vue';
import RenewalPeriodBox from '../inputs/RenewalPeriodBox.vue';
import FormSubmitBtn from '../buttons/FormSubmitBtn.vue';
import FormCancelBtn from '../buttons/FormCancelBtn.vue';
import { parse } from 'vue/compiler-sfc';

// allow emitting a "close" event to the parent
const emit = defineEmits<{
  (e: 'close'): void
}>()

const formRef = ref<HTMLFormElement | null>(null)
const token = import.meta.env.VITE_JWT_TOKEN ?? ''

function handleCancel() {
  if (formRef.value) formRef.value.reset()
  emit('close')
}
async function handleSubmit(e: Event) {
    e.preventDefault()
    if (!formRef.value) return 

    const formData = new FormData(formRef.value)
    const data: Record<string, any> = {
        licenseID: parseInt(String(formData.get('licenseID'))) || '',
        employeeID: parseInt(String(formData.get('employeeID'))) || '',
    } // data object to hold formData
   
    try {
    const res = await fetch('http://localhost:5000/employeeUnassign/', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        Bearer: token,
      },
      body: JSON.stringify(data),
    })

    // On success reset + close; otherwise log
    if (res.ok) {
      console.log('License unassigned successfully:', String(data.licenseID), String(data.employeeID))
      if (formRef.value) formRef.value.reset()
      emit('close')
    } else {
      console.error('unassign license failed', res.status, await res.text())
    }
  } catch (err) {
    console.error('Network error', err)
  }
}
</script>

<template>
    <form class="form-wrapper" ref="formRef" @submit="handleSubmit">
        <div class="form-content">
            <label id="required-fields">Please fill out all required fields *</label>

                <div class="field-block">
                    <label id="license-id">License ID *</label>
                        <input class="input-box" name="licenseID" required/>
                </div>

                <div class="field-block">
                    <label id="employeeID">Employee ID *</label>
                        <input class="input-box" name="employeeID" required/>
                </div>

                <div style="display:flex;gap:8px;align-items:center">
                  <FormSubmitBtn />
                  <FormCancelBtn @cancel="handleCancel" />
                </div>
        </div>
    </form>
</template>

<style scoped>
.form-wrapper {
    position: fixed;
    top: 5vh;
    left: 50%;
    transform: translateX(-50%);
    width: 450px;
    max-width: 90vw;
    max-height: 90vh;
    overflow-y: auto;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(248, 249, 250, 0.95));
    backdrop-filter: blur(12px);
    border: 2px solid rgba(139, 92, 246, 0.3);
    border-radius: 16px;
    padding: 32px;
    box-shadow: 0 20px 60px rgba(139, 92, 246, 0.3), 0 8px 24px rgba(0, 0, 0, 0.15);
    z-index: 100;
}

.form-wrapper::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, rgba(139, 92, 246, 0.9), rgba(168, 85, 247, 0.9));
  border-radius: 16px 16px 0 0;
}

.form-content {
  position: relative;
}

#required-fields {
  display: block;
  font-size: 0.9rem;
  color: rgba(139, 92, 246, 0.9);
  font-weight: 600;
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 2px solid rgba(139, 92, 246, 0.15);
  letter-spacing: 0.3px;
}

.field-block {
  margin-bottom: 20px;
}

.field-block label {
  display: block;
  font-weight: 600;
  color: #000;
  margin-bottom: 8px;
  font-size: 0.95rem;
  letter-spacing: 0.2px;
}

.input-box {
    width: 100%;
    padding: 12px 16px;
    box-sizing: border-box;
    border: 2px solid rgba(139, 92, 246, 0.2);
    border-radius: 8px;
    font-size: 0.95rem;
    background: rgba(255, 255, 255, 0.8);
    transition: all 0.3s ease;
    color: #000;
    font-weight: 400;
}

.input-box:focus {
  outline: none;
  border-color: rgba(139, 92, 246, 0.6);
  background: rgba(255, 255, 255, 1);
  box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1);
}

.input-box::placeholder {
  color: rgba(0, 0, 0, 0.4);
}
</style>