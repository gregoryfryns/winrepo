<template>
  <div class="home">
    <div class="container-fluid p-0">
      <picture id="hero-image">
        <source srcset="../assets/banner2-1600.webp" type="image/webp" />
        <source srcset="../assets/banner2.jpg" type="image/jpeg" />
        <img src="../assets/banner2.jpg" alt="Header Image" />
      </picture>
    </div>
    <div class="container-fluid" id="home-search">
      <form
        action="list"
        method="get"
        class="input-group bg-white rounded p-1 mx-auto"
      >
        <input
          type="text"
          id="search-input"
          class="form-control"
          placeholder="Enter search keywords here..."
          aria-label="Search"
          name="s"
          autofocus
        />
        <button
          type="submit"
          id="search-btn"
          class="btn btn-secondary pl-4 pr-4"
        >
          Search
        </button>
      </form>
    </div>
    <div
      class="container-fluid bg-primary text-white pt-5 pb-5"
      id="intro-container"
    >
      <div class="row no-gutters p-4">
        <div class="col-md-4 offset-md-4 text-center">
          <h1 class="headtitle">
            <span class="women">Women</span> in Neuroscience
          </h1>
        </div>
      </div>
      <div class="row no-gutters p-4">
        <div class="col-md-10 offset-md-1" id="intro-text">
          <p class="h5 text-justify">
            Despite some effort from the community and
            <a class="text-quinary" href="/faq#heading-resources"
              >great initiatives</a
            >, female neuroscientists
            <a
              class="text-quinary"
              href="https://onlinelibrary.wiley.com/doi/abs/10.1111/ejn.14397"
              target="_blank"
              rel="noopener"
              >are still under-represented in neuroscience</a
            >. The aim of this Women in Neuroscience Repository is to help you
            identify and recommend female neuroscientists for conferences,
            symposia or collaborations.
          </p>
        </div>
      </div>
      <div class="d-flex flex-wrap justify-content-around header-buttons">
        <div class="m-2">
          <router-link
            class="btn pill-btn header-btn text-white"
            :to="{ name: 'list' }"
          >
            View Repository
          </router-link>
        </div>
        <div class="m-2">
          <router-link
            class="btn pill-btn header-btn text-white"
            :to="{ name: 'create' }"
          >
            Create Profile
          </router-link>
        </div>
        <div class="m-2">
          <router-link
            class="btn pill-btn header-btn text-white"
            :to="{ name: 'recommend' }"
          >
            Recommend
          </router-link>
        </div>
      </div>
    </div>

    <div
      id="reco-carousel"
      class="container-fluid carousel bg-light slide"
      data-ride="carousel"
      data-interval="60000"
    >
      <ol class="carousel-indicators">
        <li
          v-for="(reco, index) in recommendationsSample"
          data-target="#reco-carousel"
          :key="reco.id"
          :class="{ active: index === 0 }"
          :data-slide-to="index"
        ></li>
      </ol>
      <div class="carousel-inner m-auto">
        <div
          v-for="(reco, index) in recommendationsSample"
          class="carousel-item p-4"
          :class="{ active: index === 0 }"
          :key="reco.id"
        >
          <span class="text-secondary quote-icon float-left m-2"
            ><i class="fas fa-quote-left"></i
          ></span>
          <blockquote class="blockquote text-center m-2">
            <p class="mb-0">
              {{
                reco.comment.length > 255
                  ? reco.comment.slice(0, 255) + '...'
                  : reco.comment
              }}
            </p>
            <footer class="blockquote-footer">
              {{ reco.reviewer_name }}, about
              <a class="text-primary" href="list/">{{ reco.profile.name }}</a>
            </footer>
          </blockquote>
        </div>
      </div>
      <a
        class="carousel-control-prev"
        href="#reco-carousel"
        role="button"
        data-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a
        class="carousel-control-next"
        href="#reco-carousel"
        role="button"
        data-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>

    <div class="container-fluid" id="stats">
      <div class="text-center m-4" id="entries-container">
        <p class="h1 text-secondary font-weight-bold mb-0">{{ nbProfiles }}</p>
        <p class="h5 text-primary" id="entries-text">entries in repository. </p>
      </div>
      <div class="d-flex flex-wrap justify-content-center align-items-start m-4" id="chart-stats">
        <div
          v-for="(donut, i) in donutCharts"
          :key="`donut_${i}`"
          class="p-2 text-center donutTab">
          <table>
            <tr>
              <td class="donutCell">
                <!-- <div class="donutDiv"></div> -->
                <GChart
                 type="PieChart"
                 :data="[
                  ['Position', 'Entries in Repository'],
                  [donut.label, donut.count],
                  ['Rest', nbProfiles - donut.count]
                  ]"
                 :options="{
                    colors: ['#dedede', '#dedede'],
                    fontName: 'Open Sans',
                    fontSize: 14,
                    chartArea: { left: '10%', top: 0, width: '80%', height: '100%' },
                    width: 120,
                    height: 120,
                    legend: 'none',
                    pieSliceText: 'none',
                    pieHole: 0.6,
                    enableInteractivity: false,
                    slices: [{ color: donut.color, textStyle: { color: '#555555', fontName: 'Open Sans', fontSize: 18 } },
                    { textStyle: { color: '#ffffff', fontName: 'Open Sans', fontSize: 1 } }]
                  }"
                />
                <div class="donutValue">{{ (100 * donut.count/nbProfiles).toFixed(0) }}%</div>
              </td>
            </tr>
          </table>
          <span :style="{ color: donut.color || '#999999' }" class="position-title">{{ donut.label }}</span>
          <p class="position-text">{{ donut.count }} profiles</p>
        </div>
      </div>
      <div class="row no-gutters m-4" id="country-stats">
        <div class="col-12 col-md-8 offset-md-2 m-auto" id="map-container">
          <GChart
            :settings="{ 'packages': ['corechart', 'geochart'], 'mapsApiKey': 'AIzaSyCoD-FXcgIKxspIjalcutPYjaSK1B1WmXc' }"
            type="GeoChart"
            :data="mapChart.data"
            :options="mapChart.options"
          />
        </div>
      </div>
    </div>
    <!-- <div class="container-fluid">
      <div class="row no-gutters m-4 pt-4">
        <div class="col-12 col-md-8 offset-md-2 text-center">
          <h2 class="text-secondary">Going to a conference soon?</h2>
          <p class="text-dark text-justify">Download our slide and insert it at the end of your presentation!
            It will raise awareness on the issue of gender equity in neuroscience and show that there are resources to
            help conference organizers. In addition, it will encourage researchers to submit recommendations of their peers.</p>
          <a :href="require('../assets/slide_May2019.pdf')" id="download-slide" class="btn pill-btn slide-btn text-white btn-secondary" download="WiNRepo_Slide">Download slide</a>
        </div>
      </div>
    </div> -->
  </div>
</template>

<script>
import { GChart } from 'vue-google-charts';
import { apiService } from '../common/api_service';

export default {
  name: 'home',
  components: {
    GChart
  },
  data() {
    return {
      recommendationsSample: [],
      mapChart: {
        data: [],
        options: {
          colorAxis: { colors: ['#a0c1c1', '#10898B'] },
          legend: 'none',
          tooltip: { isHtml: false }
        }
      },
      donutCharts: [],
      nbProfiles: 0
    };
  },
  methods: {
    getRecommendationsSample() {
      const endpoint = 'api/recommendations-sample/';
      apiService(endpoint).then(data => {
        this.recommendationsSample.push(...data);
      });
    },
    getMapChartData() {
      const endpoint = '/api/top-countries/';
      apiService(endpoint).then(data => {
        const array = data.map(country => [country.name, country.profiles_count]);
        array.unshift(['Country', '# Profiles']);
        this.mapChart.data = array;
      });
    },
    getPositionsData() {
      const endpoint = '/api/top-positions/';
      apiService(endpoint).then(data => {
        const seniorRe = /senior|lecturer|professor|director|principal/i;
        const postdocRe = /post-doc/i;
        const studentRe = /phd\sstudent/i;

        let totProfiles = 0;
        const profiles = {
            'senior': 0,
            'postdoc': 0,
            'student': 0,
            'other': 0
        }
        for (let pos of data) {
          totProfiles += pos.profiles_count;
          if (pos.position.match(seniorRe)) {
              profiles.senior += pos.profiles_count;
          }
          else if (pos.position.match(postdocRe)) {
              profiles.postdoc += pos.profiles_count;
          }
          else if (pos.position.match(studentRe)) {
              profiles.student += pos.profiles_count;
          }
          else {
              profiles.other += pos.profiles_count;
          }
        };

        this.nbProfiles = totProfiles;

        this.donutCharts.push({ label: 'PhD', count: profiles.student, color: '#CC063E' });
        this.donutCharts.push({ label: 'Post-doc', count: profiles.postdoc, color: '#E83535' });
        this.donutCharts.push({ label: 'Senior', count: profiles.senior, color: '#FD9407' });
        this.donutCharts.push({ label: 'Other', count: profiles.other, color: '#999999' });

   // const array = data.map(country => [country.name, country.profiles_count]);
        // array.unshift(['Country', '# Profiles']);
        // this.mapChart.data = array;
      });
    }
  },
  created() {
    this.getRecommendationsSample();
    this.getMapChartData();
    this.getPositionsData();
    document.title = 'Winrepo';
  }
};
</script>

<style scoped>
.container-fluid {
  font-size: 16px;
}

#hero-image > img {
  width: 100vw;
  padding-top: 28px;
  /* min-height: 200px; */
}

#home-search {
  height: 0;
}

#home-search > form {
  transform: translate(0, -50%);
  max-width: 600px;
}

#home-search input {
  border: none;
}

#home-search input:focus {
  box-shadow: none;
}

.headtitle {
  font-family: 'Nunito', sans-serif;
}

.headtitle > .women {
  font-family: 'Pacifico', sans-serif;
  color: #cc063e;
  font-size: 3rem;
  text-shadow: 0px 0px 1px white;
}

#intro-text {
  max-width: 800px;
  margin: auto;
}

.pill-btn {
  padding: 12px 0;
  border-radius: 50px;
  width: 160px;
}

.header-buttons {
  max-width: 600px;
  margin: auto;
}

.header-btn {
  border-color: white;
}

.header-btn:hover {
  background-color: rgba(255, 255, 255, 0.12);
  color: white;
}

#reco-carousel {
  min-height: 240px;
}

.carousel-inner {
  max-width: 800px;
}
.carousel-control-next,
.carousel-control-prev,
.carousel-indicators {
  filter: invert(50%);
}

.quote-icon {
  font-size: 0.8em;
}

/* Stats */
.donutCell
{
    position: relative;
}

.donutValue
{
    position: absolute;
    left: 50%;
    top: 50%;
	transform: translate(-50%,-50%);
	-ms-transform: translate(-50%,-50%);
    text-align: center;
    font-size: 16px;
    color: #555555;
}

.position-title {
	font-size: 18px;
	font-weight: bold;
}

.position-text {
	font-size: 14px;
	color: #555555;
}

#map-container > div {
  max-width: 800px;
  margin: auto;
}
</style>
