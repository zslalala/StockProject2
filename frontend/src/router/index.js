import Vue from 'vue'
import Router from 'vue-router'
import Layout from '../components/Layout/layout'
import Centre from '../components/Layout/center'
import File from '../components/Layout/file'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Layout',
      component: Layout,    //作为父组件的Layout，自然要在里面定义router-view，所有的东西也都是围绕着router-view做的
      children: [
        {
          path: '/',
          name: 'Centre',
          component: Centre
        },
        {
          path:'file',
          name:'File',
          component:File
        }
      ]
    },
  ]
})
