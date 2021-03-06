from datetime import datetime

from elasticsearch import Elasticsearch

from flask import Flask, jsonify, request

from flask_cors import CORS


app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

es = Elasticsearch(hosts=[{'host': 'elasticsearch'}])


@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello!!'})


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
    keyword = request.json.get('keyword')
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
    app.run(host='0.0.0.0')
