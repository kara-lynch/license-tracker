<script setup lang="ts">
import { ref } from 'vue';

const renewalPeriodTypes = [
    { value: 'Weekly', label: 'Weekly' },
    { value: 'Montly', label: 'Montly' },
    { value: 'Quarterly', label: 'Quarterly'},
    { value: 'Bi-Annually', label: 'Bi-Annually' },
    { value: 'Annually', label: 'Annually' },
];
    
const selectedRenewalPeriod = ref(renewalPeriodTypes[0]);

function updateLicenseType() {
    selectedRenewalPeriod.value = selectedRenewalPeriod.value;
}

</script>

<template>
    <div class="license-renewal-period">
        <label id="license-renewal-period">Renewal Period</label>

        <div class="input-wrapper" >
            <span class="selected">{{ selectedRenewalPeriod?.label }}</span>

            <select v-model="selectedRenewalPeriod" @change="updateLicenseType">
                <option v-for="rp in renewalPeriodTypes" :value="rp">
                    {{ rp.value }}
                </option>
                
            </select>
        </div>
    </div>
</template>

<style scoped>
.input-wrapper {
    border: 1px solid rgb(0, 0, 0); 
    padding: 10px;
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    margin-top: 5px;
    margin-bottom: 15px;
}
.selected {
  margin-right: 10px;
}
</style>