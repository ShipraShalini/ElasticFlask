<template>
  <div id="app">
    <h1 class="title">ElasticFlask</h1>
    <search-data class="comp"></search-data>
    <add-data class="comp" ></add-data>
  </div>
</template>


<script>
import addData from './components/addData.vue'
import searchData from './components/searchData.vue'

export default {
  name: 'App',
  components: {
    'add-data': addData,
    'search-data': searchData
  }
}
</script>


<style>
  #app {
    margin: 50px;
  }

  .comp {
    margin-bottom: 50px;
  }

  h1, h2, h3 {
    text-align: center;
  }

  .title {
    color: teal;
  }

  ::placeholder {
    padding-left: 5px;
  }
</style>
