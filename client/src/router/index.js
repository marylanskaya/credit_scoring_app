import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Books from '@/components/Books';
import Login from '@/components/Login';
import Info from '@/components/Info';
import Profile from '@/components/Profile';
import HelloWorld from '@/components/HelloWorld';


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
      props: true,
    },
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld,
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile,
      props: true,
    },
  ],
  mode: 'history',
});
