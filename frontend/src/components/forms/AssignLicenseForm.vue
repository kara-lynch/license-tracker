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
    const res = await fetch('http://localhost:5000/employeeAssign/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Bearer: token,
      },
      body: JSON.stringify(data),
    })

    // On success reset + close; otherwise log
    if (res.ok) {
      console.log('License assigned successfully:', String(data.licenseID), String(data.employeeID))
      if (formRef.value) formRef.value.reset()
      emit('close')
    } else {
      console.error('Assign license failed', res.status, await res.text())
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
    display: flex;
    flex-direction: column;
    width: 400px;
    margin: 0 auto;
    border-color: black;
    border-width: 1px;
    border-style: solid;
    padding: 20px;
}
.input-box {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    margin-top: 5px;
    margin-bottom: 15px;
}
</style>