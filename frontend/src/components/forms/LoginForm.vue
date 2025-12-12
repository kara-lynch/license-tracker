<script setup lang="ts">
// import { ref } from 'vue'
import { ref } from 'vue';
import FormSubmitBtn from '../buttons/FormSubmitBtn.vue';
import FormCancelBtn from '../buttons/FormCancelBtn.vue';
import router from '@/router';


const publicKeyPEM = `
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArkOuYMSFFatZA+PhgW6cVMVBPBdePouwHMsZYmY1vndJLQcSPzsJywdB+N5uncfgZWhTKu7ByQy/DZnpRFiMpntUCLD2c0eOZH8rqzbT+eDtemKVSmFVfz8cuWcqPJz048nqtrnKHwz/IaJvjiyBCj2BWlNgu4EDLVmDbzQJHgqFlRYad1cPf5JM6IBfZSogAO5iVcAmBTa0jz5hGiVE74QhIzes0yNrpH7VOLrVpjJo5J5dUw8iRwDVTWeNat2T+tjeMgzrQjQML2ooPasLzkEy7Jgsh3oJoAs357nKlNRWXkFzR8WUFTv+IH2rr3Hilz7Mm1thizYA2Dp0KRbypwIDAQAB
-----END PUBLIC KEY-----
`;

function encryptString(username: string, password: string) {
    // Parse the public key
    const pub = KEYUTIL.getKey(publicKeyPEM);

    // Encrypt using PKCS#1 v1.5 padding
    const encryptedHex = KJUR.crypto.Cipher.encrypt(password, pub, 'RSA');
    // Convert hex to base64 for Java
    const encryptedBase64 = hex2b64(encryptedHex);

    var json_return = {
        "username": username,
        "password": encryptedBase64
    }

    return json_return;
}

const formRef = ref<HTMLFormElement | null>(null)

async function handleLogin(e: Event) {
    e.preventDefault()
    if (!formRef.value) return

    const formData = new FormData(formRef.value)
    const data: Record<string, any> = {
        username: String(formData.get("username")),
        password: String(formData.get("password"))
    }
    
    let ctext = encryptString(data.username, data.password)

    // HTTP REQUEST TO SSO
    try {
        const res = await fetch('http://172.16.0.203:5000/sso_login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // 'Access-Control-Allow-Origin': '*'
            },
            body: await JSON.stringify(ctext)
        })
        if (res.ok) {
            // Store cookie
            // document.cookie = sdfjlsdf
            // Redirect
            var token = ""
            await res.json().then(data => {token = data.token})
            // console.log(token)
            document.cookie = token
            // console.log(document.cookie)
            router.push({ path: 'home' }) // Send to 
            // console.log("BODY -> " + await res.json().then(data => {console.log(data)}))
        }
        else {
            console.error('Ping failed!', res.status, await res.text())
        }
    } catch (err){
            console.error('Network error', err)
    }

    // STORE RESPONSE AS A COOKIE

}
</script>

<template>
    <form class="form-wrapper" ref="formRef" @submit="handleLogin">
        <div class="form-content">
            <label id="required-fields"></label>
            <div class="field-block">
                <label id="Username">Username</label>
                <input class="input-box" name="username" />
            </div>
            <div class="field-block">
                <label id="Password">Password</label>
                <input class="input-box" name="password" />
            </div>

            <div style="display:flex;gap:8px;align-items:center;">
                <FormSubmitBtn />
            </div>
        </div>
    </form>
</template>