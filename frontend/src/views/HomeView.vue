<script setup lang="ts">
import { RouterLink } from 'vue-router'
import logo from '@/assets/salts_light.jpg'

</script>

<template>
  <section class="home">
    <h1>Welcome to S.A.L.T.S</h1>

    <p class="lead">S.A.L.T.S helps your team track, assign and manage software licenses in one central place.</p>

    <h2>Getting started</h2>
    <ol>
      <li>Use the navigation at the top to move between pages.</li>
      <li>Click <RouterLink to="/view-licenses">View Licenses</RouterLink> to see all current licenses and try sorting them using the column controls.</li>
      <li>From the <em>View Licenses</em> page you can add a new license or delete an existing one using the buttons in the UI.</li>
      <li>Visit <RouterLink to="/assigned-to-me">Assigned to me</RouterLink> to see licenses specifically assigned to your account.</li>
      <li>For team information and contact details, visit the <RouterLink to="/about">About</RouterLink> page.</li>
    </ol>

    <h3>Quick actions</h3>
    <div class="actions">
      <RouterLink to="/view-licenses" class="btn">View Licenses</RouterLink>
      <RouterLink to="/assigned-to-me" class="btn">Assigned to me</RouterLink>
      <RouterLink to="/about" class="btn">About</RouterLink>
    </div>

    <h3>Features at a glance</h3>
    <ul>
      <li>View all licenses in a table with sorting and filtering.</li>
      <li>Add new licenses (product, vendor, cost, renewal period, assignee).</li>
      <li>Delete licenses you no longer track.</li>
      <li>See only the licenses assigned to you on the Assigned page.</li>
    </ul>

    <h3>How to add or delete a license</h3>
    <p>
      From the <strong>View Licenses</strong> page click the <em>Add</em> button and fill out the form with the license details. To remove a license, select it and use the <em>Delete</em> action — most actions will prompt you to confirm before changing data.
    </p>

    <h3>Sorting and searching</h3>
    <p>
      Use the table headers or provided controls on the <strong>View Licenses</strong> page to sort by fields like cost, renewal date, or license type. Use the search or filter inputs to narrow results.
    </p>

    <h3>Assigned to me</h3>
    <p>
      The <strong>Assigned to me</strong> page shows only licenses where your user is the assignee. This makes it easy to find your responsibilities and upcoming renewals.
    </p>

    <h3>Tips & troubleshooting</h3>
    <ul>
      <li>If a page looks empty, make sure you are authenticated (some features may require login/permissions).</li>
      <li>Use the browser console or the backend logs for error details when an action fails.</li>
      <li>If sorting or filtering behaves unexpectedly, try refreshing the page — the app reads latest data from the API on load.</li>
    </ul>
    <h3>Permissions</h3>
    <ul>
      <li>Some actions like adding or deleting licenses may require specific user permissions. Ensure your account has the necessary rights.</li>
      <li>Contact your administrator if you encounter permission issues.</li>
    </ul>
    <p class="help">Questions or need help? Reach out to your project team via the About page or the repository maintainers.</p>
  </section>
  <!-- simple, easy-to-edit inline logo placed top-right below header -->
  <img :src="logo" alt="S.A.L.T.S logo" 
  style="
  position:absolute; 
  top:220px; 
  right:20px; 
  width:200px; 
  height:auto;
  border: 4px solid rgba(139, 92, 246, 0.3);
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(139, 92, 246, 0.15), 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;" 
  />

</template>

<style scoped>
.home {
  padding: 1.25rem;
}

h1 {
  font-size: 3rem;
  margin: 0 0 0.5rem 0;
  margin-left: calc(-50vw + 50%);
  margin-right: calc(-50vw + 50%);
  padding-left: calc(50vw - 50%);
  padding-right: calc(50vw - 50%);
  text-align: center;
  font-weight: 800;
  letter-spacing: 0.3em;
  font-family: 'Train One', 'Tahoma', 'Verdana', 'Geneva', sans-serif;
  text-transform: uppercase;
  color: #020202;
  position: relative;
  border-top: 3px solid rgba(0, 0, 0, 0.6);
  border-bottom: 3px solid rgba(0, 0, 0, 0.6);
  padding-top: 1rem;
  padding-bottom: 1rem;
  background: linear-gradient(90deg, 
    transparent 0%, 
    rgba(139, 92, 246, 0.03) 10%, 
    rgba(139, 92, 246, 0.05) 50%, 
    rgba(139, 92, 246, 0.03) 90%, 
    transparent 100%);
}

h1::before,
h1::after {
  content: '';
  position: absolute;
  width: 40px;
  height: 3px;
  background: linear-gradient(90deg, #8b5cf6, #a855f7);
}

h1::before {
  top: -3px;
  left: 50%;
  transform: translateX(-50%);
}

h1::after {
  bottom: -3px;
  left: 50%;
  transform: translateX(-50%);
}

.lead {
  text-align: left;
  color: #1a1a1a;
  margin-bottom: 2rem;
  margin-right: 240px;
  font-size: 1.35rem;
  font-weight: 500;
  letter-spacing: 0.3px;
}

h2 {
  margin-top: 2rem;
  font-size: 2rem;
  font-weight: 600;
  color: #000;
  border-left: 4px solid rgba(139, 92, 246, 0.6);
  padding-left: 1rem;
  letter-spacing: -0.3px;
}

h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #000;
  margin-top: 1.5rem;
  position: relative;
  padding-left: 1rem;
  letter-spacing: -0.2px;
}

h3::before {
  content: '▸';
  position: absolute;
  left: 0;
  color: rgba(139, 92, 246, 0.7);
  font-size: 1.2rem;
}

ol {
  margin-left: 1.1rem;
  color: #000;
  line-height: 1.8;
  font-weight: 400;
  font-size: 1.1rem;
}

ol li {
  margin-bottom: 0.5rem;
  padding-left: 0.5rem;
}

.actions {
  display: flex;
  gap: 0.75rem;
  margin: 1.5rem 0 2rem 0;
}

.btn {
  display: inline-block;
  padding: 0.7rem 1.2rem;
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.9), rgba(168, 85, 247, 0.9));
  color: #fff;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  letter-spacing: 0.3px;
  box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
  transition: all 0.3s ease;
  border: 1px solid rgba(139, 92, 246, 0.4);
}

.btn:hover {
  background: linear-gradient(135deg, rgba(168, 85, 247, 1), rgba(139, 92, 246, 1));
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(139, 92, 246, 0.4);
}

ul {
  margin-left: 1.1rem;
  color: #000;
  line-height: 1.8;
  font-weight: 400;
  font-size: 1.1rem;
}

ul li {
  margin-bottom: 0.5rem;
  padding-left: 0.5rem;
  position: relative;
}

ul li::marker {
  color: rgba(139, 92, 246, 0.7);
}

p {
  color: #000;
  line-height: 1.7;
  font-weight: 400;
  font-size: 1.1rem;
}

strong {
  font-weight: 700;
  color: #000;
}

em {
  font-style: italic;
  color: rgba(139, 92, 246, 0.9);
  font-weight: 500;
}

.help {
  margin-top: 2rem;
  padding: 1rem;
  background: rgba(139, 92, 246, 0.05);
  border-left: 3px solid rgba(139, 92, 246, 0.6);
  border-radius: 4px;
  color: #000;
  font-weight: 500;
}
</style>

