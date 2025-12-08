<script setup lang="ts">
const emit = defineEmits<{
  (e: 'cancel'): void
}>()
</script>

<template>
    <!-- emit "cancel" when clicked; parent (form) will reset and close -->
    <button type="button" @click="emit('cancel')">Cancel</button>
</template>