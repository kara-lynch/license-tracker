<script setup lang="ts">
</script>

<template>
    <div class="side-widget-div">
        <slot></slot>
    </div>
</template>

<style scoped>
.side-widget-div {
  display: flex;
  gap: 12px;
  align-items: center;
  padding: 12px 20px;
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.08), rgba(168, 85, 247, 0.05));
  border-bottom: 2px solid rgba(139, 92, 246, 0.15);
  box-shadow: 0 4px 12px rgba(139, 92, 246, 0.1);
  position: sticky;
  top: var(--header-height, 60px);
  z-index: 10;
  backdrop-filter: blur(8px);
}

/* Style buttons inside the widget */
.side-widget-div :deep(button) {
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.9), rgba(168, 85, 247, 0.9));
  color: #fff;
  border: none;
  padding: 8px 20px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
  transition: all 0.3s ease;
  letter-spacing: 0.3px;
  font-size: 0.95rem;
}

.side-widget-div :deep(button:hover) {
  background: linear-gradient(135deg, rgba(168, 85, 247, 1), rgba(139, 92, 246, 1));
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(139, 92, 246, 0.4);
}

.side-widget-div :deep(button:active) {
  transform: translateY(0);
  box-shadow: 0 2px 8px rgba(139, 92, 246, 0.3);
}
</style>