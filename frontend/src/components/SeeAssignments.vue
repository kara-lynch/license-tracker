
<script setup lang="ts">
import BackgroundWidgetDiv from './widgets/BackgroundWidgetDiv.vue'
import SeeAssignmentsWidget from './widgets/SeeAssignmentsWidget.vue'
import AssignLicenseBtn from './buttons/AssignLicenseBtn.vue'
import SortByComponent from './inputs/SortByComponent.vue'
import SideWidgetDiv from './widgets/SideWidgetDiv.vue'
import UnassignLicenseBtn from './buttons/UnassignLicenseBtn.vue'
</script>

<template>
  <div>
    <!-- Side widget with manager buttons-->
    <SideWidgetDiv>
      <AssignLicenseBtn />
      <UnassignLicenseBtn />
    </SideWidgetDiv>  

    <!-- Main widget to see licenses -->
    <BackgroundWidgetDiv>
      <!-- <SortByComponent /> -->
      <SeeAssignmentsWidget />
    </BackgroundWidgetDiv>
  </div>

</template>