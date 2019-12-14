<template>
  <div id="profiles-list">
    <div id="list-search" class="w-100 grey-bg">
      <form method="get">
        <div id="search-container" class="form-row p-2">
          <div class="col-12 col-sm-6 offset-sm-3">
            <div id="search-form" class="input-group bg-white rounded">
              <div class="input-group-prepend p-1 w-100">
                <input
                  id="search"
                  class="form-control"
                  type="search"
                  placeholder="Enter keywords, e.g. 'Attention MEG France'"
                  name="s"
                  autofocus
                  v-model="search"
                />
                <input
                  id="search-btn"
                  type="submit"
                  value="Search"
                  class="btn btn-secondary pl-4 pr-4 rounded mx-auto"
                  @click.prevent="getProfilesList"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="form-row p-2">
          <div
            id="underrepresented-countries"
            class="col-12 col-sm-9 offset-sm-3 col-lg-3 offset-lg-3"
          >
            <div class="form-check custom-control custom-checkbox">
              <input
                type="checkbox"
                class="custom-control-input"
                id="underrepresented-only"
                v-model="underRepresented"
                @change="getProfilesList"
              />
              <label class="custom-control-label" for="underrepresented-only"
                >Under Represented Countries Only</label
              >
            </div>
          </div>
          <div
            id="senior-positions"
            class="col-12 col-sm-9 offset-sm-3 col-lg-3 offset-lg-0"
          >
            <div class="form-check custom-control custom-checkbox">
              <input
                type="checkbox"
                class="custom-control-input"
                id="senior-only"
                v-model="senior"
                @change="getProfilesList"
              />
              <label class="custom-control-label" for="senior-only"
                >Senior Positions Only</label
              >
            </div>
          </div>
        </div>
      </form>
    </div>

    <div
      v-if="count > 0"
      id="profiles-list"
      class="bg-white rounded-top p-4 offset-md-1 col-md-10 offset-lg-2 col-lg-8"
    >
      <div class="pb-3 no-gutters entries-number">
        <span id="search-message">
          <span class="text-secondary font-weight-bold">{{ count }}</span>
          entries found.
        </span>
      </div>
      <div id="results-table" class="infinite-container">
        <div
          v-for="profile in profiles"
          class="table-entry infinite-item"
          :key="profile.id"
        >
          <div class="row my-4 no-gutters">
            <div class="col-xs-12 col-sm-4 col-lg-3">
              <h5 class="text-primary font-weight-bold">{{ profile.name }}</h5>
            </div>
            <div class="col-xs-12 col-sm-4 col-lg-3 details-grey text-muted">
              <p class="m-1">
                <i class="fas fa-user"></i>
                <span class="ml-1">{{ profile.position }}</span>
              </p>
              <p class="m-1">
                <i class="fas fa-university"></i>
                <span class="ml-1">{{ profile.institution }}</span>
              </p>
              <p v-if="profile.country" class="m-1">
                <i class="fas fa-map-marker-alt"></i>
                <span class="ml-1">{{ profile.country }}</span>
              </p>
            </div>

            <div class="keywords-list col-lg-3 mt-1 d-none d-lg-block">
              {{
                []
                  .concat(profile.modalities, profile.domains, profile.keywords)
                  .filter(el => el)
                  .join(', ')
              }}
            </div>
            <div class="col-md-1 mt-1 pl-4 d-none d-md-block text-primary">
              <span v-if="profile.recommendations.length > 0"
                ><i class="fas fa-comment num-rec"></i>
                {{ profile.recommendations.length }}</span
              >
            </div>
            <div
              class="actions col-xs-12 col-sm-4 col-md-2 text-xs-left text-sm-right"
            >
              <router-link
                :to="{ name: 'profile', params: { id: profile.id.toString() } }"
                class="btn pill-btn btn-outline-secondary w-75 m-2"
              >
                View Profile
              </router-link>
              <router-link
                :to="{
                  name: 'recommend',
                  params: { id: profile.id.toString() }
                }"
                class="btn pill-btn btn-outline-secondary w-75 m-2"
              >
                Recommend
              </router-link>
              <!-- <a
                class="btn pill-btn btn-outline-secondary w-75 m-2"
                href="/recommend"
                >Recommend</a
              > -->
            </div>
          </div>
        </div>
      </div>
      <p v-show="isLoading">Loading...</p>
    </div>

    <div
      v-else
      id="profiles-list"
      class="bg-white rounded-top p-4 offset-md-1 col-md-10 offset-lg-2 col-lg-8"
    >
      <p>No matching profiles</p>
    </div>

    <!-- from http://jsfiddle.net/gilbitron/Lt2wH/ -->
    <a href="#" id="back-to-top" title="Back to top" class="btn"
      ><i class="fas fa-chevron-circle-up"></i
    ></a>

    <go-top
      :src="require('../assets/back-to-top.svg')"
      :size="44"
      :maxWidth="0"
      bg-color="#fff"
    ></go-top>
  </div>
</template>

<script>
import GoTop from '@inotom/vue-go-top';
import { apiService } from '../common/api_service';

export default {
  name: 'ProfilesList',
  components: {
    GoTop
  },
  data() {
    return {
      profiles: [],
      count: 0,
      next: null,
      isLoading: false,
      search: '',
      senior: false,
      underRepresented: false
    };
  },
  methods: {
    getProfilesList() {
      const endpoint = `api/profiles/?s=${encodeURIComponent(this.search) +
        (this.senior ? '&senior' : '') +
        (this.underRepresented ? '&ur' : '')}`;
      this.isLoading = true;
      apiService(endpoint).then(data => {
        this.count = data.count;
        this.profiles = data.results;
        this.isLoading = false;
        this.next = data.next || null;
      });
    },
    getNextProfiles() {
      if (!this.next) return;
      const endpoint = this.next;
      this.isLoading = true;
      apiService(endpoint).then(data => {
        this.count = data.count;
        this.profiles.push(...data.results);
        this.isLoading = false;
        this.next = data.next || null;
      });
    },
    onScroll() {
      if (
        (window.innerHeight + window.scrollY >= document.body.offsetHeight) &
        !this.isLoading
      ) {
        this.getNextProfiles();
      }
    }
  },
  created() {
    document.title = 'Winrepo - Repository';
    this.getProfilesList();
  },
  mounted() {
    document.addEventListener('scroll', this.onScroll);
  },
  destroyed() {
    document.removeEventListener('scroll', this.onScroll);
  }
};
</script>

<style scoped>
#list-search {
  padding-top: 64px;
  padding-bottom: 30px;
}

#list-search .custom-control-label:before,
#list-search .custom-control-label:after {
  background-color: #fff;
  border-radius: 2px;
}

#list-search
  .custom-checkbox
  .custom-control-input:checked
  ~ .custom-control-label::before,
#list-search
  .custom-checkbox
  .custom-control-input:checked
  ~ .custom-control-label::after {
  background-color: #1c898a;
  border-radius: 2px;
}

#search-message > span {
  font-size: 18px;
  padding-top: 20px;
  padding-bottom: 20px;
}

#search {
  line-height: 2.5rem;
  border: white;
  border-left: #e6e6e6;
}

#search:focus {
  box-shadow: none;
}

#search-form .input-group-prepend {
  height: 3em;
}

/* .input-group-text {
  line-height: 2.5rem;
  border: white;
} */

.entries-number {
  border-bottom: 1px solid #ababab;
}

.table-entry {
  border-bottom: 1px solid #cdcdcd;
}

.table-entry .keywords-list {
  max-height: 120px;
  overflow: hidden;
}

.table-entry .actions a {
  font-size: 0.9em;
}

.num-rec {
  font-size: 24px;
}

#results-nav a.pill-btn {
  width: 110px;
}

#page-number {
  line-height: 2.9em;
}

#back-to-top {
  position: fixed;
  bottom: 40px;
  right: 40px;
  z-index: 9999;
  background: #cacaca;
  color: #fafafa;
  cursor: pointer;
  border: 0;
  border-radius: 50%;
  height: 50px;
  width: 50px;
  padding: 0px;
  font-size: 42px;
  line-height: 50px;
  text-decoration: none;
  transition: opacity 0.2s ease-out;
  opacity: 0;
}
#back-to-top:hover {
  background: #10898b;
}

#back-to-top.show {
  opacity: 1;
}

#field-of-research-list > div {
  border-right: 1px solid #ccc;
}

#field-of-research-list > div:last-child {
  border-right: none;
}

li.quote .quote-date {
  line-height: 1.6rem;
}

/* Autocomplete fields  */
.modelselect2 {
  height: auto !important;
}

.modelselect2 > span {
  height: 100% !important;
}

.select2-selection {
  border: 1px solid #ced4da !important;
}
</style>
