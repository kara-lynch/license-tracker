<!-- Spencer will work on this component -->

<script setup lang="ts">
import BackgroundWidgetDiv from './widgets/BackgroundWidgetDiv.vue'
import SeeLicenseWidget from './widgets/SeeLicenseWidget.vue'
import AddLicenseBtn from './buttons/AddLicenseBtn.vue'
import SortByComponent from './inputs/SortByComponent.vue'
import SideWidgetDiv from './widgets/SideWidgetDiv.vue'
</script>

<template>
  <div>
    <!-- Side widget with manager buttons-->>
    <SideWidgetDiv>
      <AddLicenseBtn />
    </SideWidgetDiv>  

    <BackgroundWidgetDiv>
      <SortByComponent />
      <SeeLicenseWidget />
    </BackgroundWidgetDiv>
  </div>

</template>