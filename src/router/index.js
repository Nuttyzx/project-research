import { createRouter, createWebHistory } from 'vue-router'

import Search from '../views/show/Search.vue'; //เปิดเว็บครั้งแรกโหลดหน้า home ก่อนเลย
import Home from '../views/show/Home.vue';
import testHome from '../views/show/testHome.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/home',
      name: 'home', 
      component: Home,
      meta: {
        breadcrumb: 'Home',
      },
    },
    {
      path: '/',
      name: 'testhome', 
      component: testHome,
      meta: {
        breadcrumb: 'testHome',
      },
    },
    {
      path: '/search',
      name: 'search',
      component: Search,
      meta: {
        breadcrumb: 'Search',
      },
    },

    {
      path: '/listauthorname',
      name: 'listauthorname',
      // component: ListAuthorName
      component: () => import('../views/show/LIstAuthorName.vue'),
      meta: {
        breadcrumb: 'List Author',
      },
    },
    {
      path: '/listresearchname',
      name: 'listresearchname',
      component: () => import('../views/show/ListResearchName.vue'),
      meta: {
        breadcrumb: 'List Research',
      },
    },

    {
      path: '/graph_author/:id',
      name: 'graph_author',
      component: () => import('../views/graph/GraphAuthor.vue'),
      meta: {
        breadcrumb: 'Graph Author',
      },
    },

    {
      path: '/graph_research/:id',
      name: 'graph_research',
      component: () => import('../views/graph/GraphResearch.vue'),
      meta: {
        breadcrumb: 'Graph Research',
      },
    },
    {
      path: '/graph_expertise/:id',
      name: 'graph_expertise',
      component: () => import('../views/graph/GraphExpertise.vue'),
      meta: {
        breadcrumb: 'Graph Expertise',
      },
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/admin/Login.vue') 
    },
    {
      path: '/showuser',
      name: 'showuser',
      component: () => import('../views/admin/ShowUser.vue') //ไปยัง /showuser ค่อยโหลด
    },
    {
      path: '/showresearch',
      name: 'showresearch',
      component: () => import('../views/admin/ShowResearch.vue')
    },
    {
      path: '/addSuccess',
      name: 'addSuccess',
      component: () => import('../views/admin/AddSuccess.vue')
    },
    {
      path: '/addResearch',
      component: () => import('../views/admin/AddResearch.vue')
    },
    {
      path: '/testaddResearch',
      component: () => import('../views/admin/testAddResearch.vue')
    },
    {
      path: '/add',
      name: 'add',
      component: () => import('../views/admin/Add.vue')
    },
    {
      path: '/addscopus',
      name: 'addscopus',
      component: () => import('../views/admin/AddScopus.vue')
    },
    {
      path: '/editResearch/:id',
      name: 'editresearch',
      component: () => import('../views/admin/EditResearch.vue')
    },
    {
      path: '/editUser/:id',
      name: 'edituser',
      component: () => import('../views/admin/EditUser.vue')
    },
    {
      path: '/test',
      name: 'test',
      component: () => import('../views/test.vue')
    }
  ]
})

export default router
