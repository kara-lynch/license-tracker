<!-- Spencer will work on this component -->

<script setup lang="ts">
import BackgroundWidgetDiv from './widgets/BackgroundWidgetDiv.vue'
import AboutWidget from './widgets/AboutWidget.vue'
import AddLicenseBtn from './buttons/AddLicenseBtn.vue'
import SortByComponent from './inputs/SortByComponent.vue'
import SideWidgetDiv from './widgets/SideWidgetDiv.vue'
import DeleteLicenseBtn from './buttons/DeleteLicenseBtn.vue'
</script>

<template>
  <div>
    
    <!-- Main widget to see licenses -->
    <BackgroundWidgetDiv>
      <!-- <SortByComponent /> -->
      <AboutWidget />
    </BackgroundWidgetDiv>
  </div>

</template>