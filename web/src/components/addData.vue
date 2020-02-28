<template>
    <div id="add-data">
        <div v-if="submitted"><h3>Follwing Data has been added to elasticsearch.</h3></div>
        <div v-if="!submitted">
            <h2>Add new data</h2>
            <form>
                <label>Slug:</label>
                <input type="text" v-model="slug" required />
                <label>Title:</label>
                <input type="text" v-model="title" required />
                <label>Content:</label>
                <textarea v-model="content"></textarea>
                <button v-on:click.prevent="post">Add Data</button>
            </form>
        </div>

            <div id="preview">
                <h3>Preview</h3>
                <form>
                    <p>Slug: {{ slug }}</p>
                    <p>Title: {{ title }}</p>
                    <p>Content: {{ content }}</p>
                </form>
            </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                slug: '',
                title: '',
                content: '',
                submitted: false
            }
        },
        methods: {
            post: function () {
                this.axios.post('http://localhost:5000/add', {
                    slug: this.slug,
                    title: this.title,
                    content: this.content,
                }, {headers: {'Content-type': 'application/json'}}
                ).then(response => {
                    this.submitted = true;
                    return response
                }).catch((error) => {console.log(error)})
            }
        }

    }
</script>

<style scoped>
    #add-data *{
        box-sizing: border-box;
        margin: 20px auto;
        max-width: 500px;
    }
    label {
        display: block;
        margin: 20px 0 10px;
    }
    input[type='text'], textarea {
        display: block;
        width: 100%;
        padding: 8px;
    }
    h2 {
        text-align: center;
    }
</style>