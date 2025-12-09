<script setup lang="ts">
import { ref } from 'vue'
import FormSubmitBtn from '../buttons/FormSubmitBtn.vue';
import FormCancelBtn from '../buttons/FormCancelBtn.vue';
import axios from 'axios';

// allow emitting a "close" event to the parent
const emit = defineEmits<{
  (e: 'close'): void
}>()

const formRef = ref<HTMLFormElement | null>(null)
const lID = ref<number | null>(null)
const token = import.meta.env.VITE_JWT_TOKEN ?? ''
const responseText = ref<any | null>(null)

function handleCancel() {
  // reset native form fields
  if (formRef.value) formRef.value.reset()
  // notify parent to close the form
  emit('close')
}

async function sendDelete(e: Event){
  e.preventDefault()
  if (!formRef.value) return 

  const formData = new FormData(formRef.value)
  const data: Record<string, any> = {
        licenseID: parseInt(String(formData.get('licenseID'))) || ''
  }
  /*
  axios.delete("http://localhost:5000/deleteLicense/", {
    headers: {
        Bearer: token,
        'Content-Type': 'application/json',
    },
    data: {
        "licenseID": lID.value
    }
  })
  .catch(function(error){
    console.log(error)
  });
  */

  try {
    const res = await fetch('http://localhost:5000/deleteLicense/', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        Bearer: token,
      },
      body: JSON.stringify(data)
    })

    // On success reset + close; otherwise log
    if (res.ok) {
      console.log('License deleted succesfully')
      if (formRef.value) formRef.value.reset()
      emit('close')
    } else {
      console.error('Delete license failed', res.status, await res.text())
    }
  } catch (err) {
    console.error('Network error', err)
  }

  if (formRef.value) formRef.value.reset()
}
</script>

<template>
    <!-- add ref so we can reset the form programmatically -->
    <form class="form-wrapper" ref="formRef" @submit="sendDelete">
        <div class="form-content">
            <label id="required-fields">Please fill out all required fields *</label>

            
                <div class="field-block">
                    <label id="license-id">license ID</label>
                        <input v-model="lID" class="input-box" name="licenseID" />
                </div>

                <div style="display:flex;gap:8px;align-items:center">
                  <FormSubmitBtn />
                  <!-- Cancel button resets the form and closes it via handleCancel -->
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