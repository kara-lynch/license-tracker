<script setup lang="ts">
    const emit = defineEmits<{
    (e: 'submit'): void
}>()
</script>

<template>
    <!-- emit "submit" when clicked; parent (form) will send an http request to the license management API -->
    <button type="submit" @click="emit('submit')">Submit</button>
</template>