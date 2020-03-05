<template>
    <div>
        <div id="search-data" v-if="!submitted">
            <div class="wrap">
                <div class="search">
                    <input v-model="keyword" type="text" class="searchTerm" placeholder="What are you looking for?">
                    <button v-on:click.prevent="search" class="searchButton">
                        <i class="fa fa-search"></i>
                    </button>
                </div>
            </div>
        </div>
        <div id="show-data">
            <div v-if="submitted">
                <div v-if="results.length">
                    <h2>Elasticsearch hits:</h2>
                    <div v-for="result in results" v-bind:key="result._id" class="res-class">
                        <h3>{{ result._id }}</h3>
                        <p>ID: {{ result._id }}</p>
                        <p>Index: {{ result._index }}</p>
                        <p>Score: {{ result._score }}</p>
                        <p>Type: {{ result._type }}</p>
                        <p>Source: </p><pre>{{ result._source }}</pre>
                    </div>
                </div>
                <div v-else>
                    <h2>No Elasticsearch Hits.</h2>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                keyword: '',
                results: [],
                submitted: false
            }
        },
        methods: {
            search: function () {
                this.axios.post(
                    'http://localhost:5000/search',
                    {keyword: this.keyword},
                    {
                        headers: {'Content-type': 'application/json'},
                        withCredentials: true
                    }
                ).then(response => {
                    this.submitted = true;
                    this.results = response.data;
                    for (var res in this.results) {
                        var content = res._source;
                        res._source = JSON.stringify(content, undefined, 4)
                    }
                }).catch((error) => {console.log(error)})
            }
        }
    }
</script>

<style scoped>
    #search-data {
        max-width: 700px;
        margin: 0 auto;
    }
    .res-class {
        padding: 20px;
        margin: 20px 0;
        box-sizing: border-box;
        background: #eee;
    }

    h2 {
        text-align: center;
    }

    .search {
        width: 100%;
        position: relative;
        display: flex;
    }

    .searchTerm {
        width: 100%;
        border: 2px solid #bdbdbd;
        border-right: none;
        padding: 5px;
        height: 20px;
        border-radius: 5px 0 0 5px;
        outline: none;
        color: #9DBFAF;
    }

    .searchTerm:focus{
        color: black;
    }

    .searchButton {
        width: 40px;
        height: 34px;
        border: 1px solid #bdbdbd;
        background: #bdbdbd;
        text-align: center;
        color: #fff;
        border-radius: 0 5px 5px 0;
        cursor: pointer;
        font-size: 20px;
    }

</style>