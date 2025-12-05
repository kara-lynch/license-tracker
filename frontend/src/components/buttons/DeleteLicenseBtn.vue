<script setup lang="ts">
import { ref } from 'vue';
import DeleteLicenseForm from '../forms/DeleteLicenseForm.vue';

const showFormFlag = ref(false);

function toggleBool() {
  showFormFlag.value = !showFormFlag.value;
}
</script>

<template>
    <button @click="toggleBool">Delete License</button>
    <div v-show="showFormFlag">
        <DeleteLicenseForm />
    </div>
</template>