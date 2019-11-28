<template>
  <div class="about">
    <h4>Credits</h4>

    <p> This project would not have been possible without the help of our contributors and sponsors.
    We are especially thankful to those who contributed on their spare time, simply to improve the
        visibility of women in neuroscience.</p>
    <br>

    <h4>Contributors</h4>
    <section id="cont" class="pb-5">
      <div class="container">
        <div class="row">
          <InfoCardComponent
            name="Gregory Fryns"
            role="Implementation"
            description="Gregory is a highly qualified computer science engineer with 10+ years experience in customer support and process improvement."
            imageBaseName="Pic_GF-280"
          />
          <InfoCardComponent
            name="Laetitia Briere"
            role="Design"
            description="Laetitia is a freelance designer based in France. She creates visual identities, including logos, flyers, posters, websites, based on the unique needs of her clients. To find out more, see her portfolio at <a href='https://www.lbgraphiste.fr'>www.lbgraphiste.fr</a>"
            imageBaseName="Pic_LB-280"
          />
          <InfoCardComponent
            name="Laura Symul"
            role="Illustrations"
            description="Laura has worked as a data scientist, done data visualisations and science communication for the industry, international organisations and academia. Her freelance activities include workshops, training and consulting on data visualisation and scientific illustration."
            imageBaseName="Pic_LS-280"
          />
          <InfoCardComponent
            name="Diana Sousa"
            role="Logo"
            description="Diana is a Graduate Student Researcher at Faculty of Sciences, University of Lisbon and has been working in a few projects as a Graphic Designer."
            imageBaseName="Pic_DS-280"
          />
          <InfoCardComponent
            name="Jessica Schrouff"
            role="Founder"
            description="Jessica graduated in Electrical Engineering from the University of Liège, Belgium. She studied the application of machine learning methods to neuroimaging data during her PhD (Belgium) and post-doctoral work (Stanford, USA and UCL, UK). She is now working in industry."
            imgBasePath="Pic_JS-280"
          />
        </div>
      </div>
    </section>

    <h4>Board</h4>
    <section id="board" class="pb-5">
        <div class="container">
          <div class="row">
            <InfoCardComponent
              name="Gregory Fryns"
              role="Implementation"
              description="Gregory is a highly qualified computer science engineer with 10+ years experience in customer support and process improvement."
              imageBaseName="Pic_GF-280"
            />
          </div>
      </div>
    </section>

    <h4>Sponsors</h4>
    <ul>
      <li>Athena SWAN committee at the Computer Science Department, University College London</li>
      <li>Marie Curie Alumni Association: micro-grant to J.S.</li>
    </ul>

    <h4>Scientific sponsors</h4>
    <ul>
      <li><a href="https://biaswatchneuro.com/">Bias Watch Neuro</a></li>
    </ul>

    <h4>Acknowledgments</h4>
    <ul>
      <li><a href="https://brainthemind.com/vvw/">Virginie van Wassenhove</a></li>
      <li><a href="https://people.duke.edu/~jmgroh/">Jennifer Groh</a></li>
      <li><a href="http://churchlandlab.labsites.cshl.edu//">Anne Churchland</a></li>
    </ul>
  </div>
</template>

<script>
import InfoCardComponent from "@/components/InfoCard.vue";

export default {
  name: "AboutComponent",
  components: {
    InfoCardComponent
  }
};
</script>

<style scoped>
section .section-title {
  text-align: center;
  text-transform: uppercase;
}

#cont .card {
    width: 12rem;
    height: 16rem;
}

#board .card {
    width: 15rem;
    height: 18rem;
}
</style>
