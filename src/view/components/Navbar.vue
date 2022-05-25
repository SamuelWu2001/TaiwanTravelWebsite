
<template>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item" v-if="'/Accommodation' === this.$route.path">
          <a class="nav-link" href="#"><router-link to="/Accommodation" class="nav-link label" style="background: rgb(159, 200, 222);font-size:20px;font-weight:bolder;">Accommodation</router-link></a>
        </li>
        <li class="nav-item" v-else>
          <a class="nav-link" href="#"><router-link to="/Accommodation" class="nav-link label" style="background: white;font-size:20px;font-weight:bolder;">Accommodation</router-link></a>
        </li>
        <li class="nav-item" v-if="'/Restaurant' === this.$route.path">
          <a class="nav-link" href="#"><router-link to="/Restaurant"  class="nav-link label" style="background: rgb(159, 200, 222);font-size:20px;font-weight:bolder;">Restaurant</router-link></a>
        </li>
        <li class="nav-item" v-else>
          <a class="nav-link" href="#"><router-link to="/Restaurant"  class="nav-link label" style="background: white;font-size:20px;font-weight:bolder;">Restaurant</router-link></a>
        </li>
        <li class="nav-item" v-if="'/Attraction' === this.$route.path">
          <a class="nav-link" href="#"><router-link to="/Attraction"  class="nav-link label" style="background: rgb(159, 200, 222);font-size:20px;font-weight:bolder;">Attraction</router-link></a>
        </li>
        <li class="nav-item" v-else>
          <a class="nav-link" href="#"><router-link to="/Attraction"  class="nav-link label" style="background: white;font-size:20px;font-weight:bolder;">Attraction</router-link></a>
        </li>
        <li class="nav-item" v-if="'/Route' === this.$route.path">
          <a class="nav-link" href="#"><router-link to="/Route"  class="nav-link label" style="background: rgb(159, 200, 222);font-size:20px;font-weight:bolder;">Route</router-link></a>
        </li>
        <li class="nav-item" v-else>
          <a class="nav-link" href="#"><router-link to="/Route"  class="nav-link label" style="background: white;font-size:20px;font-weight:bolder;">Route</router-link></a>
        </li>
      </ul>
      <div style="float:right;">
        <div class="nav-item" v-if="'/User' === this.$route.path">
          <a class="nav-link" href="#"><router-link to="/User"  class="nav-link label" style="background: rgb(159, 200, 222);border-radius:1000px;"><img src="../../assets/user.png" height="50"></router-link></a>
        </div>
        <div class="nav-item" v-else>
          <a class="nav-link" href="#"><router-link to="/User"  class="nav-link label" style="background: white;border-radius:1000px;"><img src="../../assets/user.png" height="50"></router-link></a>
        </div>
      </div>
    </div>
  </div>
</nav>
</template>

<script>

export default {
  data() {
    return{
      url : "/Patient",
    };
  },
}
</script>


<style>
    .label{
      border-radius:15px;
    }
</style>
