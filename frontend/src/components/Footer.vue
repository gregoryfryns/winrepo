<template>
  <footer class="font-small bg-primary text-white p-4 mt-4">
    <div class="d-flex flex-wrap justify-content-center">
      <div
        class="col-12 col-md-4 text-md-left text-sm-center"
        style="vertical-align:middle;line-height:1.5rem"
      >
        <span class="font-weight-bold mx-1 align-middle"
          >Women in Neuroscience Repository</span
        >
      </div>
      <div class="col-12 col-md-4 text-center"></div>
      <div class="col-12 col-md-4 text-md-right text-sm-center">
        <a
          class="btn btn-lg mx-1"
          href="https://www.facebook.com/WiNRepository/"
        >
          <i class="fab fa-facebook-f"></i>
        </a>
        <a class="btn btn-lg mx-1" href="https://twitter.com/WINRePo1">
          <i class="fab fa-twitter"></i>
        </a>
        <a class="btn btn-lg mx-1" href="mailto:admin@winrepo.org">
          <i class="fas fa-envelope"></i>
        </a>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'FooterComponent'
};
</script>

<style scoped>
footer {
  color: #fff;
}

a {
  color: #fff;
}
</style>
