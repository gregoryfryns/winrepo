<template>
  <div
    id="about"
    class="bg-white rounded-top p-4 pt-5 offset-md-1 col-md-10 offset-lg-2 col-lg-8"
  >
    <h4>Credits</h4>

    <p>
      This project would not have been possible without the help of our
      contributors and sponsors. We are especially thankful to those who
      contributed on their spare time, simply to improve the visibility of women
      in neuroscience.
    </p>
    <br />

    <h4>Contributors</h4>
    <section id="cont" class="pb-5">
      <div class="container">
        <div class="row">
          <InfoCardComponent
            v-for="(contributor, i) in contributors"
            :key="`contributor_${i}`"
            :name="contributor.name"
            :role="contributor.role"
            :description="contributor.description"
            :imageBaseName="contributor.imageBaseName"
          />
        </div>
      </div>
    </section>

    <h4>Board</h4>
    <section id="board" class="pb-5">
      <div class="container">
        <div class="row">
          <InfoCardComponent
            v-for="(member, i) in board"
            :key="`member_${i}`"
            :name="member.name"
            :role="member.role"
            :description="member.description"
            :imageBaseName="member.imageBaseName"
          />
        </div>
      </div>
    </section>

    <h4>Sponsors</h4>
    <ul>
      <li>
        Athena SWAN committee at the Computer Science Department, University
        College London
      </li>
      <li>Marie Curie Alumni Association: micro-grant to J.S.</li>
    </ul>

    <h4>Scientific sponsors</h4>
    <ul>
      <li><a href="https://biaswatchneuro.com/">Bias Watch Neuro</a></li>
    </ul>

    <h4>Acknowledgments</h4>
    <ul>
      <li>
        <a href="https://brainthemind.com/vvw/">Virginie van Wassenhove</a>
      </li>
      <li><a href="https://people.duke.edu/~jmgroh/">Jennifer Groh</a></li>
      <li>
        <a href="http://churchlandlab.labsites.cshl.edu//">Anne Churchland</a>
      </li>
    </ul>
  </div>
</template>

<script>
import InfoCardComponent from '@/components/InfoCard.vue';

export default {
  name: 'About',
  components: {
    InfoCardComponent
  },
  data() {
    return {
      contributors: [
        {
          name: 'Gregory Fryns',
          role: 'Implementation',
          description: 'During the day Gregory works for a tech startup as a Technical Solution Architect. In the evening, he likes to improve his development skills by building websites like this one.',
          imageBaseName: 'Pic_GF-280'
        },
        {
          name: 'Laetitia Briere',
          role: 'Design',
          description: 'Laetitia is a freelance designer based in France. She creates visual identities, including logos, flyers, posters, websites, based on the unique needs of her clients. To find out more, see her portfolio at <a href="https://www.lbgraphiste.fr" target="_blank">www.lbgraphiste.fr</a>',
          imageBaseName: 'Pic_LB-280'
        },
        {
          name: 'Laura Symul',
          role: 'Illustrations',
          description: 'Laura has worked as a data scientist, done data visualisations and science communication for the industry, international organisations and academia. Her freelance activities include workshops, training and consulting on data visualisation and scientific illustration.',
          imageBaseName: 'Pic_LS-280'
        },
        {
          name: 'Diana Sousa',
          role: 'Logo',
          description: 'Diana is a Graduate Student Researcher at Faculty of Sciences, University of Lisbon and has been working in a few projects as a Graphic Designer.',
          imageBaseName: 'Pic_DS-280'
        },
        {
          name: 'Jessica Schrouff',
          role: 'Founder',
          description: 'Jessica graduated in Electrical Engineering from the University of Liège, Belgium. She studied the application of machine learning methods to neuroimaging data during her PhD (Belgium) and post-doctoral work (Stanford, USA and UCL, UK). She is now working in industry.',
          imageBaseName: 'Pic_JS-280'
        }
      ],
      board: [
        {
          name: 'Jessica Schrouff',
          role: 'Machine Learning Research Scientist, London, UK',
          description: `Jessica graduated in Electrical Engineering from the University of Liège, Belgium.
                        She studied the application of machine learning methods to neuroimaging data during her PhD (Belgium) and post-doctoral work (Stanford, USA and UCL, UK). She is now working in industry.`,
          imageBaseName: 'Pic_JS-280'
        },
        {
          name: 'Fabio Ferreira',
          role: 'PhD Candidate at University College London, London, UK',
          description: `Fabio graduated in Biomedical Engineering at University of Coimbra, Portugal. His research interests lie on implementing and applying
                        machine learning-based methods to multiple sources of data to identify biomarkers of mental health disorders and find reliable subgroups of patients.`,
          imageBaseName: 'Pic_FF-280'
        },
        {
          name: 'Sarah Genon',
          role: 'Research fellow at INM-7 at the Forschungszentrum Jülich, Germany',
          description: `Sarah has a background in clinical psychology, cognitive neuroscience and functional neuroanatomy. Her research aims to develop methods
                        for studying and modelling the relationships between brain and behavior in large scale neuroimaging and behavioral data.`,
          imageBaseName: 'Pic_SG-280'
        },
        {
          name: 'Aina Frau-Pascual',
          role: 'Research fellow at the Athinoula A. Martinos Center for Biomedical Imaging, USA',
          description: `Aina is working on the development of methods for diffusion and functional MRI analysis.
                        During her PhD at Inria (France), she developed statistical models for the analysis of BOLD and ASL task fMRI.`,
          imageBaseName: 'Pic_AFP-280'
        },
        {
          name: 'Gabriella Liuzzi',
          role: 'Postdoc at CIMeC in TheFairLab, Mattarello, Italy',
          description: `Gabriella obtained her PhD at KULeuven in the Laboratory for Cognitive Neurology. Her primary research program focuses
                        on the semantic representations of written words, spoken words and pictures in the human brain. By means of fMRI, she is currently investigating the role of the tasks in the semantic processing.`,
          imageBaseName: 'Pic_GL-280'
        },
        {
          name: 'Doris Pischedda',
          role: 'Postdoc at CIMeC in LDMg, Mattarello, Italy',
          description: `Doris’s PhD work at the University of Milano-Bicocca investigated how and where rules are encoded in the human brain.
                        As a postdoc, she employs fMRI and multivariate decoding to characterize neural representations of choice outcomes (previously rules) in both individual and social contexts.`,
          imageBaseName: 'Pic_DP-280'
        },
        {
          name: 'Ana Luísa Pinho',
          role: 'Postdoctoral Researcher at NeuroSpin (Inria/CEA-Saclay), Paris, France',
          description: `Ana Luisa graduated in Engineering Physics at Instituto Superior Técnico (ULisboa, Portugal). During her PhD at Karolinska Institutet (Stockholm, Sweden),
                        she used fMRI to investigate the neural correlates involved in musical creativity. Now, she is developing a neuroimaging dataset to map cognition in the human brain.`,
          imageBaseName: 'Pic_AL-280'
        },
        {
          name: 'Eliana Vassena',
          role: 'Marie Curie fellow at the Donders Institute for Brain, Cognition and Behaviour (Nijmegen, NL)',
          description: `Eliana is interested in motivation and decision-making.
                        During her PhD and postdoc she has used neuroimaging, neurostimulation and computational modelling to study
                        the contribution of the prefrontal cortex to these processes. Currently, she works on translating neurocomputational models of motivation
                        to neuropsychiatric populations.`,
          imageBaseName: 'Pic_EV-280'
        }
      ]
    };
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    }
  },
  created() {
    document.title = 'Winrepo - About';
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

.card-container {
 max-width: 12.5rem;
}

#board .card-container {
 max-width: 15.5rem;
}

#board .card {
  width: 15rem;
  height: 18rem;
}


</style>
