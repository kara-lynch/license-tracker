<script setup lang="ts">

import router from '@/router';

async function logout (){
    // console.log("BEFORE:"+document.cookie)
    document.cookie= "empty cookie";
    await router.push('/');
    window.location.reload();
    // console.log("AFTER:"+document.cookie)
}

</script>

<template>
    <button @click="logout">Logout</button>
</template>