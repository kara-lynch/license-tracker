<script setup lang="ts">
import { RouterLink } from 'vue-router'
import logo from '@/assets/salts_light.jpg'
</script>

<template>
    <nav class="taskbar">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/view-licenses">View Licenses</RouterLink>
        <RouterLink to="/assigned-to-me">Assigned Licenses</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <img :src="logo" alt="S.A.L.T.S" class="taskbar-logo" />
    </nav>
</template>

<style scoped>
/* full-width horizontal navigation with gradient and glass effect */
.taskbar {
    display: flex;
    gap: 1.0rem;
    justify-content: center;
    align-items: center;
    padding: 0.75rem 1.5rem;
    
    /* lilac gradient background with glass effect */
    background: linear-gradient(135deg, rgba(216, 180, 254, 0.85) 0%, rgba(192, 132, 252, 0.85) 50%, rgba(167, 139, 250, 0.85) 100%);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    
    border-bottom: 1px solid rgba(216, 180, 254, 0.3);
    box-shadow: 0 4px 24px rgba(139, 92, 246, 0.12);

    /* make the nav span the full viewport width (full-bleed) while
       keeping its content centered. This avoids changing App.vue structure. */
    box-sizing: border-box;
    width: 100vw;
    position: relative;
    left: 50%;
    transform: translateX(-50%);
}

.taskbar a {
    text-decoration: none;
    padding: 0.55rem 1.1rem;
    border-radius: 10px;
    color: #ffffff;
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.25);
    font-weight: 500;
    letter-spacing: 0.02em;
    transition: all 0.2s ease;
    box-shadow: 0 2px 8px rgba(139, 92, 246, 0.08);
}

.taskbar a.router-link-active {
    background: linear-gradient(135deg, #9333ea, #a855f7);
    color: #ffffff;
    border: 1px solid rgba(255, 255, 255, 0.4);
    box-shadow: 0 6px 20px rgba(147, 51, 234, 0.25);
    transform: translateY(-2px);
}

.taskbar a:hover {
    background: rgba(255, 255, 255, 0.28);
    border-color: rgba(255, 255, 255, 0.4);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(139, 92, 246, 0.15);
}

.taskbar-logo {
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    height: 40px;
    width: auto;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    transition: all 0.3s ease;
}

.taskbar-logo:hover {
    transform: translateY(-50%) scale(1.1);
    box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
}

</style>