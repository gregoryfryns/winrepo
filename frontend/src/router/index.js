import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Faq from '../views/Faq.vue';
import About from '../views/About.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/list',
    name: 'list',
    component: Home
  },
  {
    path: '/create',
    name: 'create',
    component: Home
  },
  {
    path: '/recommend',
    name: 'recommend',
    component: Home
  },
  {
    path: '/faq',
    name: 'faq',
    component: Faq
  },
  {
    path: '/about',
    name: 'about',
    component: About
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () =>
    //   import(/* webpackChunkName: 'about' */ '../views/About.vue')
  }
];

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes
});

export default router;
