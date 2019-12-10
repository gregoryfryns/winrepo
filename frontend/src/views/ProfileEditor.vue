<template>
  <div
    id="profile-editor"
    class="bg-white rounded-top p-4 pt-5 offset-md-1 col-md-10 offset-lg-2 col-lg-8"
  >
    <div v-if="error" class="alert alert-danger">
      <strong>{{ error }}</strong>
    </div>
    <form @submit.prevent="onSubmit">
      <ValidationProvider name="name" rules="required" v-slot="{ errors }">
        <div class="form-group">
          <label for="id_name" class="required">Full Name</label>
          <span class="asterisk">*</span>
          <div>
            <input
              v-model="fields.name"
              type="text"
              name="name"
              maxlength="100"
              class="textinput textInput form-control"
              :class="{
                'is-invalid': errors.length > 0 || fieldsErrors['name']
              }"
              id="id_name"
            />
            <p id="error_id_name" class="invalid-feedback">
              <strong v-if="fieldsErrors['name']">{{
                fieldsErrors['name'][0]
              }}</strong>
              <strong v-else-if="errors">{{ errors[0] }}</strong>
            </p>
          </div>
        </div>
      </ValidationProvider>
      <ValidationProvider
        name="institution"
        rules="required"
        v-slot="{ errors }"
      >
        <div class="form-group">
          <label for="id_institution" class="required"
            >Institution/Company</label
          >
          <span class="asterisk">*</span>
          <div>
            <input
              v-model="fields.institution"
              type="text"
              name="institution"
              maxlength="100"
              class="textinput textInput form-control"
              :class="{ 'is-invalid': errors.length > 0 }"
              id="id_institution"
            />
            <p id="error_id_institution" class="invalid-feedback">
              <strong>{{ errors[0] }}</strong>
            </p>
          </div>
        </div>
      </ValidationProvider>
      <ValidationProvider name="country" rules="required" v-slot="{ errors }">
        <div class="form-group">
          <label for="country" class="control-label required">
            Country
          </label>
          <span class="asterisk">*</span>
          <v-select
            class="vue-select2"
            :class="{ 'is-invalid': errors.length > 0 }"
            name="country"
            :options="countriesList"
            label="name"
            :reduce="country => country.id"
            :searchable="true"
            :filterable="true"
            :clearable="false"
            :select-on-tab="true"
            v-model="fields.country"
          />
          <p id="error_id_country" class="invalid-feedback">
            <strong>{{ errors[0] }}</strong>
          </p>
          <small id="hint_id_country" class="form-text text-muted">
            Country of the institution
          </small>
        </div>
      </ValidationProvider>
      <ValidationProvider name="country" rules="" v-slot="{ errors }">
        <div class="form-group">
          <label for="country" class="control-label">
            Position
          </label>
          <v-select
            class="vue-select2"
            :class="{ 'is-invalid': errors.length > 0 }"
            name="position"
            :options="positionsChoices"
            :clearable="false"
            :select-on-tab="true"
            label="name"
            v-model="fields.position"
          />
          <p id="error_id_position" class="invalid-feedback">
            <strong>{{ errors[0] }}</strong>
          </p>
          <small id="hint_id_position" class="form-text text-muted">
            Please choose your 'highest' title from the proposed options to ease
            future searches.
          </small>
        </div>
      </ValidationProvider>
      <ValidationProvider
        name="contact_email"
        rules="required|email"
        v-slot="{ errors }"
      >
        <div class="form-group">
          <label for="id_contact_email" class="required">Email Address</label>
          <span class="asterisk">*</span>
          <div class>
            <input
              v-model="fields.contact_email"
              type="email"
              name="contact_email"
              maxlength="254"
              class="emailinput form-control"
              :class="{ 'is-invalid': errors.length > 0 }"
              id="id_contact_email"
            />
            <p id="error_id_contact_email" class="invalid-feedback">
              <strong>{{ errors[0] }}</strong>
            </p>
            <small id="hint_id_contact_email" class="form-text text-muted">
              Email Address that will be shown to the people who look at your
              profile.
            </small>
          </div>
        </div>
      </ValidationProvider>
      <ValidationProvider name="webpage" v-slot="{ errors }">
        <div class="form-group">
          <label for="id_webpage">LinkedIn or web page</label>
          <div>
            <input
              v-model="fields.webpage"
              type="url"
              name="webpage"
              maxlength="200"
              class="urlinput form-control"
              :class="{ 'is-invalid': errors.length > 0 }"
              id="id_webpage"
            />
            <p id="error_id_webpage" class="invalid-feedback">
              <strong>{{ errors[0] }}</strong>
            </p>
            <small id="hint_id_webpage" class="form-text text-muted">
              Make sure people can look you up easily by providing a link to a
              personal website, profile or institution site.
            </small>
          </div>
        </div>
      </ValidationProvider>
      <div class="form-row">
        <div class="form-group col-md-6 mb-0">
          <ValidationProvider name="grad_month" v-slot="{ errors }">
            <div class="form-group">
              <label for="id_grad_month" class
                >Date PhD was obtained: Month</label
              >
              <div class>
                <v-select
                  class="vue-select2"
                  :class="{ 'is-invalid': errors.length > 0 }"
                  name="grad_month"
                  :options="monthsChoices"
                  :clearable="true"
                  :select-on-tab="true"
                  :reduce="month => month.value"
                  label="display_name"
                  v-model="fields.grad_month"
                />
                <p id="error_id_grad_month" class="invalid-feedback">
                  <strong>{{ errors[0] }}</strong>
                </p>
                <small id="hint_id_grad_month" class="form-text text-muted"
                  >Leave empty if no PhD (yet).</small
                >
              </div>
            </div>
          </ValidationProvider>
        </div>
        <div class="form-group col-md-6 mb-0">
          <ValidationProvider name="grad_year" v-slot="{ errors }">
            <div class="form-group">
              <label for="id_grad_year" class>Year</label>
              <div class>
                <input
                  v-model="fields.grad_year"
                  type="text"
                  name="grad_year"
                  maxlength="4"
                  class="textinput textInput form-control"
                  :class="{ 'is-invalid': errors.length > 0 }"
                  id="id_grad_year"
                />
                <p id="error_id_grad_year" class="invalid-feedback">
                  <strong>{{ errors[0] }}</strong>
                </p>
                <small id="hint_id_grad_year" class="form-text text-muted"
                  >Please enter the full year (4 digits).</small
                >
              </div>
            </div>
          </ValidationProvider>
        </div>
      </div>
      <div class="form-group">
        <label for="" class="">
          Field of Research - Brain Structure
        </label>
        <div class="">
          <div
            v-for="(struct, i) in brainStructureChoices"
            :key="struct.value"
            class="form-check custom-checkbox"
          >
            <input
              v-model="fields.brain_structure"
              type="checkbox"
              class="form-check-input custom-control-input"
              name="brain_structure"
              :id="`id_brain_structure_${i + 1}`"
              :value="struct.value"
            />
            <label
              class="form-check-label custom-control-label"
              :for="`id_brain_structure_${i + 1}`"
            >
              {{ struct.display_name }}
            </label>
          </div>
        </div>
      </div>
      <div class="form-group">
        <label for="" class="">
          Field of Research - Modalities
        </label>
        <div class="">
          <div
            v-for="(modality, i) in modalitiesChoices"
            :key="modality.value"
            class="form-check custom-checkbox"
          >
            <input
              v-model="fields.modalities"
              type="checkbox"
              class="form-check-input custom-control-input"
              name="modalities"
              :id="`id_modalities_${i + 1}`"
              :value="modality.value"
            />
            <label
              class="form-check-label custom-control-label"
              :for="`id_modalities_${i + 1}`"
            >
              {{ modality.display_name }}
            </label>
          </div>
        </div>
      </div>
      <div class="form-group">
        <label for="" class="">
          Field of Research - Methods
        </label>
        <div class="">
          <div
            v-for="(method, i) in methodsChoices"
            :key="method.value"
            class="form-check custom-checkbox"
          >
            <input
              v-model="fields.methods"
              type="checkbox"
              class="form-check-input custom-control-input"
              name="methodsList"
              :id="`id_methodsList_${i + 1}`"
              :value="method.value"
            />
            <label
              class="form-check-label custom-control-label"
              :for="`id_methodsList_${i + 1}`"
            >
              {{ method.display_name }}
            </label>
          </div>
        </div>
      </div>
      <div class="form-group">
        <label for="" class="">
          Field of Research - Domains
        </label>
        <div class="">
          <div
            v-for="(domain, i) in domainsChoices"
            :key="domain.value"
            class="form-check custom-checkbox"
          >
            <input
              v-model="fields.domains"
              type="checkbox"
              class="form-check-input custom-control-input"
              name="domains"
              :id="`id_domains_${i + 1}`"
              :value="domain.value"
            />
            <label
              class="form-check-label custom-control-label"
              :for="`id_domains_${i + 1}`"
            >
              {{ domain.display_name }}
            </label>
          </div>
        </div>
      </div>
      <ValidationProvider name="institution" rules="" v-slot="{ errors }">
        <div class="form-group">
          <label for="id_keywords">
            Field of Research - Other Keywords
          </label>
          <div>
            <input
              v-model="fields.keywords"
              type="text"
              name="keywords"
              maxlength="250"
              class="textinput textInput form-control"
              :class="{ 'is-invalid': errors.length > 0 }"
              id="id_keywords"
            />
            <p id="error_id_keywords" class="invalid-feedback">
              <strong>{{ errors[0] }}</strong>
            </p>
            <small id="hint_id_webpage" class="form-text text-muted">
              Optionally you can add some more specific terms to describe your
              field of research, separated by commas.
            </small>
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
      fields: {
        brain_structure: [],
        modalities: [],
        methods: [],
        domains: []
      },
      fieldsErrors: {},
      error: null,
      brainStructureChoices: [
        { value: 'N', display_name: 'Neuron' },
        { value: 'L', display_name: 'Layer' },
        { value: 'C', display_name: 'Column' },
        { value: 'R', display_name: 'Region' },
        { value: 'W', display_name: 'Whole Brain' }
      ],
      modalitiesChoices: [
        { value: 'EP', display_name: 'Electrophysiology (EEG, MEG, ECoG)' },
        { value: 'OE', display_name: 'Other electrophysiology' },
        { value: 'MR', display_name: 'MRI' },
        { value: 'PE', display_name: 'PET' },
        { value: 'DT', display_name: 'DTI' },
        { value: 'BH', display_name: 'Behavioural' },
        { value: 'ET', display_name: 'Eye Tracking' },
        { value: 'BS', display_name: 'Brain Stimulation' },
        { value: 'GT', display_name: 'Genetics' },
        { value: 'FN', display_name: 'fNIRS' },
        { value: 'LE', display_name: 'Lesions and Inactivations' }
      ],
      methodsChoices: [
        { value: 'UV', display_name: 'Univariate' },
        { value: 'MV', display_name: 'Multivariate' },
        { value: 'PM', display_name: 'Predictive Models' },
        { value: 'DC', display_name: 'DCM' },
        { value: 'CT', display_name: 'Connectivity' },
        { value: 'CM', display_name: 'Computational Modeling' },
        { value: 'AM', display_name: 'Animal Models' }
      ],
      domainsChoices: [
        { value: 'CG', display_name: 'Cognition (general)' },
        { value: 'MM', display_name: 'Memory' },
        { value: 'SS', display_name: 'Sensory systems' },
        { value: 'MO', display_name: 'Motor Systems' },
        { value: 'LG', display_name: 'Language' },
        { value: 'EM', display_name: 'Emotion' },
        { value: 'PN', display_name: 'Pain' },
        { value: 'LE', display_name: 'Learning' },
        { value: 'AT', display_name: 'Attention' },
        { value: 'DE', display_name: 'Decision Making' },
        { value: 'DV', display_name: 'Developmental' },
        { value: 'SL', display_name: 'Sleep' },
        { value: 'CN', display_name: 'Consciousness' },
        { value: 'CL', display_name: 'Clinical (general)' },
        { value: 'DM', display_name: 'Dementia' },
        { value: 'PK', display_name: 'Parkinson' },
        { value: 'DD', display_name: 'Other degenerative diseases' },
        { value: 'PS', display_name: 'Psychiatry' },
        { value: 'AD', display_name: 'Addiction' },
        { value: 'ON', display_name: 'Oncology' },
        { value: 'EV', display_name: 'Evolutionary' },
        { value: 'CM', display_name: 'Cellular and Molecular' },
        { value: 'BI', display_name: 'Bioinformatics' },
        { value: 'NC', display_name: 'Neuropharmacology' },
        { value: 'ET', display_name: 'Ethics' }
      ],
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
      ],
      monthsChoices: [
        { value: '01', display_name: 'January' },
        { value: '02', display_name: 'February' },
        { value: '03', display_name: 'March' },
        { value: '04', display_name: 'April' },
        { value: '05', display_name: 'May' },
        { value: '06', display_name: 'June' },
        { value: '07', display_name: 'July' },
        { value: '08', display_name: 'August' },
        { value: '09', display_name: 'September' },
        { value: '10', display_name: 'October' },
        { value: '11', display_name: 'November' },
        { value: '12', display_name: 'December' }
      ],
      countriesList: []
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
      const endpoint = '/api/profiles/';
      const method = 'POST';
      const content = this.fields;

      apiService(endpoint, method, content)
        .then(profile_data => {
          if (profile_data.id) {
            this.$router.push({
              name: 'profile',
              params: { id: profile_data.id.toString() }
            });
          } else {
            this.error = 'Could not create profile :(';
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
    loadCountriesList() {
      apiService('/api/countries-lookup/').then(data => {
        if (data instanceof Array) {
          this.countriesList = data;
        }
      });
    }
  },
  created() {
    document.title = 'Winrepo - Edit Profile';
    this.loadCountriesList();
  }
};
</script>

<style scoped></style>
