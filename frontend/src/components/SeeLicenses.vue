<!-- Spencer will work on this component -->

<script setup lang="ts">
import BackgroundWidgetDiv from './widgets/BackgroundWidgetDiv.vue'
import SeeLicenseWidget from './widgets/SeeLicenseWidget.vue'
import AddLicenseBtn from './buttons/AddLicenseBtn.vue'
import SortByComponent from './inputs/SortByComponent.vue'
</script>

<template>
  <div>
    <BackgroundWidgetDiv>
      <AddLicenseBtn />
    </BackgroundWidgetDiv>  
    
    <BackgroundWidgetDiv>
      <SortByComponent />
      <SeeLicenseWidget />
    </BackgroundWidgetDiv>
  </div>

</template>