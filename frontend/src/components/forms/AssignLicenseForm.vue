<script setup lang="ts">
import { ref } from 'vue'
import FormSubmitBtn from '../buttons/FormSubmitBtn.vue';
import FormCancelBtn from '../buttons/FormCancelBtn.vue';

// allow emitting a "close" event to the parent
const emit = defineEmits<{
  (e: 'close'): void
}>()

const formRef = ref<HTMLFormElement | null>(null)

function handleCancel() {
  // reset native form fields
  if (formRef.value) formRef.value.reset()
  // notify parent to close the form
  emit('close')
}
</script>

<template>
    <!-- add ref so we can reset the form programmatically -->
    <form class="form-wrapper" ref="formRef">
        <div class="form-content">
            <label id="required-fields">Please fill out all required fields *</label>

            
                <div class="field-block">
                    <label id="license-id">license ID</label>
                        <input class="input-box" name="id" />
                </div>

                <div class="field-block">
                    <label id="employee-id">Employee ID</label>
                        <input class="input-box" name="eid" />
                </div>

                <div style="display:flex;gap:8px;align-items:center">
                  <FormSubmitBtn />
                  <!-- Cancel button resets the form and closes it via handleCancel -->
                  <FormCancelBtn @cancel="handleCancel" />
                </div>
        </div>
    </form>
</template>

<style scoped>
.form-wrapper {
    display: flex;
    flex-direction: column;
    width: 400px;
    margin: 0 auto;
    border-color: black;
    border-width: 1px;
    border-style: solid;
    padding: 20px;
}
.input-box {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    margin-top: 5px;
    margin-bottom: 15px;
}
</style>