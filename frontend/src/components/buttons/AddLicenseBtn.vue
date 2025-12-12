<!-- Spencer will work on this component -->

<script setup lang="ts">
import { ref } from 'vue';
import AddLicenseForm from '../forms/AddLicenseForm.vue';

const showFormFlag = ref(false);

function toggleBool() {
  showFormFlag.value = !showFormFlag.value;
}
</script>

<template>
    <button @click="toggleBool">Add</button>
    <div v-show="showFormFlag">
        <AddLicenseForm @close="toggleBool" />
    </div>
</template>