<template>
  <div
    id="recommendation-editor"
    class="bg-white rounded-top p-4 pt-5 offset-md-1 col-md-10 offset-lg-2 col-lg-8"
  >
    <div v-if="error" class="alert alert-danger">
      <strong>{{ error }}</strong>
    </div>
    <form @submit.prevent="onSubmit">
      <v-select
        label="name"
        :filterable="false"
        :clearable="false"
        :select-on-tab="true"
        :options="profiles_list"
        :reduce="profile => profile.id"
        @search="onProfileSearch"
        v-model="fields.profile">
        <template slot="no-options">
          type to search profiles..
        </template>
        <template slot="option" slot-scope="option">
          <div class="d-center">
            {{ option.name }} <small class="text-muted">{{ option.institution }}</small>
            </div>
        </template>
        <template slot="selected-option" slot-scope="option">
          <div class="selected d-center">
             {{ option.name }} <small class="text-muted">{{ option.institution }}</small>
          </div>
        </template>
      </v-select>
      <ValidationProvider name="reviewer_name" rules="required" v-slot="{ errors }">
        <div class="form-group">
          <label for="id_reviewer_name" class="required">Your Full Name</label>
          <span class="asterisk">*</span>
          <div>
            <input
              v-model="fields.reviewer_name"
              type="text"
              name="reviewer_name"
              maxlength="100"
              class="textinput textInput form-control"
              :class="{
                'is-invalid': errors.length > 0 || fieldsErrors['reviewer_name']
              }"
              id="id_reviewer_name"
            />
            <p id="error_id_reviewer_name" class="invalid-feedback">
              <strong v-if="fieldsErrors['reviewer_name']">{{
                fieldsErrors['reviewer_name'][0]
              }}</strong>
              <strong v-else-if="errors">{{ errors[0] }}</strong>
            </p>
          </div>
        </div>
      </ValidationProvider>
      <ValidationProvider
        name="reviewer_institution"
        rules="required"
        v-slot="{ errors }"
      >
        <div class="form-group">
          <label for="id_reviewer_institution" class="required"
            >Your Institution/Company</label>
          <span class="asterisk">*</span>
          <div>
            <input
              v-model="fields.reviewer_institution"
              type="text"
              name="reviewer_institution"
              maxlength="100"
              class="textinput textInput form-control"
              :class="{ 'is-invalid': errors.length > 0 }"
              id="id_reviewer_institution"
            />
            <p id="error_id_reviewer_institution" class="invalid-feedback">
              <strong>{{ errors[0] }}</strong>
            </p>
          </div>
        </div>
      </ValidationProvider>

      <button type="submit" class="btn btn-primary pill-btn">Submit</button>
    </form>
  </div>
</template>

<script>
import { ValidationProvider, extend } from 'vee-validate';
import { required, email, max } from 'vee-validate/dist/rules';
import { debounce } from 'debounce';
import { apiService } from '../common/api_service';

extend('required', {
  ...required,
  message: 'This field is required'
});

extend('email', {
  ...email,
  message: 'Please enter a valid email address'
});

extend('max', max);

export default {
  name: 'ProfileEditor',
  components: {
    ValidationProvider
  },
  data() {
    return {
      fields: {},
      fieldsErrors: {},
      error: null,
      profiles_list: []
    };
  },
  computed: {
    formValid() {
      // loop over all contents of the fields object and check if they exist and valid.
      return Object.keys(this.fields).every(field => {
        return this.fields[field] && this.fields[field].valid;
      });
    }
  },
  methods: {
    onSubmit() {
      // check if input valid
      // if (!this.formValid) {
      //   console.log('bouhouhou');
      //   return;
      // }

      const endpoint = '/api/recommendations/';
      const method = 'POST';
      const content = this.fields;
      apiService(endpoint, method, content)
        .then(reco_data => {
          if (reco_data && reco_data.profile) {
            this.$router.push({
              name: 'profile',
              params: { id: reco_data.profile.id }
            });
          } else {
            this.error = 'Could not create recommendation :(';
            this.fieldsErrors = profile_data;
          }
        })
        .catch(err => {
          console.log('error: ', JSON.stringify(err));
          this.loaded = true;
          if (err.response.status === 400) {
            // this.errors = error.response.data.errors || {};
            this.fieldsErrors = err.response.data.errors || '';
          }
        });
    },
    onProfileSearch(search, loading) {
      if (search.length > 1) {
        loading(true);
        this.search(loading, search, this);
      }
    },
    search: debounce((loading, search, vm) => {
      apiService(`/api/profiles-lookup/?q=${encodeURIComponent(search)}`)
        .then(data => {
          vm.profiles_list = data;
          loading(false);
        });
      }, 350)
  },
  created() {
    document.title = 'Winrepo - Edit Recommendation';
  }
};
</script>

<style scoped>

</style>
