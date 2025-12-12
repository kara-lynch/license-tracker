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
  animation: slideDown 0.5s ease-out;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
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
  animation: buttonSlide 0.5s ease-out backwards;
}

.side-widget-div :deep(button:nth-child(1)) {
  animation-delay: 0.1s;
}

.side-widget-div :deep(button:nth-child(2)) {
  animation-delay: 0.2s;
}

.side-widget-div :deep(button:nth-child(3)) {
  animation-delay: 0.3s;
}

.side-widget-div :deep(button:nth-child(4)) {
  animation-delay: 0.4s;
}

.side-widget-div :deep(button:nth-child(5)) {
  animation-delay: 0.5s;
}

.side-widget-div :deep(button:nth-child(6)) {
  animation-delay: 0.6s;
}

@keyframes buttonSlide {
  0% {
    opacity: 0;
    transform: translateY(-50px);
  }
  60% {
    transform: translateY(5px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
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