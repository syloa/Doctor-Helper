import { boot } from 'quasar/wrappers'
import axios from 'axios'

// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)
// const api = axios.create({ baseURL: 'https://api.example.com' })
// const url='http://http://192.168.1.147:'
const url='http://localhost:'

//chestapi
const api = axios.create({ baseURL: url + '5000' })
// briantumor
const api2 = axios.create({ baseURL: url + '5001' })
// skin
const api3 = axios.create({ baseURL: url + '5002' })
// db 관련 api
const apiDB = axios.create({ baseURL: url + '3030' })



export default boot(({ app }) => {
  // for use inside Vue files (Options API) through this.$axios and this.$api

  app.config.globalProperties.$axios = axios
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  app.config.globalProperties.$axios = url

  app.config.globalProperties.$api = api

  app.config.globalProperties.$api2 = api2

  app.config.globalProperties.$api3 = api3

  app.config.globalProperties.$apiDB = apiDB
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API
})

export { axios, api, api2, api3, apiDB }
