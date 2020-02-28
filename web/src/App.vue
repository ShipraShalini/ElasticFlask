<template>
  <div id="app">
    <add-data></add-data>
    <show-data></show-data>
  </div>
</template>

<script>
import addData from './components/addData.vue'
import showData from './components/showData.vue'


export default {
  name: 'App',
  components: {
    'add-data': addData,
    'show-data': showData
  }
}
</script>

<style>
</style>
