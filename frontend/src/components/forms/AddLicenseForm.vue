<script setup lang="ts">
import CostInputBox from '../inputs/CostInputBox.vue';


</script>

<template>
    <form>
        <div class="form-wrapper">
            <label id="required-fields">Please fill out all required fields</label>

                <div class="license-name-input">
                    <label id="license-name">License Name</label>
                    <input></input>
                </div>

                <div class="license-version-input">
                    <label id="license-version">License version</label>
                    <input></input>
                </div>

                <div class="license-type-input">
                    <label id="license-type">License Type</label>
                    <select id="license-type" name="license-type">
                        <option>Enterprise</option>
                        <option>Open Source</option>
                    </select>
                </div>

                <CostInputBox />

                <div class="license-renewal-date-input">
                    <label id="license-renewal-period">Renewal Period</label>
                    <input></input>
                </div>

            <label id="license-renewal-date">Renewal Date</label>
            <input></input>

            <label id="license-expiration-date">Expiration Date</label>
            <input></input>

            <label id="license-geography-restrictions">Geography Restrictions</label>
            <input></input>
        </div>
    </form>
</template>