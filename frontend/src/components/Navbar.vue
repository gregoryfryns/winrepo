<template>
  <nav class="navbar fixed-top navbar-light shadow-sm navbar-expand-md">
    <router-link class="navbar-brand" :to="{ name: 'home' }">
      <picture id="winrepo-logo">
        <source
          srcset="../assets/logo_fill_triangles_wb.webp"
          type="image/webp"
        />
        <source
          srcset="../assets/logo_fill_triangles_wb.png"
          type="image/png"
        />
        <source
          srcset="../assets/logo_fill_triangles_wb.jpg"
          type="image/jpeg"
        />
        <img src="../assets/logo_fill_triangles_wb.jpg" alt="Winrepo Logo" />
      </picture>
    </router-link>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <ul class="nav navbar-nav ml-auto">
        <router-link
          :to="{ name: 'home' }"
          v-slot="{ href, route, navigate, isActive, isExactActive }"
        >
          <li
            class="nav-item"
            :class="[isActive && 'active', isExactActive && 'exact-active']"
          >
            <a class="nav-link h6" :href="href" @click="navigate">Home</a>
          </li>
        </router-link>
        <router-link
          :to="{ name: 'list' }"
          v-slot="{ href, route, navigate, isActive, isExactActive }"
        >
          <li
            class="nav-item"
            :class="[isActive && 'active', isExactActive && 'exact-active']"
          >
            <a class="nav-link h6" :href="href" @click="navigate">Repository</a>
          </li>
        </router-link>
        <router-link
          :to="{ name: 'create' }"
          v-slot="{ href, route, navigate, isActive, isExactActive }"
        >
          <li
            class="nav-item"
            :class="[isActive && 'active', isExactActive && 'exact-active']"
          >
            <a class="nav-link h6" :href="href" @click="navigate">Create Profile</a>
          </li>
        </router-link>
        <router-link
          :to="{ name: 'recommend' }"
          v-slot="{ href, route, navigate, isActive, isExactActive }"
        >
          <li
            class="nav-item"
            :class="[isActive && 'active', isExactActive && 'exact-active']"
          >
            <a class="nav-link h6" :href="href" @click="navigate">Recommend</a>
          </li>
        </router-link>
        <router-link
          :to="{ name: 'faq' }"
          v-slot="{ href, route, navigate, isActive, isExactActive }"
        >
          <li
            class="nav-item"
            :class="[isActive && 'active', isExactActive && 'exact-active']"
          >
            <a class="nav-link h6" :href="href" @click="navigate">FAQ</a>
          </li>
        </router-link>
        <router-link
          :to="{ name: 'about' }"
          v-slot="{ href, route, navigate, isActive, isExactActive }"
        >
          <li
            class="nav-item"
            :class="[isActive && 'active', isExactActive && 'exact-active']"
          >
            <a class="nav-link h6" :href="href" @click="navigate">About</a>
          </li>
        </router-link>

<!-- 
        <li
          @click="active = 'home'"
          class="nav-item"
          :class="{ active: active === 'home' }"
        >
          <router-link class="nav-link h6" :to="{ name: 'home' }">
            Home
          </router-link>
        </li>
        <li
          @click="active = 'list'"
          class="nav-item"
          :class="{ active: active === 'list' }"
        >
          <router-link class="nav-link h6" :to="{ name: 'list' }">
            Repository
          </router-link>
        </li>
        <li
          @click="active = 'create'"
          class="nav-item"
          :class="{ active: active === 'create' }"
        >
          <router-link class="nav-link h6" :to="{ name: 'create' }">
            Create Profile
          </router-link>
        </li>
        <li
          @click="active = 'recommend'"
          class="nav-item"
          :class="{ active: active === 'recommend' }"
        >
          <router-link class="nav-link h6" :to="{ name: 'recommend' }">
            Recommend
          </router-link>
        </li>
        <li
          @click="active = 'faq'"
          class="nav-item"
          :class="{ active: active === 'faq' }"
        >
          <router-link class="nav-link h6" :to="{ name: 'faq' }">
            FAQ
          </router-link>
        </li>
        <li
          @click="active = 'about'"
          class="nav-item"
          :class="{ active: active === 'about' }"
        >
          <router-link class="nav-link h6" :to="{ name: 'about' }">
            About
          </router-link>
        </li> -->
      </ul>
    </div>
    <button
      class="navbar-toggler ml-auto"
      type="button"
      data-toggle="collapse"
      data-target="#navbarNavAltMarkup"
      aria-controls="navbarNavAltMarkup"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
  </nav>
</template>

<script>
export default {
  name: 'NavbarComponent',
  data() {
    return { active: 'home' };
  }
};
</script>

<style scoped>
nav {
  background-color: white;
}

.navbar-brand,
.navbar-text {
  color: #555;
}
.navbar-nav .nav-link {
  color: #555;
}
.nav-item.active .nav-link {
  color: #10898b; /*red #CC063E*/
  text-decoration: underline;
  font-weight: bold;
}
.nav-item:hover .nav-link {
  color: #10898b;
}
#winrepo-logo > img {
  height: 38px;
}
</style>
