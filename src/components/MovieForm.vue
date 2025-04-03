<template>
    <div class="container">
      <h2 class="mb-4">Add New Movie</h2>
      
      
      <div v-if="message" class="alert alert-success">{{ message }}</div>
      <div v-if="errors.length" class="alert alert-danger">
        <ul>
          <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
        </ul>
      </div>
  
     
      <form id="movieForm" @submit.prevent="saveMovie">
        <div class="form-group mb-3">
          <label for="title" class="form-label">Title</label>
          <input type="text" v-model="title" name="title" class="form-control" required />
        </div>
  
        <div class="form-group mb-3">
          <label for="description" class="form-label">Description</label>
          <textarea v-model="description" name="description" class="form-control" rows="4" required></textarea>
        </div>
  
        <div class="form-group mb-3">
          <label for="poster" class="form-label">Poster</label>
          <input type="file" @change="handleFileUpload" name="poster" class="form-control" required />
        </div>
  
        <button type="submit" class="btn btn-primary">Save</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  

  let title = ref("");
  let description = ref("");
  let poster = ref(null);
  let csrf_token = ref("");
  let message = ref("");
  let errors = ref([]);
  
  
  onMounted(() => {
    getCsrfToken();
  });
  
 
  function getCsrfToken() {
    fetch('/api/v1/csrf-token')
      .then(response => response.json())
      .then(data => {
        csrf_token.value = data.csrf_token;
      })
      .catch(error => console.log(error));
  }
  
  
  function handleFileUpload(event) {
    poster.value = event.target.files[0];
  }
  
 
  function saveMovie() {
    let fData = new FormData();
    fData.append("title", title.value);
    fData.append("description", description.value);
    fData.append("poster", poster.value);
  
    fetch("/api/v1/movies", {
      method: 'POST',
      body: fData,
      headers: {
        'X-CSRFToken': csrf_token.value
      }
    })
    .then(response => response.json())
    .then(data => {
      if (data.errors) {
        errors.value = Object.values(data.errors).flat(); // Convert error object to array
        message.value = "";
      } else {
        message.value = data.message;
        errors.value = [];
        title.value = "";
        description.value = "";
        poster.value = null;
      }
    })
    .catch(error => console.log(error));
  }
  </script>
  
  <style>
  .container {
    max-width: 500px;
    margin: auto;
    padding: 20px;
  }
  .alert {
    margin-bottom: 15px;
  }
  </style>
  