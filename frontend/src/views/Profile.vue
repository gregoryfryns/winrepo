<template>
  <div id="profileDetails">
    <div id="list-search" class="w-100 bg-primary"></div>
    <div
      class="bg-white rounded-top p-4 offset-md-1 col-md-10 offset-lg-2 col-lg-8"
    >
      <div class="container-fluid">
        <div class="row no-gutters">
          <div class="col-xs-6 col-sm-8 col-md-9 text-muted details-grey">
            <h2 class="text-primary font-weight-bold">{{ profile.name }}</h2>
            <p v-if="profile.position" class="m-1">
              <i class="fas fa-user"></i> {{ profile.position }}
            </p>
            <p v-if="profile.institution" class="m-1">
              <i class="fas fa-university"></i> {{ profile.institution }}
            </p>
            <p v-if="profile.country" class="m-1">
              <i class="fas fa-map-marker-alt"></i> {{ profile.country }}
            </p>
            <p v-if="profile.grad_year" class="m-1">
              <i class="fas fa-graduation-cap"></i>
              {{ profile.grad_month }} {{ profile.grad_year }}
            </p>
          </div>
          <div class="col-xs-6 col-sm-4 col-md-3">
            <div class="d-flex flex-column">
              <a
                class="btn pill-btn text-white btn-secondary m-1 email-btn"
                :class="{ disabled: profile.contact_email === '' }"
                :href="`mailto:${profile.contact_email}`"
              >
                <i class="fas fa-envelope"></i> Send Email
              </a>

              <a
                class="btn pill-btn text-white btn-secondary m-1 webpage-btn"
                :class="{ disabled: profile.webpage === '' }"
                :href="profile.webpage"
                target="_blank"
                rel="noopener"
              >
                <i class="fas fa-address-card"></i> View Page
              </a>

              <router-link
                :to="{ name: 'recommend', params: { id: id } }"
                class="btn pill-btn btn-outline-primary m-1"
              >
                <i class="fas fa-comment"></i> Recommend</router-link
              >
            </div>
          </div>
        </div>
      </div>

      <div id="field-of-research">
        <h5 class="text-primary font-weight-bold mt-5">
          <span class="text-secondary"
            ><i class="fas fa-chevron-circle-right"></i
          ></span>
          Field of Research
        </h5>
        <div
          id="field-of-research-list"
          class="w-100 p-4 mt-3 d-flex flex-row grey-bg rounded"
        >
          <div class="w-25 p-2 text-center">
            <h6 class="text-secondary font-weight-bold">Brain Area</h6>
            <ul class="list-group list-group-flush">
              <li
                v-for="structure in (profile.brain_structure || '').split(',')"
                :key="structure"
                class="list-group-item grey-bg"
                style="border: none; padding: 0;"
              >
                {{ structure }}
              </li>
            </ul>
          </div>
          <div class="w-25 p-2 text-center">
            <h6 class="text-secondary font-weight-bold">Domain</h6>
            <ul class="list-group list-group-flush">
              <li
                v-for="domain in (profile.domains || '').split(',')"
                :key="domain"
                class="list-group-item grey-bg"
                style="border: none; padding: 0;"
              >
                {{ domain }}
              </li>
            </ul>
          </div>
          <div class="w-25 p-2 text-center">
            <h6 class="text-secondary font-weight-bold">Modalities</h6>
            <ul class="list-group list-group-flush">
              <li
                v-for="modality in (profile.modalities || '').split(',')"
                :key="modality"
                class="list-group-item grey-bg"
                style="border: none; padding: 0;"
              >
                {{ modality }}
              </li>
            </ul>
          </div>
          <div class="w-25 p-2 text-center">
            <h6 class="text-secondary font-weight-bold">Methods</h6>
            <ul class="list-group list-group-flush">
              <li
                v-for="method in (profile.methods || '').split(',')"
                :key="method"
                class="list-group-item grey-bg"
                style="border: none; padding: 0;"
              >
                {{ method }}
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div v-if="profile.keywords" id="keywords">
        <h5 class="text-primary font-weight-bold mt-5">
          <span class="text-secondary">
            <i class="fas fa-chevron-circle-right"></i
          ></span>
          Other keywords
        </h5>
        <div class="grey-bg p-4 mt-3 rounded">
          <p>{{ profile.keywords }}</p>
        </div>
      </div>

      <div id="recommendations">
        <h5 class="text-primary font-weight-bold mt-5">
          <span class="text-secondary">
            <i class="fas fa-chevron-circle-right"></i
          ></span>
          Recommendations
        </h5>
        <!--<div class="col-12 col-md-4 text-right pt-3 pr-4">
                <a class="btn pill-btn text-white btn-primary" href="{% url 'profiles:recommend_profile' profile.id %}" target="_blank">Recommend</a>
            </div>-->
        <div v-if="profile.recommendations">
          <span class="text-primary float-right" style="margin-top:-34px;"
            ><i class="fas fa-comment num-rec"></i>
            {{ profile.recommendations.length }}</span
          >
          <ul id="profile-quotes" class="list-unstyled">
            <li
              v-for="recommendation in profile.recommendations"
              :key="recommendation.id"
              class="quote grey-bg p-4 mt-3 rounded"
            >
              <h5 class="quote-reviewer text-secondary font-weight-bold">
                {{ recommendation.reviewer_name }}
                <small
                  >({{ recommendation.reviewer_position }} -
                  {{ recommendation.reviewer_institution }})</small
                >
                <small class="text-muted float-right quote-date">{{
                  new Date(recommendation.publish_date)
                    | dateFormat('MMM DD, YYYY')
                }}</small>
              </h5>
              <blockquote>
                <p>{{ recommendation.comment }}</p>
              </blockquote>
            </li>
          </ul>
          <div class="d-flex justify-content-end">
            <router-link
              :to="{ name: 'recommend', params: { id: id } }"
              class="btn pill-btn btn-outline-primary m-1"
            >
              <i class="fas fa-comment"></i> Recommend</router-link
            >
          </div>
        </div>
        <div v-else class="m-1 pt-4">
          <p>No recommendations have been made for {{ profile.name }} yet.</p>
          <p>
            Have you seen her at a conference? If so, please consider
            <router-link :to="{ name: 'recommend', params: { id: id } }">
              <b>writing her one.</b>
            </router-link>
            <!-- <b><a href="/list/recommend" target="_blank">writing her one.</a></b> -->
          </p>
        </div>
        <p class="m-1"></p>
      </div>

      <div class="mt-5">
        <p class="m-1 text-muted small">
          Noticed something incorrect in your profile?
          <a
            :href="
              encodeURI(
                `mailto:admin@winrepo.org?subject=Winrepo - update profile ${profile.id} (${profile.name})`
              )
            "
          >
            <b>Send us an email</b>
          </a>
          with instructions so we can update it!
        </p>
      </div>

      <div id="results-nav" class="border-top pt-2 mt-4 w-100 text-muted">
        <div class="float-left">
          <router-link
            :to="{ name: 'list' }"
            class="btn btn-outline-primary pill-btn m-1"
          >
            Back to List
          </router-link>
          <!-- <a class="btn btn-outline-primary pill-btn m-1" href="{% url 'profiles:index' %}">Back to list</a> -->
        </div>
        <!-- <div id="filtered-list-navigation" class="float-right" style="display:none;">
                <ul class="nav justify-content-end">
                    <li>
                        <a id="previous-btn" class="btn btn-outline-primary pill-btn m-1 disabled" href="#">Previous</a>
                    </li>
                    <li><span id="page-number" class="m-1 ml-2 mr-2">Result <span id="current-result" class="text-secondary font-weight-bold"></span> of <span id="total-results"></span></span></li>
                    <li>
                        <a id="next-btn" class="btn btn-outline-primary pill-btn m-1 disabled" href="#">Next</a>
                    </li>
                </ul>
            </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from '../common/api_service';

export default {
  name: 'Profile',
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      profile: {}
    };
  },
  methods: {
    setTitle(title) {
      document.title = title;
    },
    getProfilesDetails() {
      const endpoint = `/api/profiles/${this.id}/`;
      apiService(endpoint).then(data => {
        this.profile = data;
      });
    }
  },
  created() {
    this.getProfilesDetails();
    this.setTitle(`Winrepo - ${this.profile.name}`);
  }
};
</script>

<style scoped>
#list-search {
  height: 216px;
  margin-bottom: -150px;
}
</style>
