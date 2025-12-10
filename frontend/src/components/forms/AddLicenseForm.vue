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
        name: String(formData.get('name')) || '',
        ver: String(formData.get('ver')) || '',
        type: String(formData.get('type')) || '',
        expiration_date: formData.get('expiration_date') || '',
        restrictions: String(formData.get('restrictions')) || '',

        cost: parseFloat(String(formData.get('cost'))) || parseFloat('0'),
        curr: String(formData.get('curr')) || '',
        period: String(formData.get('period')) || '',
        date_of_renewal: formData.get('date_of_renewal') || '',
    } // data object to hold formData
   
    try {
    const res = await fetch('http://localhost:5000/addLicense/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Bearer: token,
      },
      body: JSON.stringify(data),
    })

    // On success reset + close; otherwise log
    if (res.ok) {
      console.log('License added successfully:', String(data.name), String(data.ver), String(data.type), String(data.expiration_date), String(data.restrictions))
      if (formRef.value) formRef.value.reset()
      emit('close')
    } else {
      console.error('Add license failed', res.status, await res.text())
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
                    <label id="license-name">License Name *</label>
                        <input class="input-box" name="name" required/>
                </div>

                <div class="field-block">
                    <label id="license-version">License version *</label>
                        <input class="input-box" name="ver" required/>
                </div>

                 <div class="field-block">
                    <label id="license-type">License Type *</label>
                        <input class="input-box" name="type" required/>
                </div>

                <div class="field-block">
                    <label id="license-expiration-date">Expiration Date</label>
                        <input type="date" class="input-box" name="expiration_date" />
                </div> 

                <div class="field-block">
                    <label id="license-geographical-restrictions">Geographical Restrictions</label>
                        <input class="input-box" name="restrictions" />
                </div>

                <!-- vv HOLY SHIT ITS FINALLY WORKING vv-->

                <div class="field-block">
                    <label id="license-cost">License Cost</label>
                        <input class="input-box" name="cost"/>
                </div>

                <div class="field-block">
                    <label id="license-curr">Currency</label>
                        <input class="input-box" name="curr"/>
                </div>

                <div class="field-block">
                    <label id="license-period">Period</label>
                        <input class="input-box" name="period"/>
                </div> 

                <div class="field-block">
                    <label id="license-renewal-date">Renewal Date</label>
                        <input type="date" class="input-box" name="date_of_renewal" />
                </div>

                <!-- <LicenseTypeBox />

                <CostInputBox />

                <RenewalPeriodBox /> 

                --> 

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