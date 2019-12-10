<template>
  <div id="app">
    <NavbarComponent />
    <div id="content" class="bg-white mb-5">
      <router-view />
    </div>
    <FooterComponent />
  </div>
</template>

<script>
// @ is an alias to /src
import { apiServce } from '@/common/api_service';
import NavbarComponent from '@/components/Navbar.vue';
import FooterComponent from '@/components/Footer.vue';

export default {
  name: 'App',
  components: {
    NavbarComponent,
    FooterComponent
  }
};
</script>

<style>
#app {
  font-family: 'Open Sans', 'Lato', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center;
  color: #2c3e50; */
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: 'Nunito', 'Lato', sans-serif;
}

#content {
  margin-top: 2.3em;
}

.grey-bg {
  background-color: #e6e6e6;
}

.link-secondary {
  color: #cc063e;
}

.pill-btn {
  border-radius: 50px;
}

.full-page {
  padding-top: 65px;
}

.vs__search,
.vs__search:focus {
  padding: 2px 4px !important;
  line-height: 24px !important;
}

.vs__selected-options {
  padding-left: 6px !important;
}
</style>
