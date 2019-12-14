<template>
  <div id="pageNotFound">
    <div id="list-search" class="w-100 bg-primary"></div>
    <div
      class="bg-white rounded-top p-4 offset-md-1 col-md-10 offset-lg-2 col-lg-8"
    >
      <h2 class="p-4 text-center">{{ message }}</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
  data() {
    return {
      message: '404 - Page Not Found!'
    };
  }
};
</script>
