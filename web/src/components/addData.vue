<template>
    <div id="add-data">
        <div v-if="submitted"><h3>Data has been added to elasticsearch.</h3></div>
        <div v-if="!submitted">
            <h3>Add data to Elastic</h3>
            <form>
                <input type="text" v-model="slug" placeholder="Slug" required />
                <input type="text" v-model="title" placeholder="Title" required />
                <textarea rows="10" v-model="content" placeholder="Content" required></textarea>
                <div class="center-align"><button v-on:click.prevent="post">Submit Data</button></div>
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
                this.axios.post(
                    'http://localhost:5000/add',
                    {
                        slug: this.slug,
                        title: this.title,
                        content: this.content,
                    },
                    {
                        headers: {'Content-type': 'application/json'},
                        withCredentials: true
                    }
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

    button {
        border: 1px solid teal;
        border-radius: 4px;
        width: 100px;
        height: 30px;
        text-align: center;
        max-width: 300px;
        margin: auto;
        color: teal;
    }

    input, textarea {
        display: block;
        width: 100%;
        padding: 8px;
        border: 1px solid #bdbdbd;
        border-radius: 4px;
    }

</style>