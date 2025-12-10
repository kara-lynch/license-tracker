<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
    <nav class="taskbar">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/view-licenses">View Licenses</RouterLink>
        <RouterLink to="/assigned-to-me">Assigned to me</RouterLink>
        <RouterLink to="/about">About</RouterLink>
    </nav>
</template>

<style scoped>
/* Sticky, full-width horizontal navigation */
.taskbar {
    display: flex;
    gap: 0.5rem;
    justify-content: center;
    align-items: center;
    padding: 0.5rem 1rem;
    background: var(--color-background-soft, #f8fafc);
    border-bottom: 1px solid var(--color-border, rgba(15,23,42,0.06));

    /* No positioning here — App.vue provides the sticky full-viewport header.
         Keep the nav at 100% of the header so it is fully visible and centered. */
    width: 100%;
    position: static;
}

.taskbar a {
    text-decoration: none;
    padding: 0.45rem 0.9rem;
    border-radius: 6px;
    color: var(--color-heading, #0f172a);
    background: transparent;
    border: 1px solid transparent;
    transition: background-color 0.15s ease, color 0.15s ease;
}

.taskbar a.router-link-active {
    background: #0ea5a0; /* active teal */
    color: white;
}

.taskbar a:hover {
    background: rgba(14,165,160,0.08);
}

/* Make sure the sticky nav doesn't overlap content on small screens */
@media (max-width: 640px) {
    .taskbar {
        padding: 0.5rem;
        gap: 0.25rem;
    }
    .taskbar a {
        padding: 0.35rem 0.6rem;
        font-size: 0.95rem;
    }
}
</style>