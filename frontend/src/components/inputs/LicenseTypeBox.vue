<script setup lang="ts">
import { ref } from 'vue';

const licenseTypes = [
    { value: 'Enterprise', label: 'Enterprise' },
    { value: 'Open Source', label: 'Open Source'},
    { value: 'Freeware', label: 'Freeware' },
    { value: 'Shareware', label: 'Shareware' },
];
    
const selectedLicense = ref(licenseTypes[0]);

function updateLicenseType() {
    selectedLicense.value = selectedLicense.value;
}

</script>

<template>
    <div class="license-type-input">
        <label id="license-type">License Type *</label>

        <div class="input-wrapper" >
            <span class="selected">{{ selectedLicense?.label }}</span>

            <select v-model="selectedLicense" @change="updateLicenseType">
                <option v-for="type in licenseTypes" :value="type">
                    {{ type.value }}
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