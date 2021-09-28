import { routerInstance } from 'boot/router'

export default function useGoBack() {
  let pathArray = routerInstance.currentRoute.value.path.split('/')
  if (pathArray.length > 2) {
    pathArray.pop()
    let newPath = pathArray.join('/')
    routerInstance.push(newPath)
  }
}