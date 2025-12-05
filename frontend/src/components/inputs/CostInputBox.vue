<script setup lang="ts">
import { ref } from 'vue';

const amount = ref('');
const currencies =[
    { value: 'USD', symbol: '$' },
    { value: 'EU', symbol: '€' },
    { value: 'CH', symbol: '¥' },
];

const selectedCurrency = ref(currencies[0]);

function updateCurrency() {
    selectedCurrency.value = selectedCurrency.value;
}

</script>

<template>

<div class="currency-input">
    <label>Cost</label>
    <div class="input-wrapper">
      <!-- Currency symbol -->
      <span>{{ selectedCurrency?.symbol }}</span>

      <!-- Amount input -->
      <input type="number" v-model="amount" placeholder="0.00"/>

      <!-- Dropdown -->
      <select v-model="selectedCurrency" @change="updateCurrency">
        <option v-for="currency in currencies" :value="currency">
            {{ currency.value }}
        </option>
      </select>
    </div>
  </div>

</template>