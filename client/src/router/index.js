import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Books from '@/components/Books';
import Login from '@/components/Login';
import Info from '@/components/Info';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/books',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/info',
      name: 'Info',
      component: Info,
    },
  ],
  mode: 'history',
});
