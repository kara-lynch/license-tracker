<script setup lang="ts">
import { ref } from 'vue';
import AssignLicenseForm from '../forms/AssignLicenseForm.vue';

const showFormFlag = ref(false);

function toggleBool() {
  showFormFlag.value = !showFormFlag.value;
}
</script>

<template>
    <button @click="toggleBool">Assign to Employee</button>
    <div v-show="showFormFlag">
        <AssignLicenseForm @close='toggleBool' />
    </div>
</template>