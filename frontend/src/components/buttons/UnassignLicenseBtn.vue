<script setup lang="ts">
import { ref } from 'vue';
import UnassignLicenseForm from '../forms/UnassignLicenseForm.vue';

const showFormFlag = ref(false);

function toggleBool() {
  showFormFlag.value = !showFormFlag.value;
}
</script>

<template>
    <button @click="toggleBool">Unassign from Employee</button>
    <div v-show="showFormFlag">
        <UnassignLicenseForm @close='toggleBool'/>
    </div>
</template>