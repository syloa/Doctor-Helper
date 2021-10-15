
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', redirect: '/home' },
      {
        path: '/home',
        component: () => import('pages/Home/Home.vue'),
        children: [
          {
            path: '/home/child',
            component: () => import('pages/Home/Child.vue'),
            children: [
              {
                path: '/home/child/grandchild',
                component: () => import('pages/Home/Grandchild.vue'),
              }
            ]
          }
        ]
      },
      {
        path: '/questions',
        component: () => import('pages/Questions/Questions.vue'),
        children: [
          {
            path: '/questions/answer',
            component: () => import('pages/Questions/Answer.vue'),
          }
        ]
      },
      {
        path: '/images',
        component: () => import('pages/Images/Images.vue'),
        children: [
          {
            path: '/images/:id',
            component: () => import('pages/Images/Image.vue'),
          }
        ]
      },
      {
        path: '/xrays',
        component: () => import('pages/Xrays/Xrays.vue'),
        children: [
          {
            path: '/xrays/:id',
            component: () => import('pages/Xrays/Xray.vue'),
          }
        ]
      },
      {
        path: '/skins',
        component: () => import('pages/Skins/Skins.vue'),
        children: [
          {
            path: '/Skins/:id',
            component: () => import('pages/Skins/Skin.vue'),
          }
        ]
      },
      {
        path: '/brains',
        component: () => import('pages/Brains/Brains.vue'),
        children: [
          {
            path: '/Brains/:id',
            component: () => import('pages/Brains/Brain.vue'),
          }
        ]
      },
      {
        path: '/label',
        component: () => import('pages/Label/Top.vue'),
        children: [
          {
            path: '/label/bottom',
            component: () => import('pages/Label/Bottom.vue'),
          },
          {
            path: '/label/bottom2',
            component: () => import('pages/Label/Bottom2.vue'),
          }
        ]
      },
      {
        path: '/Notice',
        component: () => import('pages/Notice/Notice.vue'),
      },
      {
        path: '/Settings',
        component: () => import('pages/Settings/Settings.vue'),
      },
      {
        path: '/Bookmarks',
        component: () => import('pages/Bookmarks/Bookmarks.vue'),
      },
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
