<template>
  <div
    id="recommendation-editor"
    class="bg-white rounded-top p-4 pt-5 offset-md-1 col-md-10 offset-lg-2 col-lg-8"
  >
    <div v-if="error" class="alert alert-danger">
      <strong>{{ error }}</strong>
    </div>
    <form @submit.prevent="onSubmit">
      <div class="form-group">
        <ValidationProvider name="profile" rules="required" v-slot="{ errors }">
            <label for="id_profile" class="required">Recommended Person</label>
            <span class="asterisk">*</span>
        <v-select
            label="name"
            id="id_profile"
            :filterable="false"
            :clearable="false"
            :select-on-tab="true"
            :options="profiles_list"
            @search="onProfileSearch"
            v-model="profile"
          >
            <template slot="no-options">
              type to search profiles..
            </template>
            <template slot="option" slot-scope="option">
              <div class="d-center">
                {{ option.name }}
                <small class="text-muted">{{ option.institution }}</small>
              </div>
            </template>
            <template slot="selected-option" slot-scope="option">
              <div class="selected d-center">
                {{ option.name }}
                <small class="text-muted">{{ option.institution }}</small>
              </div>
            </template>
          </v-select>
          <small id="hint_id_profile" class="form-text text-muted">Name of the person you would like to recommend</small>
          <p id="error_id_reviewer_name" class="invalid-feedback">
            <strong v-if="errors">{{ errors[0] }}</strong>
          </p>
        </ValidationProvider>
      </div>
      <div class="form-group">
        <ValidationProvider
          name="reviewer_name"
          rules="required"
          v-slot="{ errors }"
        >
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
      </div>
      <div class="form-row">
        <div class="form-group col-md-6 mb-0">
          <ValidationProvider
            name="reviewer_position"
            rules="required"
            v-slot="{ errors }"
          >
            <div class="form-group">
              <label for="id_reviewer_position" class="required"
                >Your Position</label
              >
              <span class="asterisk">*</span>
              <v-select
                class="vue-select2"
                :class="{ 'is-invalid': errors.length > 0 }"
                name="reviewer_position"
                :options="positionsChoices"
                :clearable="false"
                :select-on-tab="true"
                label="name"
                v-model="fields.reviewer_position"
              />
              <div>
                <!-- <input
                  v-model="fields.reviewer_position"
                  type="text"
                  name="reviewer_position"
                  maxlength="100"
                  class="textinput textInput form-control"
                  :class="{ 'is-invalid': errors.length > 0 }"
                  id="id_reviewer_position"
                /> -->
                <small id="hint_id_reviewer_position" class="form-text text-muted">Please choose the 'closest' title from the proposed options.</small>
                <p id="error_id_reviewer_position" class="invalid-feedback">
                  <strong>{{ errors[0] }}</strong>
                </p>
              </div>
            </div>
          </ValidationProvider>
        </div>
        <div class="form-group col-md-6 mb-0">
          <ValidationProvider
            name="reviewer_institution"
            rules="required"
            v-slot="{ errors }"
          >
            <div class="form-group">
              <label for="id_reviewer_institution" class="required"
                >Your Institution/Company</label
              >
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
        </div>
      </div>
      <div class="form-group">
        <ValidationProvider
          name="comment"
          rules="required"
          v-slot="{ errors }"
        >
          <div class="form-group">
            <!-- <label for="id_comment" class="required"
              >Comment</label
            >
            <span class="asterisk">*</span> -->
            <div>
              <textarea
                v-model="fields.comment"
                rows="6"
                placeholder="Enter your comment here..."
                type="text"
                name="comment"
                maxlength="100"
                class="form-control"
                :class="{ 'is-invalid': errors.length > 0 }"
                id="id_comment"
              />
              <p id="error_id_comment" class="invalid-feedback">
                <strong>{{ errors[0] }}</strong>
              </p>
              <small id="hint_id_comment" class="form-text text-muted">Describe here why you recommend this person for conference invitations or collaborations. If you attended one of her talks, add details on the event (year, event name). Please also mention potential conflicts of interest, like personal or professional relationships (friends, colleagues, former PI, ...)</small>
            </div>
          </div>
        </ValidationProvider>
      </div>
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
  props: {
    id: {
      type: String,
      required: false
    }
  },
  components: {
    ValidationProvider
  },
  data() {
    return {
      fields: {},
      profile: null,
      fieldsErrors: {},
      error: null,
      profiles_list: [],
      positionsChoices: [
        'PhD student',
        'Medical Doctor',
        'Post-doctoral researcher',
        'Researcher/ scientist',
        'Senior researcher/ scientist',
        'Lecturer',
        'Assistant Professor',
        'Associate Professor',
        'Professor',
        'Group leader/ Director/ Head of Department'
      ]
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
    getProfilesDetails() {
      const endpoint = `/api/profiles/${this.id}/`;
      apiService(endpoint).then(data => {
        this.profile = (({id, name, institution }) => ({id: id, name: name, institution: institution}))(data);
      });
    },
    onSubmit() {
      // check if input valid
      // if (!this.formValid) {
      //   console.log('bouhouhou');
      //   return;
      // }

      const endpoint = `/api/profiles/${this.profile_id}/recommend/`;
      const method = 'POST';
      const content = this.fields;
      apiService(endpoint, method, content)
        .then(response_data => {
          if (response_data && this.profile) {
            this.$router.push({
              name: 'profile',
              params: { id: this.profile.id }
            });
          } else {
            this.error = 'Could not create recommendation :(';
            this.fieldsErrors = profile_data;
          }
        })
        .catch(err => {
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
      apiService(`/api/profiles-lookup/?q=${encodeURIComponent(search)}`).then(
        data => {
          vm.profiles_list = data;
          loading(false);
        }
      );
    }, 350)
  },
  created() {
    document.title = 'Winrepo - Edit Recommendation';
    if (this.id) {
      this.getProfilesDetails();
    }
  }
};
</script>

<style scoped></style>
