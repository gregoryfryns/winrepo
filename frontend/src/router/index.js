import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import ProfilesList from '../views/ProfilesList';
import Profile from '../views/Profile';
import ProfileEditor from '../views/ProfileEditor';
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
    component: ProfilesList
  },
  {
    path: '/list/:id',
    name: 'profile',
    component: Profile,
    props: true
  },
  {
    path: '/create',
    name: 'create',
    component: ProfileEditor
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
