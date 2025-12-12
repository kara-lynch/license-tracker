<script setup lang="ts">
import AssignLicense from '@/components/AssignLicense.vue'
import Taskbar from '@/components/Taskbar.vue';
</script> 

<template>
  <Taskbar />
  <AssignLicense />
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>