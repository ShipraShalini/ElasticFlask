from datetime import datetime

from elasticsearch import Elasticsearch

from flask import Flask, jsonify, request

app = Flask(__name__)

es = Elasticsearch(hosts=[{'host': 'elasticsearch'}])


@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello!!'})


@app.route('/data', methods=['GET'])
def index():
    results = es.get(index='contents', doc_type='title', id='abc')
    return jsonify(results['_source'])


@app.route('/add', methods=['POST'])
def insert_data():
    data = request.json
    slug = data['slug']
    title = data['title']
    content = data['content']

    body = {
        'slug': slug,
        'title': title,
        'content': content,
        'timestamp': datetime.now()
    }

    result = es.index(index='contents', doc_type='title', id=slug, body=body)

    return jsonify(result)


@app.route('/search', methods=['POST'])
def search():
    keyword = request.json['keyword']

    body = {
        "query": {
            "multi_match": {
                "query": keyword,
                "fields": ["content", "title"]
            }
        }
    }

    res = es.search(index="contents", doc_type="title", body=body)
    return jsonify(res['hits']['hits'])


if __name__ == '__main__':
    app.run(port=6000, debug=True)
