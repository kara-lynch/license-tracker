<script setup lang="ts">
import { RouterLink } from 'vue-router'
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
</template>

<style scoped>
.home {
  max-width: 980px;
  margin: 0 auto;
  padding: 1.25rem;
}

h1 {
  font-size: 2rem;
  margin: 0 0 0.5rem 0;
  text-align: center;
}

.lead {
  text-align: center;
  color: rgba(15,23,42,0.75);
  margin-bottom: 1rem;
}

h2 {
  margin-top: 1rem;
}

ol {
  margin-left: 1.1rem;
}

.actions {
  display: flex;
  gap: 0.75rem;
  margin: 0.5rem 0 1rem 0;
}

.btn {
  display: inline-block;
  padding: 0.5rem 0.9rem;
  background: #0ea5a0;
  color: #fff;
  border-radius: 6px;
  text-decoration: none;
}

.btn:hover {
  background: #08a299;
}

ul {
  margin-left: 1.1rem;
}

.help {
  margin-top: 1.25rem;
  color: rgba(15,23,42,0.7);
}
</style>

