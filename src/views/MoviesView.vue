<template>
    <div class="container">
      <h2>Movie List</h2>
      <div class="row">
        <div v-for="movie in movies" :key="movie.id" class="col-md-4">
          <div class="card">
            <img :src="movie.poster" class="image" alt="Poster" />
            <div class="body">
              <h5 class="title">{{ movie.title }}</h5>
              <p class="text">{{ movie.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  
  let movies = ref([]);
  
  onMounted(() => {
    fetch("/api/v1/movies")
      .then((response) => response.json())
      .then((data) => {
        movies.value = data.movies;
      })
      .catch((error) => console.error("Error fetching movies:", error));
  });
  </script>
  