<template>
  <div class="faq">
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  name: "faq",
  data() {
    return {
      message: "hello FAQ!"
    };
  }
};
</script>

<style scoped>
h1 {
  color: blue;
}
</style>
