<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/view-licenses">View Licenses</RouterLink>
        <RouterLink to="/assigned-to-me">Assigned to me</RouterLink>
        <!-- <RouterLink to="/login">Assigned to me</RouterLink> -->
    </nav>
</template>